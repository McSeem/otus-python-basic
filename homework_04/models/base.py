from sqlalchemy import Column, Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    scoped_session,
)

import os
import config

PG_CONN_URI = os.environ.get(
    'SQLALCHEMY_PG_CONN_URI'
) or "postgresql+asyncpg://postgres:password@localhost:5432/postgres"


class Base:
    """ Класс описывает настройки подключения к БД. """
    DB_TYPE_SQLITE = 0

    def __tablename__(cls):
        return f"blog_{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


db_connection_url = config.SQLALCHEMY_PG_CONN_URI

if config.DB_TYPE == Base.DB_TYPE_SQLITE:
    db_connection_url = config.SQLALCHEMY_SQLITE_CONN_URI

engine = create_async_engine(url=PG_CONN_URI, echo=config.DB_ECHO)

Base = declarative_base(cls=Base, bind=engine)

session_factory = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Session = scoped_session(session_factory)
