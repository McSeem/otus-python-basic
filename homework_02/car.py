from .base import Vehicle
from .engine import Engine

"""
создайте класс `Car`, наследник `Vehicle`
"""


class Car(Vehicle):
    engine = "Diesel"

    def set_engine(self, engine: Engine):
        self.engine = engine
