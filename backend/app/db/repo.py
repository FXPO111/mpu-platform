from datetime import datetime
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.domain.models import (
    AIEvaluation,
    AIMessage,
    AISession,
    Booking,
    Entitlement,
    Order,
    PaymentEvent,
    Product,
    Slot,
    User,
)


class Repo:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, email: str, password_hash: str, name: str, locale: str = "de") -> User:
        user = User(email=email.lower(), password_hash=password_hash, name=name, locale=locale)
        self.db.add(user)
        self.db.flush()
        return user

    def get_user_by_email(self, email: str) -> User | None:
        return self.db.scalar(select(User).where(User.email == email.lower()))

    def create_ai_session(self, user_id: UUID, mode: str, locale: str) -> AISession:
        session = AISession(user_id=user_id, mode=mode, locale=locale)
        self.db.add(session)
        self.db.flush()
        return session

    def get_ai_session(self, session_id: UUID) -> AISession | None:
        return self.db.get(AISession, session_id)

    def add_message(self, session_id: UUID, role: str, content: str) -> AIMessage:
        message = AIMessage(session_id=session_id, role=role, content=content)
        self.db.add(message)
        self.db.flush()
        return message

    def list_messages(self, session_id: UUID) -> list[AIMessage]:
        return list(self.db.scalars(select(AIMessage).where(AIMessage.session_id == session_id).order_by(AIMessage.created_at)).all())

    def add_evaluation(self, session_id: UUID, message_id: UUID, rubric_scores: dict, summary_feedback: str, detected_issues: dict):
        row = AIEvaluation(
            session_id=session_id,
            message_id=message_id,
            rubric_scores=rubric_scores,
            summary_feedback=summary_feedback,
            detected_issues=detected_issues,
        )
        self.db.add(row)
        return row

    def consume_credit(self, user_id: UUID) -> bool:
        ent = self.db.scalar(
            select(Entitlement)
            .where(Entitlement.user_id == user_id, Entitlement.kind == "ai_credits")
            .order_by(Entitlement.valid_to.is_(None).desc(), Entitlement.created_at)
            .with_for_update()
        )
        if not ent or ent.qty_used >= ent.qty_total:
            return False
        ent.qty_used += 1
        return True

    def list_open_slots(self) -> list[Slot]:
        return list(self.db.scalars(select(Slot).where(Slot.status == "open").order_by(Slot.starts_at_utc)).all())

    def book_slot(self, user_id: UUID, slot_id: UUID) -> Booking:
        slot = self.db.get(Slot, slot_id, with_for_update=True)
        if not slot or slot.status != "open":
            raise ValueError("Slot not available")
        slot.status = "booked"
        booking = Booking(user_id=user_id, slot_id=slot_id, status="confirmed")
        self.db.add(booking)
        self.db.flush()
        return booking

    def create_order(self, user_id: UUID, product: Product, provider_ref: str) -> Order:
        order = Order(
            user_id=user_id,
            product_id=product.id,
            amount_cents=product.price_cents,
            currency=product.currency,
            provider_ref=provider_ref,
            status="pending",
        )
        self.db.add(order)
        self.db.flush()
        return order

    def get_product(self, product_id: UUID) -> Product | None:
        return self.db.get(Product, product_id)

    def list_products(self) -> list[Product]:
        return list(self.db.scalars(select(Product).where(Product.active.is_(True))).all())

    def insert_payment_event(self, provider: str, event_id: str, event_type: str, payload: dict) -> tuple[PaymentEvent, bool]:
        existing = self.db.scalar(select(PaymentEvent).where(PaymentEvent.event_id == event_id))
        if existing:
            return existing, False
        evt = PaymentEvent(provider=provider, event_id=event_id, type=event_type, payload_json=payload)
        self.db.add(evt)
        self.db.flush()
        return evt, True

    def mark_payment_event_processed(self, evt: PaymentEvent):
        evt.processed_at = datetime.utcnow()

    def find_order_by_provider_ref(self, provider_ref: str) -> Order | None:
        return self.db.scalar(select(Order).where(Order.provider_ref == provider_ref))

    def grant_entitlement_once(self, order: Order, kind: str, qty_total: int):
        existing = self.db.scalar(select(Entitlement).where(Entitlement.source_order_id == order.id, Entitlement.kind == kind))
        if existing:
            return existing
        ent = Entitlement(user_id=order.user_id, kind=kind, qty_total=qty_total, source_order_id=order.id)
        self.db.add(ent)
        order.status = "paid"
        return ent
