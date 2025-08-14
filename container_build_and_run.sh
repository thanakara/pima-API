#!/bin/bash


# Restore .csv file from remote storage:
! dvc pull

# Run the build:
! docker build --tag pima ./
! docker run --rm -p 8080:80 pima

# Visit localhost:8080

# Remove image:
# ! docker rmi pima