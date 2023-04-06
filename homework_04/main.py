"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

import config
import asyncio
import jsonplaceholder_requests

# from models import Base, Session
from models.models import *


async def async_main():
    users_data: []
    posts_data: []

    # Загрузка пользователей и постов
    users_data, posts_data = await asyncio.gather(
        jsonplaceholder_requests.fetch_users_data(jsonplaceholder_requests.USERS_DATA_URL),
        jsonplaceholder_requests.fetch_posts_data(jsonplaceholder_requests.POSTS_DATA_URL),
    )


def create_database():
    Base.metadata.create_all()


def main():
    create_database()


if __name__ == "__main__":
    main()
    asyncio.run(async_main())
