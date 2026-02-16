from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.repo import Repo
from app.db.session import get_db
from app.deps import get_current_user
from app.domain.models import Booking
from app.services.booking import create_booking

router = APIRouter(prefix="/api/booking", tags=["booking"])


@router.get("/slots")
def get_slots(db: Session = Depends(get_db)):
    rows = Repo(db).list_open_slots()
    return {"data": [{"id": str(s.id), "starts_at_utc": s.starts_at_utc.isoformat(), "title": s.title} for s in rows]}


@router.post("/slots/{slot_id}/reserve")
def reserve(slot_id: UUID):
    return {"data": {"slot_id": str(slot_id), "status": "pending_payment"}}


@router.post("/slots/{slot_id}/book")
def book(slot_id: UUID, user=Depends(get_current_user), db: Session = Depends(get_db)):
    booking = create_booking(db, user.id, slot_id)
    db.commit()
    return {"data": {"booking_id": str(booking.id), "status": booking.status}}


@router.get("/my")
def my_bookings(user=Depends(get_current_user), db: Session = Depends(get_db)):
    rows = db.scalars(select(Booking).where(Booking.user_id == user.id).order_by(Booking.created_at.desc())).all()
    return {"data": [{"id": str(b.id), "slot_id": str(b.slot_id), "status": b.status} for b in rows]}


@router.post("/{booking_id}/cancel")
def cancel_booking(booking_id: UUID, user=Depends(get_current_user), db: Session = Depends(get_db)):
    booking = db.get(Booking, booking_id)
    if booking and booking.user_id == user.id:
        booking.status = "cancelled"
        db.commit()
    return {"data": {"id": str(booking_id), "status": "cancelled"}}
