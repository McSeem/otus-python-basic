FROM python:3.10-buster

WORKDIR /var/app

RUN apt-get update && \
    apt-get install -y mc

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80
