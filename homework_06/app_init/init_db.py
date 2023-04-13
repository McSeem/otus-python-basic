from models.base import Base


def create_database():
    Base.metadata.create_all()
