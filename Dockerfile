FROM python:3.14.1-alpine

ARG POETRY_VERSION=2.2.1

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/root/.local/bin:$PATH"

# System deps (build + runtime)
RUN apk add --no-cache --virtual .build-deps \
        curl \
        gcc \
        libffi-dev \
        musl-dev \
    && python -m pip install --no-cache-dir "poetry==${POETRY_VERSION}" \
    && apk del .build-deps

WORKDIR /usr/src/app

COPY surehub_api ./surehub_api
COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --only main

EXPOSE 3001

ENTRYPOINT ["python", "surehub_api/main.py"]