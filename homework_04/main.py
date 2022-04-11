"""
Домашнее задание №3
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
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from homework_04.models import Base, engine, Session
from homework_04.jsonplaceholder_requests import fetch_user, fetch_post


async def create_tables():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)


async def create_user(session: AsyncSession, id: int):
    user = await fetch_user(id)
    session.add(user)


async def create_post(session: AsyncSession, post_id: int):
    post = await fetch_post(post_id)
    # statement = select(User).where(User.id == post.user_id)
    # result: Result = await session.execute(statement)
    # user: User = result.scalar_one()
    session.add(post)


async def create_users(session: AsyncSession):
    for i in range(1, 11):
        await create_user(session, i)



async def create_posts(session: AsyncSession):
    for i in range(1, 101):
        await create_post(session, i)



async def async_main():
    await create_tables()
    async with Session() as session:
        await asyncio.gather(create_users(session), create_posts(session))
        await session.commit()




def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_main())
    """asyncio.run(async_main())"""


if __name__ == "__main__":
    main()
