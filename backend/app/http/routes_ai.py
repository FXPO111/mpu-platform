from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.repo import Repo
from app.db.session import get_db
from app.deps import get_current_user
from app.domain.models import APIError, MessageIn, SessionCreateIn
from app.services.ai_orchestrator import process_user_message

router = APIRouter(prefix="/api/ai", tags=["ai"])


@router.post("/sessions")
def create_session(payload: SessionCreateIn, user=Depends(get_current_user), db: Session = Depends(get_db)):
    repo = Repo(db)
    session = repo.create_ai_session(user.id, payload.mode, payload.locale)
    db.commit()
    return {"data": {"id": str(session.id), "mode": session.mode, "locale": session.locale, "status": session.status}}


@router.get("/sessions/{session_id}")
def get_session(session_id: UUID, user=Depends(get_current_user), db: Session = Depends(get_db)):
    repo = Repo(db)
    sess = repo.get_ai_session(session_id)
    if not sess or sess.user_id != user.id:
        raise APIError("NOT_FOUND", "Session not found", status_code=404)
    return {"data": {"id": str(sess.id), "mode": sess.mode, "status": sess.status}}


@router.get("/sessions/{session_id}/messages")
def messages(session_id: UUID, user=Depends(get_current_user), db: Session = Depends(get_db)):
    repo = Repo(db)
    sess = repo.get_ai_session(session_id)
    if not sess or sess.user_id != user.id:
        raise APIError("NOT_FOUND", "Session not found", status_code=404)
    rows = repo.list_messages(session_id)
    return {"data": [{"id": str(m.id), "role": m.role, "content": m.content, "created_at": m.created_at.isoformat()} for m in rows]}


@router.post("/sessions/{session_id}/messages")
def send_message(session_id: UUID, payload: MessageIn, user=Depends(get_current_user), db: Session = Depends(get_db)):
    repo = Repo(db)
    sess = repo.get_ai_session(session_id)
    if not sess or sess.user_id != user.id:
        raise APIError("NOT_FOUND", "Session not found", status_code=404)
    if not repo.consume_credit(user.id):
        raise APIError("NO_CREDITS", "No AI credits left. Please buy an AI package.", {"pricing_url": "/pricing"}, 402)
    assistant = process_user_message(db, session_id, payload.content, sess.locale, sess.mode)
    db.commit()
    return {"data": {"assistant_message": {"id": str(assistant.id), "content": assistant.content}}}


@router.post("/sessions/{session_id}/close")
def close_session(session_id: UUID, user=Depends(get_current_user), db: Session = Depends(get_db)):
    repo = Repo(db)
    sess = repo.get_ai_session(session_id)
    if not sess or sess.user_id != user.id:
        raise APIError("NOT_FOUND", "Session not found", status_code=404)
    sess.status = "closed"
    db.commit()
    return {"data": {"id": str(sess.id), "status": "closed"}}
