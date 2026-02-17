from fastapi import Depends, Header
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.domain.models import APIError, User
from app.security.auth import decode_access_token


def get_current_user(authorization: str | None = Header(default=None), db: Session = Depends(get_db)) -> User:
    if not authorization or not authorization.lower().startswith("bearer "):
        raise APIError("UNAUTHORIZED", "Missing bearer token", status_code=401)
    token = authorization.split(" ", 1)[1]
    try:
        payload = decode_access_token(token)
    except Exception as exc:  # noqa: BLE001
        raise APIError("UNAUTHORIZED", "Invalid token", status_code=401) from exc
    user = db.get(User, payload["sub"])
    if not user:
        raise APIError("UNAUTHORIZED", "User not found", status_code=401)
    return user


def require_roles(*roles: str):
    def checker(user: User = Depends(get_current_user)) -> User:
        if user.role.value not in roles:
            raise APIError("FORBIDDEN", "Insufficient role", status_code=403)
        return user

    return checker
