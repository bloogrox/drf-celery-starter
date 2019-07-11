FROM python:3

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /app

COPY ./src .

EXPOSE 8000
