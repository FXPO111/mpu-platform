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

1. Create `backend/.env` from `.env.example` and set real values:

```env
APP_ENV=dev
FRONTEND_URL=http://localhost:3000
CORS_ALLOW_ORIGINS=http://localhost:3000
DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/mpu
JWT_SECRET=change-me
JWT_EXP_MINUTES=60
STRIPE_SECRET_KEY=sk_test_xxx
STRIPE_WEBHOOK_SECRET=whsec_xxx
```

2. Use one-line Python checks in PowerShell (not bash heredoc):

```powershell
python -c "import psycopg; psycopg.connect('postgresql://postgres:postgres@localhost:5432/mpu').close(); print('DB OK')"
python -m alembic upgrade head
```

3. If `alembic upgrade head` fails with `password authentication failed for user "postgres"`, your DB credentials do not match `DATABASE_URL`.
   - Fix `DATABASE_URL` to your real user/password/database, or
   - Recreate postgres with default creds (`postgres/postgres`, db `mpu`) and rerun migrations.

## Seed
Use Python shell and call seed helpers from `app.db.seeds.seed_data`.

## Smoke checklist
1. `POST /api/auth/register` -> returns user id.
2. `POST /api/auth/login` -> returns bearer token.
3. `POST /api/payments/checkout` with product id -> creates order.
4. `POST /api/payments/webhook` with valid signature -> grants entitlement.
5. `POST /api/ai/sessions` + `/messages` -> consumes one AI credit.
6. `POST /api/booking/slots/{id}/book` from two users -> only one success.
