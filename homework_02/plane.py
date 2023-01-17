from .base import Vehicle
from .exceptions import CargoOverload

"""
создайте класс `Plane`, наследник `Vehicle`
"""

class Plane(Vehicle):
    cargo: float = 10.5
    max_cargo: float

    def __init__(self, max_cargo: float):
        self.max_cargo = max_cargo

    def load_cargo(self, add_cargo: float):
        total_cargo = self.cargo + add_cargo

        if total_cargo <= self.max_cargo:
            self.cargo = total_cargo
        else:
            raise CargoOverload
