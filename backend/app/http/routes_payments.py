from fastapi import APIRouter, Depends, Header, Request
from sqlalchemy.orm import Session

from app.db.repo import Repo
from app.db.session import get_db
from app.deps import get_current_user
from app.domain.models import APIError, CheckoutIn
from app.integrations.payments_stripe import create_checkout_session_stub, parse_event, verify_signature
from app.services.payments import apply_paid_event
from app.settings import settings

router = APIRouter(prefix="/api/payments", tags=["payments"])


@router.post("/checkout")
def checkout(payload: CheckoutIn, user=Depends(get_current_user), db: Session = Depends(get_db)):
    repo = Repo(db)
    product = repo.get_product(payload.product_id)
    if not product or not product.active:
        raise APIError("PRODUCT_NOT_FOUND", "Product not found", status_code=404)
    provider_ref = f"pi_{user.id.hex[:8]}_{product.id.hex[:8]}"
    order = repo.create_order(user.id, product, provider_ref)
    session = create_checkout_session_stub(str(order.id))
    db.commit()
    return {"data": {"checkout_session_id": session["id"], "checkout_url": session["url"], "provider_ref": provider_ref}}


@router.post("/webhook")
async def webhook(request: Request, stripe_signature: str | None = Header(default=None), db: Session = Depends(get_db)):
    payload = await request.body()
    if not stripe_signature or not verify_signature(payload, stripe_signature, settings.stripe_webhook_secret):
        raise APIError("INVALID_SIGNATURE", "Invalid webhook signature", status_code=401)

    event = parse_event(payload)
    repo = Repo(db)
    evt, is_new = repo.insert_payment_event("stripe", event["id"], event["type"], event)
    if is_new and event["type"] in {"payment_intent.succeeded", "checkout.session.completed"}:
        provider_ref = event.get("data", {}).get("object", {}).get("metadata", {}).get("provider_ref")
        if provider_ref:
            apply_paid_event(db, provider_ref)
    repo.mark_payment_event_processed(evt)
    db.commit()
    return {"data": {"received": True, "deduplicated": not is_new}}
