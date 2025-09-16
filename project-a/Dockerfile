ARG REGISTRY="docker.io"

FROM ${REGISTRY}/python:3.10-slim-bookworm

RUN mkdir /app
WORKDIR /app/

# install pipenv packages
RUN pip install pipenv==2024.2.0

# Copy shared packages first
COPY shared-packages/ /app/shared-packages/

# Copy project-a files
COPY project-a/Pipfile /app/project-a/Pipfile
COPY project-a/Pipfile.lock /app/project-a/Pipfile.lock

WORKDIR /app/project-a/

RUN  apt-get update \
  && apt-get install -y g++ curl libpq-dev libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0 libpangocairo-1.0-0 \
  && rm -rf /var/lib/apt/lists/*

# Install shared packages in development mode
RUN cd /app/shared-packages/common-utils && pip install -e .
RUN cd /app/shared-packages/data-models && pip install -e .

# Install project dependencies
RUN pipenv install --system --deploy --dev

# Copy the rest of project-a files
COPY project-a/ /app/project-a/

WORKDIR /app/project-a/
