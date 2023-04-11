import random
from typing import List

from models.models import Post, User

from models.base import Session

""" Для заполнения созданных таблиц users и posts
    нужно добавлять в сессию сразу несколько записей пачками.
    
    Для работы с базовыми операциями CRUD работать с одной записью (объектом)
    в сессии.
"""


def load_users(users: List) -> List:
    users_records = []

    for user in users:
        user_record = User()

        user_record.username = user["username"]
        user_record.name = user["name"]
        user_record.email = user["email"]

        users_records.append(user_record)

    return users_records


def load_users_posts(posts: List) -> List:
    posts_records = []

    for post in posts:
        post_record = Post()

        post_record.user_id = post["userId"]
        post_record.title = post["title"]
        post_record.body = post["body"]

        posts_records.append(post_record)

    return posts_records
