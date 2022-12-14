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

NEXT_NUMBER = 1
DEEGRE_ORDER = 2
BASE_DIVIDER = 2
ZERO = 0


def is_prime(number) -> bool:
    """ Функция определяет, является ли число простым. """
    for item in range(BASE_DIVIDER, (number//DEEGRE_ORDER) + NEXT_NUMBER):
        if number % item == ZERO:
            return False
    return True


def is_even(number) -> bool:
    """ Функция определяет, является ли число чётным. """
    result = number % BASE_DIVIDER
    return result == ZERO


def is_odd(number) -> bool:
    """ Функция определяет, является ли число нечётным. """
    result = number % BASE_DIVIDER
    return result != ZERO


def filter_numbers(numbers, filter_type) -> list:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    """
    if filter_type == EVEN:
        result = filter(is_even, numbers)

    if filter_type == ODD:
        result = filter(is_odd, numbers)

    if filter_type == PRIME:
        result = filter(is_prime, numbers)

    return list(result)


filtered = filter_numbers([1, 2, 3, 6, 9], PRIME)
print(filtered)
