import asyncio
import jsonplaceholder_requests

from app_init import init_db
from models import crud
from models.base import Session


async def pull_data():
    users_data: []
    posts_data: []

    # Загрузка пользователей и постов
    users_data, posts_data = await asyncio.gather(
        jsonplaceholder_requests.fetch_users_data(jsonplaceholder_requests.USERS_DATA_URL),
        jsonplaceholder_requests.fetch_posts_data(jsonplaceholder_requests.POSTS_DATA_URL),
    )

    # Создание сессии работы с БД
    session = Session()

    session.begin()

    try:
        # Подготовка списков данных пользователей и постов и добавдение их в сессию БД
        print("   ... заполнение таблиц")

        session.add_all(crud.load_users(users_data))
        session.add_all(crud.load_users_posts(posts_data))
    except Exception:
        session.rollback()

        print("   ... не удалось добавить загруженные данные в БД")

        raise
    else:
        # Запись данных в БД
        session.commit()
        session.close()

        print("   ... данные успешно добавлены")

# Создание БД
init_db.create_database()

# Заполнение таблиц данными
asyncio.run(pull_data())
