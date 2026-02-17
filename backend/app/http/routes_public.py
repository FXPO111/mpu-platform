from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.repo import Repo
from app.db.session import get_db

router = APIRouter(prefix="/api/public", tags=["public"])


@router.get("/expert")
def expert():
    return {
        "data": {
            "bio": "Certified MPU consultant",
            "languages": ["de", "en"],
            "city_for_offline": "Berlin",
            "pricing_summary": "AI packs + paid consultation slots",
        }
    }


@router.get("/products")
def products(db: Session = Depends(get_db)):
    repo = Repo(db)
    rows = repo.list_products()
    return {"data": [{"id": str(p.id), "code": p.code, "price_cents": p.price_cents, "currency": p.currency, "type": p.type} for p in rows]}


@router.get("/slots")
def slots(db: Session = Depends(get_db)):
    repo = Repo(db)
    rows = repo.list_open_slots()
    return {"data": [{"id": str(s.id), "starts_at_utc": s.starts_at_utc.isoformat(), "duration_min": s.duration_min, "title": s.title} for s in rows]}
