# Practicum Web

Full-stack web application — **Angular 22** frontend + **FastAPI** backend.

## Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Angular 22, SCSS, standalone components |
| Backend | Python 3.11+, FastAPI, Pydantic v2, SQLAlchemy 2 |
| Auth | JWT (python-jose + passlib) |
| Linting | ESLint + Prettier (FE) · Ruff + mypy (BE) |
| Hooks | pre-commit |

---

## Quick Start

### Prerequisites
- Node.js ≥ 18, npm ≥ 9
- Python ≥ 3.11
- `pip install pre-commit`

### 1 — Clone & install hooks
```bash
git clone <repo-url> && cd practicum-web
pre-commit install
```

### 2 — Backend
```bash
cd backend
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

pip install -e ".[dev]"
cp .env.example .env          # edit values as needed
uvicorn app.main:app --reload --port 8000
```
API docs → http://localhost:8000/api/v1/docs

### 3 — Frontend
```bash
cd frontend
npm install
npm start                     # http://localhost:4200
```

---

## Project Structure

```
practicum-web/
├── backend/
│   ├── app/
│   │   ├── main.py           # FastAPI app + CORS
│   │   ├── core/
│   │   │   ├── config.py     # pydantic-settings
│   │   │   └── security.py   # JWT + password hashing
│   │   ├── api/v1/
│   │   │   ├── router.py     # aggregates all endpoint routers
│   │   │   └── endpoints/    # one file per resource
│   │   ├── models/           # SQLAlchemy ORM models
│   │   ├── schemas/          # Pydantic request/response DTOs
│   │   └── services/         # business logic layer
│   └── tests/
├── frontend/
│   └── src/app/
│       ├── core/
│       │   ├── guards/       # route guards
│       │   ├── interceptors/ # HTTP interceptors
│       │   └── services/     # singleton services (ApiService…)
│       ├── shared/
│       │   └── components/   # ButtonComponent, CardComponent, LoadingSpinner
│       ├── layout/
│       │   └── header/
│       └── features/
│           └── home/         # lazy-loaded feature pages
├── .pre-commit-config.yaml
├── docker-compose.yml
└── CHECKLIST.md
```

---

## Scripts

### Backend
```bash
pytest                        # run tests
ruff check backend/ --fix     # lint
ruff format backend/          # format
mypy backend/app/             # type-check
```

### Frontend
```bash
npm run lint                  # ESLint
npm run lint:fix              # ESLint with auto-fix
npm run format                # Prettier write
npm run format:check          # Prettier check (CI)
npm test                      # Vitest unit tests
npm run build:prod            # production build
```

---

## Adding a New Feature

1. **Backend**: add endpoint in `backend/app/api/v1/endpoints/`, register in `router.py`
2. **Frontend**: create feature folder under `src/app/features/`, add lazy route in `app.routes.ts`
3. **Shared UI**: add reusable component under `src/app/shared/components/`

## Environment Variables

Copy `backend/.env.example` to `backend/.env` and fill in:

| Variable | Description |
|----------|-------------|
| `SECRET_KEY` | JWT signing key (`openssl rand -hex 32`) |
| `DATABASE_URL` | SQLAlchemy connection string |
| `BACKEND_CORS_ORIGINS` | JSON array of allowed origins |

---

## Contributing

See [CHECKLIST.md](CHECKLIST.md) before opening a PR.
