ARG REGISTRY="docker.io"
ARG HOME_DIR=/code
# ARG APP_HOME_DIR=/code/apps/project-a

FROM ${REGISTRY}/python:3.12-slim-bookworm

RUN mkdir /code
RUN mkdir /code/apps
WORKDIR /code/

# install pipenv packages
RUN pip install pipenv==2025.0.4

# Copy shared packages first
COPY packages/ /code/packages/

# Copy project-a files
COPY apps/project-a/Pipfile /code/apps/project-a/Pipfile
COPY apps/project-a/Pipfile.lock /code/apps/project-a/Pipfile.lock

WORKDIR /code/apps/project-a/

RUN  apt-get update \
  && apt-get install -y g++ curl libpq-dev libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0 libpangocairo-1.0-0 \
  && rm -rf /var/lib/apt/lists/*

# Install shared packages in development mode
RUN cd /code/packages/common-utils && pip install -e .
RUN cd /code/packages/data-models && pip install -e .

# Install project dependencies
RUN pipenv install --system --deploy --dev

# Copy the rest of project-a files
COPY apps/project-a/ /code/apps/project-a/

WORKDIR /code/apps/project-a/
