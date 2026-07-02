# AI Interview Platform

AI Interview Platform is a FastAPI backend for practicing technical interviews with AI-generated questions, stored answers, automated evaluation, and interview history.

The MVP flow is:

```text
register/login -> profile -> create interview -> generate questions -> answer questions -> evaluate -> view results
```

## Current Stack

- FastAPI
- PostgreSQL
- SQLAlchemy async
- Alembic
- Poetry
- Docker Compose

Planned later: OpenAI integration, Redis, RabbitMQ, background workers, cloud deployment, and GraphQL.


## Requirements

- Python 3.13
- Poetry
- Docker Desktop

## Setup

Install dependencies:

```bash
poetry install --no-root
```

Create a local `.env` file based on the project settings. Example:

```env
POSTGRES_DB=ai_interview_platform
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
PGADMIN_EMAIL=admin@example.com
PGADMIN_PASSWORD=admin
SECRET_KEY=change-me
ACCESS_TOKEN_EXPIRE_MINUTES=30
ALGORITHM=HS256
```

Start PostgreSQL:

```bash
docker compose up -d
```

Run the API locally:

```bash
poetry run python -m uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/health
```

## Database Migrations

Create a migration:

```bash
poetry run alembic revision --autogenerate -m "create users table"
```

Apply migrations:

```bash
poetry run alembic upgrade head
```

Check current migration:

```bash
poetry run alembic current
```

## Development Notes

- Use Poetry's environment for local commands.
- Keep real secrets in `.env`; do not commit `.env`.
- Use Docker Compose for local PostgreSQL.
- Keep migrations reviewed before applying them.

## Docs

Project planning documents live in `docs/`.
