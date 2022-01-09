"""
Домашнее задание №1
Функции и структуры данных
"""

"""
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
def power_numbers(*numbers):
    return [num ** 2 for num in list(numbers)]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    counter = 0
    for i in range(2, number):
        if number % i == 0:
            counter += 1
    return counter == 0

"""
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

def filter_numbers(numbers, num_type):
    if num_type == "odd":
        return list(filter(lambda num: num % 2 != 0, numbers))
    elif num_type == "even":
        return list(filter(lambda num: num % 2 == 0, numbers))
    else:
        return list(filter(is_prime, numbers))


