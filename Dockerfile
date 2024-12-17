# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

RUN apt-get update
#RUN apt-get install ffmpeg libsm6 libxext6 curl wget python-pip python-dev build-essential -y

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "gunicorn", "wsgi:app", "-b", "0.0.0.0:8001", "--access-logfile=-"]