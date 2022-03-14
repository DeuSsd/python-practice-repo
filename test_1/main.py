# Написать функцию, которая проверяет является ли строка палиндромом.
import re

def is_palindrome(line: str)-> bool:
    line = re.sub(r'[\d\W]', "", line).lower()
    return line == line[::-1]
