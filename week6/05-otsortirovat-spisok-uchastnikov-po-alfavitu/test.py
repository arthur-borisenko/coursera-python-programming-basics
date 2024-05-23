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
        result = file_test("""Иванов Сергей 14 56
Сергеев Петр 23 74
Петров Василий 3 99
Васильев Андрей 3 56
Андреев Роман 14 75
Романов Иван 27 68""", task.main)
        self.assertEqual(result, """Андреев Роман 75
Васильев Андрей 56
Иванов Сергей 56
Петров Василий 99
Романов Иван 68
Сергеев Петр 74
""")

    def test_case2(self):
        result = file_test("""Андреев Роман 14 75
Васильев Андрей 3 56
Иванов Сергей 14 56
Петров Василий 3 99
Романов Иван 27 68
Сергеев Петр 23 74""", task.main)
        self.assertEqual(result, """Андреев Роман 75
Васильев Андрей 56
Иванов Сергей 56
Петров Василий 99
Романов Иван 68
Сергеев Петр 74
""")

    def test_case3(self):
        result = file_test("""Сергеев Петр 23 74
Романов Иван 27 68
Петров Василий 3 99
Иванов Сергей 14 56
Васильев Андрей 3 56
Андреев Роман 14 75""", task.main)
        self.assertEqual(result, """Андреев Роман 75
Васильев Андрей 56
Иванов Сергей 56
Петров Василий 99
Романов Иван 68
Сергеев Петр 74
""")

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
