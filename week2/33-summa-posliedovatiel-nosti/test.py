import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''1
7
9
0'''.splitlines(), main)
        expected_result = "17\n"
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun('''1
1
1
1
1
1
1
1
1
0'''.splitlines(), main)
        expected_result = "9\n"
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun('''34
2345
2345
2345
2345
345
3
345
3
345
1
3
424
5
453
0'''.splitlines(), main)
        expected_result = "11341\n"
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
