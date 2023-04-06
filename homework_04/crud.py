from models.models import Post, User

from models.base import Session

""" Для заполнения созданных таблиц users и posts
    нужно добавлять в сессию сразу несколько записей пачками.
    
    Для работы с базовыми операциями CRUD работать с одной записью (объектом)
    в сессии.
"""