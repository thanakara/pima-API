# -------- Stage 1: Build --------
FROM python:3.10.18-slim AS builder

# Install build tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && pip install --upgrade pip \
    && pip install --no-cache-dir poetry

WORKDIR /app

COPY . /app/

# Install dependencies to virtualenv
RUN poetry config virtualenvs.create true \
    && poetry config virtualenvs.in-project true \
    && poetry install --with dev

# Run your model preparation script (if needed at build time)
RUN poetry run python \
    pima_api/model/hydrajob_localmode.py \
    model=xgboost ++seed=2025

# -------- Stage 2: Runtime --------
FROM python:3.10.18-slim

WORKDIR /app

# Install runtime dependencies only (copy venv from builder)
COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app /app

# Set environment to use Poetry virtualenv
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 80

CMD ["uvicorn", "pima_api.fastapi.app:api", "--host", "0.0.0.0", "--port", "80"]

