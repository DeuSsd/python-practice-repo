import unittest
from main import Student, Postgraduate

class MyTestCase(unittest.TestCase):
    def test_methods(self):
        s1_data = ("Огнев Денис Андреевич", 22)
        s1 = Student(*s1_data)
        self.assertEqual(s1.get_info(),s1_data)
        s1.set_average_mark(5)
        self.assertEqual(s1.get_stipend(), s1.STUDENT_STIPEND_5)

        s2_data = ("Петрович Илья Александрович", 25)
        s2 = Postgraduate(*s2_data)
        self.assertEqual(s2.get_info(), s2_data)
        s2.set_average_mark(5)
        self.assertEqual(s2.get_stipend(), s2.STUDENT_STIPEND_5)

        s3_data = ("Плотников Андрей Васильевич", 17)
        s3 = Student(*s3_data)
        self.assertEqual(s3.get_info(), s3_data)
        s3.set_average_mark(3)
        self.assertEqual(s3.get_stipend(), s3.STUDENT_STIPEND_3)

        self.assertFalse(s3.stipend_gt(s2))
        self.assertFalse(s2.stipend_eq(s1))
        self.assertFalse(s1.stipend_lt(s3))

if __name__ == '__main__':
    unittest.main()