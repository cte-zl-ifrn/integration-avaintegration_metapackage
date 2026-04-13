#########################
# Args
########################################################################
ARG PYTHON_VERSION=3.14.4-slim-trixie
ARG PACKAGE_VERSION
ENV PACKAGE_VERSION=${PACKAGE_VERSION:-unknown}

#########################
# Base stage
########################################################################
FROM python:$PYTHON_VERSION AS base

ENV PYTHONUNBUFFERED=1

RUN    pip install --upgrade "avaintegration_metapackage==6.0.4.${PACKAGE_VERSION}" uv pip \
    && useradd -ms /usr/sbin/nologin app
