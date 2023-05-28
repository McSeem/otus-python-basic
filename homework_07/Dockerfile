# 1. Перейдите в каталог с данным Dockerfile
# 2. Соберите Docker-образ с инфраструктурой приложения:
#    docker-compose build --build-arg UID=$(id -u) --build-arg GID=$(id -g) --no-cache
# 3. Запустите образ:
#    docker-compose up
# 4. Запуск миграций:
#    Во время запуска образа должен быть вывод log-сообщений о миграциях
#    . . .
#    Создание миграций приложения lmsbaikal
#    | Migrations for 'lmsbaikal':
#    |   lmsbaikal/migrations/0001_initial.py
#    |     - Create model Question
#    |     - Create model QuestionAnswers
#    | Запуск миграций приложения lmsbaikal...
#    | Operations to perform:
#    |   Apply all migrations: admin, auth, contenttypes, lmsbaikal, sessions
#    | Running migrations:
#    |   Applying lmsbaikal.0001_initial... OK
#    . . .
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
