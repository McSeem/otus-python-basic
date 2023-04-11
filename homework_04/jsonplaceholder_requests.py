"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import json

import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"
RESPONSE_STATUS_OK = 200


async def fetch_json(url: str) -> str:
    """ Функция получает данные по переданному URL в асинхронном режиме. """

    session = aiohttp.ClientSession()

    async with session.get(url) as response:
        if response.status != RESPONSE_STATUS_OK:
            response.raise_for_status()

        result = await response.text()
    await session.close()

    return result


async def fetch_users_data(url: str) -> json:
    """ Функция извлекает данные пользователей по переданному URL. """
    if not url:
        return

    users_data = await fetch_json(url)

    return json.loads(users_data)


async def fetch_posts_data(url: str) -> json:
    """ Функция извлекает данные пользовательских постов по переданному URL. """
    if not url:
        return

    posts_data = await fetch_json(url)

    return json.loads(posts_data)

