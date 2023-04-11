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

Для включения работы с БД SQLite установите переменную конфига (файл config.py) создайте
следующие переменные:
SQLALCHEMY_SQLITE_CONN_URI = "sqlite:///db/blog.db"
DB_TYPE = 0

"""

import crud

import asyncio
import jsonplaceholder_requests

# from models import Base, Session
from models.models import *
from models.base import Session


async def async_main():
    users_data: []
    posts_data: []

    # Загрузка пользователей и постов
    users_data, posts_data = await asyncio.gather(
        jsonplaceholder_requests.fetch_users_data(jsonplaceholder_requests.USERS_DATA_URL),
        jsonplaceholder_requests.fetch_posts_data(jsonplaceholder_requests.POSTS_DATA_URL),
    )

    print(users_data)
    print(posts_data)

    #sys.exit()

    # Создание сессии работы с БД
    session = Session()

    # Подготовка списков данных пользователей и постов и добавдение их в сессию БД
    session.add_all(crud.load_users(users_data))
    session.add_all(crud.load_users_posts(posts_data))

    # Запись данных в БД
    session.commit()
    session.close()


def create_database():
    Base.metadata.create_all()


def main():
    pass
    create_database()


if __name__ == "__main__":
    main()
    asyncio.run(async_main())
