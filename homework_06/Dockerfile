# 1. Перейдите в каталог с данным Dockerfile
# 2. Возможно потребуется установить пакеты (для тестов) - docker и faker:
#    pip install docker faker
# 3. Соберите контейнер с приложением:
#    docker build . -t homework_05
# 4. Запустите контейнер:
#    docker run -it -p 8000:5000 homework_05
# 5. Проверить работу приложения:
#    http://localhost:8000

FROM python:3.10-buster

ARG GID=1000
ARG UID=1000

RUN groupadd -g $GID www && \
    useradd -l -u $UID -ms /bin/bash -g www www

WORKDIR /var/app

RUN apt-get update && \
    apt-get install -y \
    mc \
    nano

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD gunicorn --bind 0.0.0.0:5000 wsgi:app

USER www
