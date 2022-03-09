import unittest
from main import check_palindeom

class MyTestCase(unittest.TestCase):
    def test_line_is_palindrome(self):
        palindrome_list = [
            "!Нажал кабан на баклажан",
            "А роза упала не на лапу Азора"
        ]

        not_palindrome_list = [
            "Text",
            "simple_2",
            "just a sentences"
        ]

        for line in palindrome_list:
            self.assertTrue(check_palindeom(line))

        for line in not_palindrome_list:
            self.assertFalse(check_palindeom(line))


if __name__ == '__main__':
    unittest.main()
