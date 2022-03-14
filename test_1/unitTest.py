import unittest
from main import is_palindrome

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
            self.assertTrue(is_palindrome(line))

        for line in not_palindrome_list:
            self.assertFalse(is_palindrome(line))


if __name__ == '__main__':
    unittest.main()
