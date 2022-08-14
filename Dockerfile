FROM python:3.10.6-slim-buster

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y libpq-dev

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /website

COPY Pipfile Pipfile.lock /website/

RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /website/