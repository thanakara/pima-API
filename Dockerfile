# The main build stage - Uses Miniconda3 image
FROM continuumio/miniconda3 AS base

# Auto-accept required TOS during build:
ENV CONDA_PLUGINS_AUTO_ACCEPT_TOS=true

# Create environment and install uv
# Note that we don't activate the enviroment; instead use:
# conda run -n <evn> <command> to run a command inside a specific env
RUN conda create -y --name pima-api python=3.10.18 && \
    conda run --name pima-api pip install poetry

# Add the project code using .dockerignore:
ADD . /pima-API
WORKDIR /pima-API

# Install dependencies from .toml file:
RUN conda run --name pima-api poetry install

# Remove pyopenssl dependency for DVC - Google Drive Storage
# RUN conda run --name pima-api pip uninstall pyopenssl -y

# Train-Job produces a classification report and a serialized model:
RUN conda run --name pima-api \
    poetry run python pima_api/model/hydrajob_localmode.py

# Run the FastAPI app using fastapi CLI:
ENTRYPOINT ["conda", "run", "--name", "pima-api", "poetry", "run"]

# Declare which port the container will listen on at runtime:
EXPOSE 80

CMD ["fastapi", "run", "pima_api/fastapi_pima.py", "--host", "0.0.0.0", "--port", "80"]

