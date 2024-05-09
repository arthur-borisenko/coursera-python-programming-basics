import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''Bilbo.Baggins@bagend.hobbiton.shire.me'''.splitlines(), main)
        expected_result = """Bilbo.Bagginsbagend.hobbiton.shire.me\n"""
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun('''dfa;sdkfj;ajva;bvna'sdasdfasdglJLHJKFHLDKJFh'''.splitlines(), main)
        expected_result = """dfa;sdkfj;ajva;bvna'sdasdfasdglJLHJKFHLDKJFh\n"""
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun('''@'''.splitlines(), main)
        expected_result = """\n"""
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
