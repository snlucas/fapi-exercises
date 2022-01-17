FROM python3.9:slim-buster

WORKDIR /app

RUN pip install -U pip \
    -r requirements.txt