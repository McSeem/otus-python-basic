from models.models import *


def create_database():
    Base.metadata.create_all()
