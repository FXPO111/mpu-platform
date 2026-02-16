# MPU Platform

MVP platform for MPU AI preparation and consultation booking.

## Stack
- Backend: FastAPI + PostgreSQL + Alembic + pgvector
- Frontend: Next.js
- Payments: Stripe webhooks (idempotent)

## Run
```bash
cd infra
docker compose up --build
```

## Backend local
```bash
cd backend
pip install -e .[test]
alembic upgrade head
uvicorn app.main:app --reload
```

## Seed
Use Python shell and call seed helpers from `app.db.seeds.seed_data`.

## Smoke checklist
1. `POST /api/auth/register` -> returns user id.
2. `POST /api/auth/login` -> returns bearer token.
3. `POST /api/payments/checkout` with product id -> creates order.
4. `POST /api/payments/webhook` with valid signature -> grants entitlement.
5. `POST /api/ai/sessions` + `/messages` -> consumes one AI credit.
6. `POST /api/booking/slots/{id}/book` from two users -> only one success.
