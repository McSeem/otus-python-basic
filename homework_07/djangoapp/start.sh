#!/bin/bash

# Запуск сервера обработки запросов
echo "Запуск django..."
python manage.py runserver 0.0.0.0:8000
echo "   ... сервер запущен"