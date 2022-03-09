"""
Написать функцию, которая принимает два аргумента: лямбда функция для фильтрации массива, массив строк.
Сделать вызов данной функции для следующих функций фильтрации:

- Исключить строки с пробелами
- Исключить строки, начинающиеся с буквы “a”
- Исключить строки, длина которых меньше 5

"""

from collections.abc import Callable
from typing import List


def func(filter: Callable[str, bool], list_for_filtering: List[str]) -> List[str]:
    for string in list_for_filtering.copy():
        if filter(string):
            list_for_filtering.remove(string)
    return list_for_filtering

filter_list = [
    lambda line: line.find(" ") != -1,
    lambda line: line.startswith("a"),
    lambda line: len(line) < 5
]

if __name__ == '__main__':
    test_line = [
        "Text",
        "Нажал кабан на баклажан",
        "Привет мир!",
        "аврора",
        "atmosphere"
    ]

    print(test_line)
    for num, filter in enumerate(filter_list):
        print(num, f" - {func(filter, test_line.copy())}")
