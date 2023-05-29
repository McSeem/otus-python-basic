# 1. Перейдите в каталог с данным Dockerfile
# 2. Создайте файл .env:
#    cp .env_example .env
# 3. Соберите Docker-образ с инфраструктурой приложения:
#    docker-compose build --build-arg UID=$(id -u) --build-arg GID=$(id -g) --no-cache
# 4. Запустите образ:
#    docker-compose up
# 5. Приложение доступно:
#    http://localhost:8000/lmsbaikal/

FROM python:3.10-buster

ARG GID=1000
ARG UID=1000

# Добавление группы и пользователя с такимиже идентификаторами, как и в хост-системе
RUN groupadd -g $GID www && \
    useradd -l -u $UID -ms /bin/bash -g www www

# Определение рабочей директории проекта внутри контейнера приложения
WORKDIR /var/app

# Установка необходимого ПО (файловый менеджер mc, текстовый редактор nano)
RUN apt-get update && \
    apt-get install -y \
    mc \
    nano \
    htop

# Копирование файлов проекта из хост-системы в рабочий каталог '/var/app' внутри контейнера
COPY . .

# Установка Python-зависимостей проекта
RUN pip install -r requirements.txt

# Открытие внешнего порта для отправки запросов и подключений из хост-системы
EXPOSE 8000

# Запуск скрипта инициализации БД и начальной настройки инфраструктуры системы
CMD ["/bin/bash", "start.sh"]

# Определение пользователя, от которого будут выполняться команды
USER www
