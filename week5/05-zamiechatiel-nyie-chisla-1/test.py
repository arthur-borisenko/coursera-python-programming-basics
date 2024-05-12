import unittest
from os import system


class Test(unittest.TestCase):
    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
