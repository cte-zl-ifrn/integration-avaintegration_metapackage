ARG PYTHON_VERSION=3.14.2-slim-trixie
ARG PACKAGE_NAME=avaintegration_metapackage
ARG PACKAGE_VERSION

FROM python:${PYTHON_VERSION} AS build

ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir "${PACKAGE_NAME}==${PACKAGE_VERSION}"

CMD ["python", "-c", "import django; print(django.get_version())"]
