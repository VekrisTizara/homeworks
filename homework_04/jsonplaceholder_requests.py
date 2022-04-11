"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp
from homework_04.models import User, Post

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users/"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts/"


async def fetch_json(source):
    async with aiohttp.ClientSession() as session:
        async with session.get(source) as response:
            response_json = await response.json()
            return response_json


async def fetch_user(user_id: int):
    user = await fetch_json(f'{USERS_DATA_URL}{user_id}')
    return User(
        id=user.get('id'),
        name=user.get('name'),
        username=user.get('username'),
        email=user.get('email')
    )


async def fetch_post(post_id: int):
    post = await fetch_json(f'{POSTS_DATA_URL}{post_id}')
    return Post(
        id=post.get('id'),
        user_id=post.get('userId'),
        title=post.get('title'),
        body=post.get('body')
    )


"""user = loop.run_until_complete(fetch_user(7))
post = loop.run_until_complete(fetch_post(15))


print(user.__dict__)
print(post.__dict__)"""