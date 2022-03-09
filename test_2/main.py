"""
Написать функцию, которая принимает два аргумента: лямбда функция для фильтрации массива, массив строк.
Сделать вызов данной функции для следующих функций фильтрации:

- Исключить строки с пробелами
- Исключить строки, начинающиеся с буквы “a”
- Исключить строки, длина которых меньше 5

"""

from collections.abc import Callable
from typing import List


def filter(filter: Callable[str, bool], list_for_filtering: List[str]) -> List[str]:
    for string in list_for_filtering.copy():
        if filter(string):
            list_for_filtering.remove(string)
    return list_for_filtering

filter_list = [
    lambda line: line.find(" ") != -1,
    lambda line: line.startswith("a"),
    lambda line: len(line) < 5
]
