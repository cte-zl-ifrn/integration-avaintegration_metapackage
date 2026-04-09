#########################
# Args
########################################################################
ARG PYTHON_VERSION=3.14.4-slim-trixie
ARG PACKAGE_VERSION

#########################
# Base stage
########################################################################
FROM python:$PYTHON_VERSION AS base

ENV PYTHONUNBUFFERED=1

RUN    pip install "avaintegration_metapackage==6.0.4.3" \
    && useradd -ms /usr/sbin/nologin app
