import unittest
from main import Rectangle,Triangle,Square,Circle
import math

class MyTestCase(unittest.TestCase):
    def test_figure(self):
    # def test_Rectangle(self):
        r1 = Rectangle(2,3)
        self.assertEqual(r1.p, 10.)
        self.assertEqual(r1.s, 6.)

        r2 = Rectangle(4.5, 3.)
        self.assertEqual(r2.p, 15)
        self.assertEqual(r2.s, 13.5)

        self.assertFalse(r2.square_lt(r1))
        self.assertFalse(r2.perimeter_lt(r1))


    # def test_Square(self):
        s1 = Square(2)
        self.assertEqual(s1.p, 8)
        self.assertEqual(s1.s, 4)

        s2 = Square(5.)
        self.assertEqual(s2.p, 20)
        self.assertEqual(s2.s, 25)

        self.assertTrue(s1.square_lt(s2))
        self.assertTrue(s1.perimeter_lt(s2))

    # def test_Triangle(self):
        t1 = Triangle(1,3,3)
        self.assertEqual(t1.p, 7)
        self.assertEqual(t1.s, math.sqrt(35)/4) # 1.47

        t2 = Triangle(3,4,5)
        self.assertEqual(t2.p, 12)
        self.assertEqual(t2.s, 6)

        self.assertTrue(t1.square_lt(t2))
        self.assertTrue(t1.perimeter_lt(t2))

    # def test_Circle(self):
        c1 = Circle(4)
        self.assertEqual(c1.p, 2 * 4 * math.pi)
        self.assertEqual(c1.s, math.pi * (4 ** 2))

        c2 = Circle(1.44)
        self.assertEqual(c2.p, 2 * 1.44 * math.pi)
        self.assertEqual(c2.s, math.pi * (1.44 ** 2))

        self.assertTrue(c2.square_lt(c1))
        self.assertFalse(c1.perimeter_lt(c2))


if __name__ == '__main__':
    unittest.main()
