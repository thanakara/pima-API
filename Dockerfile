
# Pull a prebuilt image that contains uv and uvx binaries.
# No need to install uv from source --just grab the compiled binaries:
FROM ghcr.io/astral-sh/uv:latest AS uv-bin


# The main build stage - Uses Miniconda3 image
FROM continuumio/miniconda3 AS build


# Auto-accept required TOS during build:
ENV CONDA_PLUGINS_AUTO_ACCEPT_TOS=true


# Create environment and install uv
# Note that we don't activate the enviroment; instead use:
# conda run -n <evn> <command> to run a command inside a specific env,
# -c conda-forge since uv is from Conda Forge channel - not defaults
RUN conda create -y --name pima-api python=3.10.18 && \
    conda run --name pima-api conda install -y conda-forge::uv


# Copy uv and uvx binaries from previous stage
# This makes multi-stage build powerfull:
# get prebuilt stuff from one image; drop it into another:
COPY --from=uv-bin /uv /bin/uv
COPY --from=uv-bin /uvx /bin/uvx


# Add the project code using .dockerignore:
ADD . /pima-API
WORKDIR /pima-API


# Sync using uv within conda env
RUN conda run --name pima-api uv sync --locked


# Build the model.joblib @--entrypoint + --cmd:
ENTRYPOINT ["conda", "run", "--name", "pima-api"]


CMD ["uv", "run", "pima_api/model/produce.py"]



