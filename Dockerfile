FROM python:3.10-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/


# Copy the project into the image
ADD . /pima-api

# Sync into a new enviroment, asserting the lockfile is up to date
WORKDIR /pima-api
RUN uv sync --locked


ENTRYPOINT ["uv", "run"]
