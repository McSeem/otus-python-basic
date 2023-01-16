from abc import ABC


class Vehicle(ABC):
    """ Класс, описывающий транспортное средство. """
    started = False

    def __init__(self, weight: float, fuel: float, fuel_consumption: float):
        """ Конструктор. """
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
