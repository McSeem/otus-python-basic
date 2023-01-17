from .base import Vehicle
from .exceptions import CargoOverload

"""
создайте класс `Plane`, наследник `Vehicle`
"""

class Plane(Vehicle):
    cargo: float = 0
    max_cargo: float

    CARGO_EMPTY = 0

    def __init__(self, weight: float, fuel: float, fuel_consumption: float, max_cargo: float):
        """ Конструктор. """
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.max_cargo = max_cargo

    def load_cargo(self, add_cargo: float) -> None | CargoOverload:
        """ Метод загружает летательный аппарат грузом, проверяя максимальную грузоподъёмность аппарата. """
        total_cargo = self.cargo + add_cargo

        if total_cargo <= self.max_cargo:
            self.cargo = total_cargo
        else:
            raise CargoOverload()

    def remove_all_cargo(self) -> float:
        """ Метод полностью разгружает летательный аппарат, предоставляя информацию о массе груза. """
        stored_cargo = self.cargo
        self.cargo = self.CARGO_EMPTY

        return stored_cargo