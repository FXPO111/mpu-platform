from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any
from uuid import UUID, uuid4

from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import (
    JSON,
    DateTime,
    Enum as SAEnum,
    Float,
    ForeignKey,
    Index,
    Integer,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import ARRAY, UUID as PGUUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Role(str, Enum):
    user = "user"
    admin = "admin"
    consultant = "consultant"


class UserStatus(str, Enum):
    active = "active"
    blocked = "blocked"
    deleted = "deleted"


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    email: Mapped[str] = mapped_column(String(320), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(120))
    locale: Mapped[str] = mapped_column(String(5), default="de")
    timezone: Mapped[str | None] = mapped_column(String(64), nullable=True)
    role: Mapped[Role] = mapped_column(SAEnum(Role), default=Role.user)
    status: Mapped[UserStatus] = mapped_column(SAEnum(UserStatus), default=UserStatus.active)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)


class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), index=True)
    token_hash: Mapped[str] = mapped_column(String(255), index=True)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    revoked_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)


class AuditLog(Base):
    __tablename__ = "audit_log"
    __table_args__ = (Index("ix_audit_entity_created", "entity_type", "entity_id", "created_at"),)

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    actor_user_id: Mapped[UUID | None] = mapped_column(ForeignKey("users.id"), nullable=True)
    action: Mapped[str] = mapped_column(String(64))
    entity_type: Mapped[str] = mapped_column(String(64), index=True)
    entity_id: Mapped[str] = mapped_column(String(64), index=True)
    ip: Mapped[str | None] = mapped_column(String(64), nullable=True)
    user_agent: Mapped[str | None] = mapped_column(String(255), nullable=True)
    payload_json: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)


class Topic(Base):
    __tablename__ = "topics"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    slug: Mapped[str] = mapped_column(String(60), unique=True)
    title_de: Mapped[str] = mapped_column(String(255))
    title_en: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)


class Question(Base):
    __tablename__ = "questions"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    topic_id: Mapped[UUID] = mapped_column(ForeignKey("topics.id"), index=True)
    level: Mapped[int] = mapped_column(Integer)
    question_de: Mapped[str] = mapped_column(Text)
    question_en: Mapped[str] = mapped_column(Text)
    intent: Mapped[str] = mapped_column(Text)
    tags: Mapped[list[str]] = mapped_column(ARRAY(String), default=list)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)


class Rubric(Base):
    __tablename__ = "rubrics"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    code: Mapped[str] = mapped_column(String(64), unique=True)
    title_de: Mapped[str] = mapped_column(String(255))
    title_en: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)
    scale_min: Mapped[int] = mapped_column(Integer, default=0)
    scale_max: Mapped[int] = mapped_column(Integer, default=5)


class Material(Base):
    __tablename__ = "materials"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    topic_id: Mapped[UUID] = mapped_column(ForeignKey("topics.id"), index=True)
    title_de: Mapped[str] = mapped_column(String(255))
    title_en: Mapped[str] = mapped_column(String(255))
    body: Mapped[str] = mapped_column(Text)
    source_url: Mapped[str | None] = mapped_column(String(1000), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)


class AISession(Base):
    __tablename__ = "ai_sessions"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), index=True)
    mode: Mapped[str] = mapped_column(String(32))
    locale: Mapped[str] = mapped_column(String(5), default="de")
    status: Mapped[str] = mapped_column(String(32), default="active")
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    closed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)


class AIMessage(Base):
    __tablename__ = "ai_messages"
    __table_args__ = (Index("ix_ai_messages_session_created", "session_id", "created_at"),)

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    session_id: Mapped[UUID] = mapped_column(ForeignKey("ai_sessions.id"))
    role: Mapped[str] = mapped_column(String(32))
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)


class AIEvaluation(Base):
    __tablename__ = "ai_evaluations"
    __table_args__ = (Index("ix_ai_evals_session_created", "session_id", "created_at"),)

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    session_id: Mapped[UUID] = mapped_column(ForeignKey("ai_sessions.id"))
    message_id: Mapped[UUID] = mapped_column(ForeignKey("ai_messages.id"))
    rubric_scores: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    summary_feedback: Mapped[str] = mapped_column(Text)
    detected_issues: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)


class Slot(Base):
    __tablename__ = "slots"
    __table_args__ = (Index("ix_slots_consultant_starts", "consultant_id", "starts_at_utc"),)

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    consultant_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    starts_at_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    duration_min: Mapped[int] = mapped_column(Integer)
    title: Mapped[str] = mapped_column(String(255))
    meeting_provider: Mapped[str] = mapped_column(String(32), default="manual")
    meeting_url: Mapped[str | None] = mapped_column(String(2000), nullable=True)
    status: Mapped[str] = mapped_column(String(32), default="open")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)


class Booking(Base):
    __tablename__ = "bookings"
    __table_args__ = (
        UniqueConstraint("slot_id", name="uq_booking_slot_id"),
        Index("ix_bookings_user_created", "user_id", "created_at"),
    )

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    slot_id: Mapped[UUID] = mapped_column(ForeignKey("slots.id"))
    status: Mapped[str] = mapped_column(String(32), default="confirmed")
    client_note: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)


class Product(Base):
    __tablename__ = "products"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    code: Mapped[str] = mapped_column(String(64), unique=True)
    type: Mapped[str] = mapped_column(String(32))
    name_de: Mapped[str] = mapped_column(String(255))
    name_en: Mapped[str] = mapped_column(String(255))
    price_cents: Mapped[int] = mapped_column(Integer)
    currency: Mapped[str] = mapped_column(String(3), default="EUR")
    stripe_price_id: Mapped[str | None] = mapped_column(String(128), nullable=True)
    metadata_json: Mapped[dict[str, Any]] = mapped_column("metadata", JSON, default=dict)
    active: Mapped[bool] = mapped_column(default=True)


class Order(Base):
    __tablename__ = "orders"
    __table_args__ = (UniqueConstraint("provider", "provider_ref", name="uq_order_provider_ref"),)

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    product_id: Mapped[UUID] = mapped_column(ForeignKey("products.id"))
    amount_cents: Mapped[int] = mapped_column(Integer)
    currency: Mapped[str] = mapped_column(String(3))
    status: Mapped[str] = mapped_column(String(32), default="created")
    provider: Mapped[str] = mapped_column(String(32), default="stripe")
    provider_ref: Mapped[str] = mapped_column(String(128))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)


class PaymentEvent(Base):
    __tablename__ = "payments_events"
    __table_args__ = (Index("ix_payment_events_processed", "processed_at"),)

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    provider: Mapped[str] = mapped_column(String(32), default="stripe")
    event_id: Mapped[str] = mapped_column(String(128), unique=True)
    type: Mapped[str] = mapped_column(String(128))
    payload_json: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    received_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    processed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)


class Entitlement(Base):
    __tablename__ = "entitlements"
    __table_args__ = (Index("ix_entitlements_user_kind_valid", "user_id", "kind", "valid_to"),)

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), index=True)
    kind: Mapped[str] = mapped_column(String(32))
    qty_total: Mapped[int] = mapped_column(Integer)
    qty_used: Mapped[int] = mapped_column(Integer, default=0)
    valid_from: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    valid_to: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    source_order_id: Mapped[UUID] = mapped_column(ForeignKey("orders.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)


class APIError(Exception):
    def __init__(self, code: str, message: str, details: dict[str, Any] | None = None, status_code: int = 400):
        self.code = code
        self.message = message
        self.details = details or {}
        self.status_code = status_code
        super().__init__(message)


class RegisterIn(BaseModel):
    email: EmailStr
    password: str = Field(min_length=10)
    name: str
    locale: str = "de"


class LoginIn(BaseModel):
    email: EmailStr
    password: str


class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"


class SessionCreateIn(BaseModel):
    mode: str
    locale: str = "de"


class MessageIn(BaseModel):
    content: str = Field(min_length=1)


class CheckoutIn(BaseModel):
    product_id: UUID


class ErrorEnvelope(BaseModel):
    error: dict[str, Any]


class DataEnvelope(BaseModel):
    data: Any
