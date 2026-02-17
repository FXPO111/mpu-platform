from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.domain.models import Question


def next_question(db: Session, locale: str = "de") -> str:
    q = db.scalar(select(Question).order_by(func.random()))
    if not q:
        return "Bitte schildern Sie kurz Ihre aktuelle Situation rund um das MPU-Thema."
    return q.question_de if locale == "de" else q.question_en
