"""
Создать иерархию классов фигур: квадрат, прямоугольник,треугольник, круг.
Каждый класс должен реализовывать следующие методы:
вычисление площади
вычисление периметра
сравнение площади с другой фигурой (больше или меньше)
сравнение периметра с другой фигурой (больше или меньше)

"""
import math


class Figure:
    def __init__(self):
        self.s = 0.
        self.p = 0.

    def square_lt(self, other):
        return self.s < other.s

    def perimeter_lt(self, other):
        return self.p < other.p


class Rectangle(Figure):
    def __init__(self, w: float, h: float):
        super().__init__()
        assert w > 0 and h > 0, "Values expect be positive"
        self.w = w
        self.h = h
        self.p = 2 * (w + h)
        self.s = w * h


class Square(Rectangle):
    def __init__(self, a: float):
        super().__init__(a, a)


class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        super().__init__()
        assert a > 0 and b > 0 and c > 0, "Values expect be positive"
        assert a < b + c and b < a + c and c < a + b, "Wrong sides of a triangle"
        self.a = a
        self.b = b
        self.c = c
        self.p = a + b + c
        half_p = self.p/2
        self.s = math.sqrt(half_p * (half_p- self.a) * (half_p - self.b) * (half_p - self.c))


class Circle(Figure):
    def __init__(self, r: float):
        super().__init__()
        assert r > 0, "Value expect be positive"
        self.r = r
        self.p = 2 * self.r * math.pi
        self.s = math.pi * (self.r ** 2)
