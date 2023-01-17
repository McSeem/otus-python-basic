from abc import ABC
from homework_02.exceptions import CargoOverload, LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    """ Класс, описывающий транспортное средство. """
    started = False

    FUEL_EMPTY = 0

    def __init__(self, weight: float, fuel: float, fuel_consumption: float) -> None:
        """ Конструктор. """
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self) -> None | LowFuelError:
        """ Метод определяет уровень топлива. """
        if not self.started:
            if self.fuel > self.FUEL_EMPTY:
                self.started = True
            else:
                raise LowFuelError()

    def move(self, distance: float) -> None | LowFuelError:
        """ Метод проверяет запас топлива для преодоления пути. """
        fuel_required = distance * self.fuel_consumption

        if fuel_required <= self.fuel:
            self.fuel -= fuel_required
        else:
            raise NotEnoughFuel()


