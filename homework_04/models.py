"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, relationship, declared_attr, declarative_base

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"
print(PG_CONN_URI)

class Base:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    """def __repr__(self):
        return str(self)"""


engine = create_async_engine(PG_CONN_URI)
Base = declarative_base(bind=engine, cls=Base)

Session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


class User(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    username = Column(String(32), unique=True, nullable=False)
    email = Column(String(32), unique=True, nullable=False)

    posts = relationship("Post", back_populates="user")


class Post(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)

    user = relationship("User", back_populates="posts")
