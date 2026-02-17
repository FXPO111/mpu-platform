from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.db.repo import Repo
from app.db.session import get_db
from app.deps import get_current_user
from app.domain.models import APIError, LoginIn, RegisterIn
from app.security.auth import create_access_token, hash_password, verify_password
from app.security.rate_limit import limiter

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/register")
@limiter.limit("5/minute")
def register(request: Request, payload: RegisterIn, db: Session = Depends(get_db)):
    repo = Repo(db)
    if repo.get_user_by_email(payload.email):
        raise APIError("EMAIL_EXISTS", "Email already registered", status_code=409)
    user = repo.create_user(payload.email, hash_password(payload.password), payload.name, payload.locale)
    db.commit()
    return {"data": {"id": str(user.id), "email": user.email}}


@router.post("/login")
@limiter.limit("5/minute")
def login(request: Request, payload: LoginIn, db: Session = Depends(get_db)):
    repo = Repo(db)
    user = repo.get_user_by_email(payload.email)
    if not user or not verify_password(payload.password, user.password_hash):
        raise APIError("INVALID_CREDENTIALS", "Invalid credentials", status_code=401)
    token = create_access_token(str(user.id), user.role.value)
    return {"data": {"access_token": token, "token_type": "bearer"}}


@router.post("/logout")
def logout():
    return {"data": {"ok": True}}


@router.get("/me")
def me(user=Depends(get_current_user)):
    return {
        "data": {
            "id": str(user.id),
            "email": user.email,
            "name": user.name,
            "locale": user.locale,
            "role": user.role.value,
        }
    }
