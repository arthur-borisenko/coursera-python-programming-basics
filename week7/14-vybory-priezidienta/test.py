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
        result = file_test("""Полуэкт Варфоломеев
Варфоломей Полуэктов
Полуэкт Варфоломеев""", task.main)
        self.assertEqual(result, """Полуэкт Варфоломеев
""")
    def test_case2(self):
        result = file_test("""Полуэкт Варфоломеев
Варфоломей Виссарионов
Виссарион Полуэктов
Варфоломей Виссарионов
Варфоломей Виссарионов
Полуэкт Варфоломеев""", task.main)
        self.assertEqual(result, """Варфоломей Виссарионов
Полуэкт Варфоломеев
""")
    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
