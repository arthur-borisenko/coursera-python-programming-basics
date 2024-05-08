import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''Abrakadabra'''.splitlines(), main)
        expected_result = """r
r
Abrak
Abrakadab
Arkdba
baaar
arbadakarbA
abdkrA
11\n"""
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun('''Hello'''.splitlines(), main)
        expected_result = """l
l
Hello
Hel
Hlo
el
olleH
olH
5\n"""
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun('''qwertyuiop'''.splitlines(), main)
        expected_result = """e
o
qwert
qwertyui
qetuo
wryip
poiuytrewq
piyrw
10\n"""
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
