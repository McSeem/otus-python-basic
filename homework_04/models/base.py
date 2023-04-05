from sqlalchemy import Column, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import (
    declarative_base,
    declared_attr,
    sessionmaker,
    scoped_session,
)

import config


class Base:
    def __tablename__(cls):
        return f"blog_{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


engine = create_engine(url=config.SQLALCHEMY_PG_CONN_URI, echo=config.DB_ECHO)

Base = declarative_base(cls=Base, bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
