import random

from models.models import Post, User

from models.base import Session

""" Для заполнения созданных таблиц users и posts
    нужно добавлять в сессию сразу несколько записей пачками.
    
    Для работы с базовыми операциями CRUD работать с одной записью (объектом)
    в сессии.
"""


def load_users(users):
    session = Session()

    for user in users:
        user_record = User()

        user_record.username = user["username"]
        user_record.name = user["name"]
        user_record.email = user["email"]

        session.add(user_record)

    session.commit()
    session.close()


def load_users_posts(posts):
    session = Session()

    for post in posts:
        post_record = Post()

        post_record.user_id = random.randint(1, 10)
        post_record.title = post["title"]
        post_record.body = post["body"]

        session.add(post_record)

    session.commit()
    session.close()
