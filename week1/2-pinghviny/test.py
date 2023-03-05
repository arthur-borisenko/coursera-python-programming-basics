import sys
import unittest
from io import StringIO
from unittest import mock

from task import main


class Test(unittest.TestCase):

    @mock.patch('builtins.input', side_effect=['3'])
    def test_when3_then3(self, params):
        old_stdout = sys.stdout
        sys.stdout = capturedStdOut = StringIO()
        main()
        sys.stdout = old_stdout
        value = capturedStdOut.getvalue()
        print("Output")
        print(value)
        expected_result = """\
   _~_       _~_       _~_    
  (o o)     (o o)     (o o)   
 /  V  \   /  V  \   /  V  \  
/(  _  )\ /(  _  )\ /(  _  )\ 
  ^^ ^^     ^^ ^^     ^^ ^^   \
\n"""
        self.assertEqual(expected_result, value)

    @mock.patch('builtins.input', side_effect=['1'])
    def test_when1_then1(self, params):
        old_stdout = sys.stdout
        sys.stdout = capturedStdOut = StringIO()
        main()
        sys.stdout = old_stdout
        value = capturedStdOut.getvalue()
        print("Output")
        print(value)
        expected_result = """\
   _~_    
  (o o)   
 /  V  \  
/(  _  )\ 
  ^^ ^^   \
\n"""
        self.assertEqual(expected_result, value)


if __name__ == '__main__':
    unittest.main()
