import unittest
from main import data_cleaning_via_filters_apart,data_cleaning_via_filters_together, filter_list


class MyTestCase(unittest.TestCase):
    def test_space(self):
        lambda_fun = [lambda line: line.find(" ") == -1]
        test_lines = [
            "Text",
            "Нажал кабан на баклажан",
            "Привет мир!",
            "аврора",
            "atmosphere"
        ]
        result_lines = [[
            "Text",
            "аврора",
            "atmosphere"
        ]]
        self.assertEqual(result_lines,data_cleaning_via_filters_apart(lambda_fun, test_lines))

    def test_string_startswith_a(self):
        lambda_fun = [lambda line: not line.startswith("a")]
        test_lines = [
            "Text",
            "Нажал кабан на баклажан",
            "Привет мир!",
            "аврора",
            "atmosphere"
        ]
        result_lines = [[
            "Text",
            "Нажал кабан на баклажан",
            "Привет мир!",
            "аврора",
        ]]
        self.assertEqual(data_cleaning_via_filters_apart(lambda_fun, test_lines), result_lines)

    def test_line_less_5(self):
        lambda_fun = [lambda line: len(line) > 5]
        test_lines = [
            "Text",
            "Нажал кабан на баклажан",
            "Привет мир!",
            "аврора",
            "atmosphere"
        ]
        result_lines = [[
            "Нажал кабан на баклажан",
            "Привет мир!",
            "аврора",
            "atmosphere"
        ]]
        self.assertEqual(data_cleaning_via_filters_apart(lambda_fun, test_lines), result_lines)


    def test_all(self):
        test_lines = [
            "Text",
            "Нажал кабан на баклажан",
            "Привет мир!",
            "аврора",
            "atmosphere"
        ]
        result_lines = ['аврора']
        self.assertEqual(data_cleaning_via_filters_together(filter_list, test_lines), result_lines)

if __name__ == '__main__':
    unittest.main()
