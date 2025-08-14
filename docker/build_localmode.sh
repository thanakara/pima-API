#!/bin/bash


# Restore .csv file from remote storage:
pip uninstall pyopenssl
dvc pull

# Run the build:
docker build --file docker/Dockerfile --tag pimaim ./

# # Run the image in detached mode:
# docker run --name pimaco -d --rm -p 8080:80 pimaim

# Visit localhost:8080
curl localhost:8080/docs

# # Stop container - Remove image:
# docker stop pimaco
# docker rmi pimaim