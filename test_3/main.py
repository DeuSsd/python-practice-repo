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

        self._s = 0.
        self._p = 0.

    def __square(self):
        pass

    def __perimetr(self):
        pass

    def get_parameters(self):
        pass

    def get_square(self):
        self.__square()
        return self._s

    def get_perimeter(self):
        self.__perimetr()
        return self._p

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
        return (self._w,self._h)

    def __square(self):
        self.s = self._w * self._h

    def __perimetr(self):
        self._p = 2 * (self._w + self._h)


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
        return (self._a,self._b,self._c)

    def __square(self):
        self.__perimetr()
        half_p = self._p/2
        self._s = math.sqrt(half_p * (half_p- self._a) * (half_p - self._b) * (half_p - self._c))

    def __perimetr(self):
        self._p = self._a + self._b + self._c

class Circle(Figure):
    def __init__(self, r: float):
        super().__init__()
        assert r > 0, "Value expect be positive"
        self._r = r

    def get_parameters(self):
        return (self._r)

    def __square(self):
        self.s = math.pi * (self._r ** 2)

    def __perimetr(self):
        self.p = 2 * self._r * math.pi