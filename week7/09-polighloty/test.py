import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        result = mockAndRun("""3
3
Russian
English
Japanese
2
Russian
English
1
English""".splitlines(), main)
        value = result.splitlines()
        a = value[0]
        b = set(value[1:2])
        c = value[2]
        d = set(value[3:])
        exp_res = (
        "1", {"English"}, "3", {"Russian", "English", "Japanese"})
        self.assertEqual(exp_res, (a, b, c, d))

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
