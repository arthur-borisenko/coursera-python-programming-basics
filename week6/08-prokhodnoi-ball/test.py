import os.path
from os import system
import unittest
import task


def file_test(i, m):
    if not os.path.exists("input.txt"):
        open("input.txt", "x", encoding="utf-8").close()
    input_file = open("input.txt", "w", encoding="utf-8")
    try:
        input_file.write(i)
    finally:
        input_file.close()
    if not os.path.exists("output.txt"):
        open("output.txt", "x", encoding="utf-8").close()
    output_file = open("output.txt", "r", encoding="utf-8")
    try:
        m()
        result = output_file.read()
    finally:
        output_file.close()
    return result


class TestCase(unittest.TestCase):
    def test_case1(self):
        result = file_test("""5
Иванов Сергей 70 70 70
Сергеев Петр 100 100 0
Петров Василий 70 60 70
Васильев Андрей 70 60 70
Андреев Денис 100 30 100
Денисов Роман 50 50 50
Романов Иван 60 70 70
Ким Чен Ир 50 50 50
Ким Ир Сен 40 40 40""", task.main)
        self.assertEqual(result, """200
""")
    def test_case2(self):
        result = file_test("""1
Иванов Сергей 40 40 40
Сергеев Петр 100 100 39""", task.main)
        self.assertEqual(result, """0
""")
    def test_case3(self):
        result = file_test("""1
Иванов Сергей 60 60 60
Сергеев Петр 100 40 40""", task.main)
        self.assertEqual(result, """1
""")
    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
