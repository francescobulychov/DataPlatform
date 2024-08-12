FROM python:3.12-slim

WORKDIR /app
COPY ./data-generator/requirements.txt /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt