FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

ENV UV_SYSTEM_PYTHON=1
ENV UV_PYTHON_DOWNLOADS=0
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-dev

COPY ./monolith/ /app
COPY uv.lock /app/uv.lock
COPY pyproject.toml /app/pyproject.toml

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev


FROM python:3.12-slim-bookworm

WORKDIR /app

COPY --from=builder --chown=app:app /app /app

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="."

ENTRYPOINT [ "./entrypoint.sh" ]

CMD [ "fastapi", "run", "app/main.py", "--proxy-headers", "--port", "8000" ]
