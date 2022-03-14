"""
Создать иерархию классов фигур: квадрат, прямоугольник,треугольник, круг.
Каждый класс должен реализовывать следующие методы:
вычисление площади
вычисление периметра
сравнение площади с другой фигурой (больше или меньше)
сравнение периметра с другой фигурой (больше или меньше)

"""
import math

from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self):
        self._s = 0.
        self._p = 0.

    @abstractmethod
    def get_square(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_parameters(self):
        pass

    def square_lt(self, other):
        return self._s < other._s

    def perimeter_lt(self, other):
        return self._p < other._p


class Rectangle(Figure):
    def __init__(self, w: float, h: float):
        super().__init__()
        assert w > 0 and h > 0, "Values expect be positive"
        self._w = w
        self._h = h

    def get_parameters(self):
        return self._w, self._h

    def get_square(self):
        self.s = self._w * self._h
        return self._s

    def get_perimeter(self):
        self._p = 2 * (self._w + self._h)
        return self._p

class Square(Rectangle):
    def __init__(self, a: float):
        super().__init__(a, a)


class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        super().__init__()
        assert a > 0 and b > 0 and c > 0, "Values expect be positive"
        assert a < b + c and b < a + c and c < a + b, "Wrong sides of a triangle"
        self._a = a
        self._b = b
        self._c = c

    def get_parameters(self):
        return self._a, self._b, self._c

    def get_square(self):
        half_p = self.get_perimeter() / 2
        self._s = math.sqrt(half_p * (half_p - self._a) * (half_p - self._b) * (half_p - self._c))
        return self._s

    def get_perimeter(self):
        self._p = self._a + self._b + self._c
        return self._p

class Circle(Figure):
    def __init__(self, r: float):
        super().__init__()
        assert r > 0, "Value expect be positive"
        self._r = r

    def get_parameters(self):
        return self._r

    def get_square(self):
        self.s = math.pi * (self._r ** 2)
        return self._s

    def get_perimeter(self):
        self.p = 2 * self._r * math.pi
        return self._p


if __name__ == '__main__':
    t1 = Triangle(2, 3, 4)
    print(t1.get_perimeter(),
          t1.get_square())
