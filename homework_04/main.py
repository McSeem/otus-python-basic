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

Для включения работы с БД SQLite проверьте наличие переменной конфига (файл config.py)
SQLALCHEMY_SQLITE_CONN_URI = "sqlite:///db/blog.db",
а также
DB_TYPE = 0,
либо
DB_TYPE = 1 для работы с БД Postgres
"""


import crud

import asyncio
import jsonplaceholder_requests

from models.models import Base
from models.base import engine, Session


async def async_main():
    users_data: []
    posts_data: []

    # Загрузка пользователей и постов
    users_data, posts_data = await asyncio.gather(
        jsonplaceholder_requests.fetch_users_data(jsonplaceholder_requests.USERS_DATA_URL),
        jsonplaceholder_requests.fetch_posts_data(jsonplaceholder_requests.POSTS_DATA_URL),
    )

    await create_database()

    # Создание сессии работы с БД
    session = Session()

    try:
        # Подготовка списков данных пользователей и постов и добавдение их в сессию БД
        async with session as users_session:
            async with users_session.begin():
                session.add_all(crud.load_users(users_data))

        async with session as posts_session:
            async with posts_session.begin():
                session.add_all(crud.load_users_posts(posts_data))

    except Exception:
        session.rollback()

        print("Не удалось добавить загруженные данные в БД")

        raise
    else:
        print("Данные успешно добавлены")


async def create_database():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
