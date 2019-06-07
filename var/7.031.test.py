import random
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
      def test_1(self):
            stack1 = MoneyStack(1, 2, 3, 4, 5)
            if getattr(stack1, 'singles') == 1 and getattr(stack1, 'fives') == 2 and \
               getattr(stack1, 'tens') == 3 and getattr(stack1, 'twenties') == 4 and getattr(stack1, 'hundreds') == 5:
                  success = True
            self.assertEqual(True, success)
            
      def test_2(self):
            stack1 = MoneyStack(1, 1, 1, 2, 3)
            stack2 = MoneyStack(2, 0, 0, 1, 5)
            stack3 = stack1 + stack2
            success = False
            if stack3.singles == 3 and stack3.fives == 1 and stack3.tens == 1 and stack3.twenties == 3 and stack3.hundreds == 8:
                  success = True
            self.assertEqual(True, success)

      def test_3(self):
            stack1 = MoneyStack(4, 1, 1, 2, 3)
            stack2 = MoneyStack(9, 2, 2, 5, 9)
            stack3 = stack1 + stack2
            if stack3.singles == 3 and stack3.fives == 1 and stack3.tens == 1 and stack3.twenties == 4 and stack3.hundreds == 13:
                  success = True
            self.assertEqual(True, success)

            

if __name__ == '__main__':
   unittest.main() 
