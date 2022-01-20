FROM python:3.8-slim-buster

WORKDIR /app

COPY app/ /app/
COPY requirements.txt /app/

RUN pip install -U pip \
    -r requirements.txt
