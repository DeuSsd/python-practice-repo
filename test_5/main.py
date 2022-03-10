"""
Реализовать декоратор, который выводит в консоль время выполнения декорируемой функции.
Протестировать работу декоратора на двух функциях:

Функция вычисляет сумму двух чисел a и b, выводит результат в консоль

Функция читает из файла input.txt значение двух чисел a и b,
записывает результат вычисления в файл output.txt (файлы приложить к репозиторию)
"""

from tools import count_time, delay_finish



@count_time
@delay_finish()
def sum(a: float, b: float) -> float:
    return a + b


@count_time
@delay_finish(time_sleep=4)
def rewrite(file_input: str, file_output: str):
    try:
        sum = 0
        with open(file_input, "r") as input_f:
            a = float(input_f.readline())
            b = float(input_f.readline())
            sum = a + b
        with open(file_output, "w") as output_f:
            output_f.write(str(sum))
        return sum
    except (FileExistsError, FileNotFoundError) as e:
        print(e)
    except TypeError as e:
        print(e)


if __name__ == '__main__':
    print(rewrite("input.txt", "output.txt"))
    print(sum(2, 4))
