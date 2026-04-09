#########################
# Args
########################################################################
ARG PYTHON_VERSION=3.14.4-slim-trixie
ARG PACKAGE_NAME=avaintegration_metapackage
ARG PACKAGE_VERSION

#########################
# Base stage
########################################################################
FROM python:$PYTHON_VERSION AS base

ENV PYTHONUNBUFFERED=1

RUN    pip install "${PACKAGE_NAME}==${PACKAGE_VERSION}" \
    && useradd -ms /usr/sbin/nologin app
