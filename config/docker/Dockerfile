# Backend setup
FROM python:3.12 AS development

# Unbuffer Python logs
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.8.3

RUN pip install poetry==$POETRY_VERSION

WORKDIR /usr/src/app
COPY poetry.lock pyproject.toml /usr/src/app/

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

FROM development AS production
WORKDIR /usr/src/app
COPY . /usr/src/app/

CMD [ "gunicorn", "backend.wsgi", "--log-file -" ]