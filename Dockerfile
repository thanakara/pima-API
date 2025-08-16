FROM python:3.10.18-slim AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && pip install --upgrade pip \
    && pip install --no-cache-dir poetry

WORKDIR /app

COPY . /app/

RUN poetry config virtualenvs.create true \
    && poetry config virtualenvs.in-project true \
    && poetry install --with dev

RUN poetry run python \
    pima_api/model/hydrajob_localmode.py \
    model=xgboost ++seed=2025

# @_runtime_
FROM python:3.10.18-slim

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app /app

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 80 8501

CMD ["sh", "-c", "uvicorn pima_api.fastapi.app:api --host 0.0.0.0 --port 80 & streamlit run pima_api/streamlit/app.py --server.port=8501 --server.address=0.0.0.0"]