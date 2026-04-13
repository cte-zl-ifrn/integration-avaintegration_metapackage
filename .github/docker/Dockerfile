#########################
# Args
########################################################################
ARG PYTHON_VERSION=3.14.4-slim-trixie

#########################
# Base stage
########################################################################
FROM python:$PYTHON_VERSION AS base

ENV PYTHONUNBUFFERED=1

RUN    pip install --upgrade "avaintegration_metapackage==6.0.4.11" uv pip \
    && useradd -ms /usr/sbin/nologin app
