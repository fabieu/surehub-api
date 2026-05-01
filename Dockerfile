# ── Stage 1: build dependencies ──────────────────────────────────────────────
FROM python:3.15.0a8-alpine AS builder

ARG POETRY_VERSION=2.3.2

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1

RUN pip install --no-cache-dir "poetry==${POETRY_VERSION}"

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN poetry install --only main --no-root

COPY surehub_api ./surehub_api
RUN poetry install --only main

# ── Stage 2: runtime image ────────────────────────────────────────────────────
FROM python:3.15.0a8-alpine AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

COPY --from=builder /app/.venv .venv
COPY --from=builder /app/surehub_api ./surehub_api

USER appuser

EXPOSE 3001

ENTRYPOINT ["python", "surehub_api/main.py"]