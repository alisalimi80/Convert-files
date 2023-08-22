FROM python:3.10

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .
RUN pip install --upgrade pip
RUN apt-get update &&\
    apt-get install -y build-essential libpq-dev ncat netcat-traditional
RUN pip install --upgrade -r requirements.txt