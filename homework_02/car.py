from .base import Vehicle
from .engine import Engine

"""
создайте класс `Car`, наследник `Vehicle`
"""


class Car(Vehicle):
    """ Класс описывает автомобиль. """
    engine = "Diesel"

    def set_engine(self, engine: Engine) -> None:
        """ Метод устанавливает двигатель для автомобиля. """
        self.engine = engine
