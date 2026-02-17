from sqlalchemy.orm import Session

from app.db.repo import Repo
from app.domain.models import APIError


PRODUCT_TO_ENTITLEMENT = {
    "ai_pack": ("ai_credits", 50),
    "booking": ("booking_access", 1),
}


def apply_paid_event(db: Session, provider_ref: str):
    repo = Repo(db)
    order = repo.find_order_by_provider_ref(provider_ref)
    if not order:
        raise APIError("ORDER_NOT_FOUND", "Order for provider reference not found", status_code=404)
    if order.status == "paid":
        return
    kind, qty = PRODUCT_TO_ENTITLEMENT.get(order.product.type, ("ai_credits", 50))
    repo.grant_entitlement_once(order, kind, qty)
