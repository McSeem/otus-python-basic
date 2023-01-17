from  dataclasses import dataclass
"""
create dataclass `Engine`
"""


@dataclass
class Engine:
    """ Класс описывает двигатель и его базовые характеристики. """
    volume: float
    pistons: int


