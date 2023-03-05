import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):

    def test_when3_then3(self):
        value = mockAndRun(['3'], main)
        expected_result = """\
   _~_       _~_       _~_    
  (o o)     (o o)     (o o)   
 /  V  \   /  V  \   /  V  \  
/(  _  )\ /(  _  )\ /(  _  )\ 
  ^^ ^^     ^^ ^^     ^^ ^^   \
\n"""
        self.assertEqual(expected_result, value)

    def test_when1_then1(self):
        value = mockAndRun(['1'], main)
        expected_result = """\
   _~_    
  (o o)   
 /  V  \  
/(  _  )\ 
  ^^ ^^   \
\n"""
        self.assertEqual(expected_result, value)