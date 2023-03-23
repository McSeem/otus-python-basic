"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import asyncio
import json

import aiohttp
from urllib.request import urlopen

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url: str):
    response = urlopen(url)
    print(f"Отправлен запрос для получения пользователей...")

    json_data = json.loads(response.read())

    print(type(json_data))
    print(json_data)

    return json_data
