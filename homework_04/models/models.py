"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)

from datetime import datetime
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):
    """ Класс описывает модель пользователя. """
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True)
    name = Column(String(30), unique=False)
    email = Column(String(30), unique=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    posts = relationship("Post")


class Post(Base):
    """ Класс описывает модель поста пользователя. """
    __tablename__ = "posts"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=False)
    title = Column(String(150), unique=False)
    body = Column(String(300), unique=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    user = relationship("User", back_populates="posts")
