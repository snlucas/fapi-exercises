FROM python3.9:slim-buster

WORKDIR /app

COPY app/ /app/
COPY requirements.txt /app/

RUN pip install -U pip \
    -r requirements.txt