"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import json

import aiohttp
from urllib.request import urlopen

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url: str):
    response = urlopen(url)

    json_data = json.loads(response.read())

    return json_data


async def fetch_users_data(url: str):
    if not url:
        return

    users_data = await fetch_json(url)

    return users_data


async def fetch_posts_data(url: str):
    if not url:
        return

    posts_data = await fetch_json(url)

    return posts_data

