#########################
# Args
########################################################################
ARG PYTHON_VERSION=3.14.4-slim-trixie

#########################
# Base stage
########################################################################
FROM python:$PYTHON_VERSION AS base

ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1
ARG PACKAGE_VERSION

RUN pip install --upgrade uv pip \
    && uv pip install --system "avaintegration_metapackage==${PACKAGE_VERSION}" \
    && useradd -ms /usr/sbin/nologin app
