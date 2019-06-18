import random
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
      def test_fried_chicken_1(self):
            pieces = fried_chicken_problem_1(100,0)
            self.assertAlmostEqual(pieces, 25.0)

            
      def test_fried_chicken_2(self):
            pieces = fried_chicken_problem_1(10000,.25)
            passed = False
            if pieces < 2904 and pieces > 2902:
                  passed = True
            self.assertTrue(passed)

            
      def test_fried_chicken_3(self):
            pieces = fried_chicken_problem_2(100,0)
            passed = False
            if pieces < 25.2 and pieces > 24.8:
                  passed = True
            self.assertTrue(passed)

      def test_fried_chicken_4(self):
            pieces = fried_chicken_problem_1(10000,.25)
            passed = False
            if pieces < 2903.7 and pieces > 2902.2:
                  passed = True
            self.assertTrue(passed)

            

if __name__ == '__main__':
   unittest.main() 
