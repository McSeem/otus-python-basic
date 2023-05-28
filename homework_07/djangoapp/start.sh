#!/bin/bash

echo "Запуск миграций..."
python manage.py migrate

# Запуск сервера обработки запросов
echo "Запуск django..."
python manage.py runserver 0.0.0.0:8000
echo "   ... сервер запущен"
