from abc import ABC
from homework_02.exceptions import CargoOverload, LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    """ Класс, описывающий транспортное средство. """
    started = False

    def __init__(self, weight: float, fuel: float, fuel_consumption: float):
        """ Конструктор. """
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError()

    def move(self, distance: float):
        fuel_required = distance * self.fuel_consumption

        if fuel_required <= self.fuel:
            self.fuel -= fuel_required
        else:
            raise NotEnoughFuel()


