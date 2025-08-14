FROM python:3.10.18-slim

RUN pip install --upgrade pip && pip install poetry

COPY . /pima-API

WORKDIR /pima-API

RUN poetry install

RUN poetry run python \
    pima_api/model/hydrajob_localmode.py \
    model=xgboost ++seed=2025

ENTRYPOINT ["poetry", "run"]

EXPOSE 8080

CMD ["fastapi", "run", "fastapi/app.py", "--host", "0.0.0.0", "--port", "8080"]