"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    """ Исключение для случая нехватки топлива для запуска двигателя. """
    pass


class NotEnoughFuel(Exception):
    """ Исключение для случая нехватки топлива для преодоления пути. """
    pass


class CargoOverload(Exception):
    """ Исключение для случая перегрузки летательного аппарата. """
    pass
