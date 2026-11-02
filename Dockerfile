FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim AS builder

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /app

COPY pyproject.toml .
RUN uv venv /app/.venv && \
    uv pip install --no-cache -r pyproject.toml

FROM python:3.13-slim AS runner

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

RUN useradd -m -u 1000 appuser

COPY --from=builder /app/.venv /app/.venv
COPY --chown=appuser:appuser app ./app

USER appuser

CMD ["python", "-m", "app"]
