#########################
# Args
########################################################################
ARG PYTHON_VERSION=3.14.4-slim-trixie
ARG AVAINTEGRATION_METAPACKAGE_VERSION

#########################
# Base stage
########################################################################
FROM python:$PYTHON_VERSION AS base

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade uv pip \
    && uv pip install --system "avaintegration_metapackage==${AVAINTEGRATION_METAPACKAGE_VERSION}" \
    && useradd -ms /usr/sbin/nologin app
