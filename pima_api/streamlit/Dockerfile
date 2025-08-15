FROM python:3.10.18-slim

WORKDIR /app

COPY pima_api/streamlit /app

RUN pip install --no-cache-dir streamlit requests

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]