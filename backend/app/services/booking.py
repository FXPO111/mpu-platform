from uuid import UUID

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.repo import Repo
from app.domain.models import APIError


def create_booking(db: Session, user_id: UUID, slot_id: UUID):
    repo = Repo(db)
    try:
        booking = repo.book_slot(user_id, slot_id)
        return booking
    except (ValueError, IntegrityError) as exc:
        raise APIError("SLOT_UNAVAILABLE", "Slot already booked", status_code=409) from exc
