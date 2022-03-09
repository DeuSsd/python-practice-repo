# Написать функцию, которая проверяет является ли строка палиндромом.
import re

def check_palindeom(line: str)-> bool:
    line = re.sub(r'[\d\W]', "", line).lower()
    return line == line[::-1]

if __name__ == '__main__':
    test = [
        "Text",
        "Нажал? кабан на баклажан"

    ]
    for num, line in enumerate(test):
        print(num, f" - {check_palindeom(line)}", line)