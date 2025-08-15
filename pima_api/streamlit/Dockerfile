FROM python:3.10.18-slim

RUN pip install --upgrade pip && pip install poetry

COPY . /pima-API

WORKDIR /pima-API

RUN poetry install

ENTRYPOINT ["poetry", "run"]

EXPOSE 8501

CMD ["streamlit", "run", "streamlit/app.py"]