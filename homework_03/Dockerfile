# 1. Перейдите в каталог с данным Dockerfile
# 2. Возможно потребуется установить пакеты (для тестов) - docker и faker:
#    pip install docker faker
# 3. Соберите контейнер с приложением:
#    docker build . -t homework_03
# 4. Запустите контейнер:
#    docker run -it -p 12345:8000 homework_03
# 5. Проверить работу приложения:
#    http://localhost:12345/docs

FROM python:3.10-buster

WORKDIR /var/app

RUN apt-get update && \
    apt-get install -y mc

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
