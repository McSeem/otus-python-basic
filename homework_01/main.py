"""
Домашнее задание №1
Функции и структуры данных
"""

DEGREE = 2


def square(item) -> int:
    """ Функция возведения в квадрат. """
    return item ** DEGREE


def power_numbers(*numbers) -> list:
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел.
    """
    return list(map(square, numbers))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers():
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    #>>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    #>>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """


print(power_numbers(1, 2, 5, 7, 9))
