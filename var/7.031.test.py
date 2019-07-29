import random
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
    def test_1(self):
        stack1 = MoneyStack(1, 2, 3, 4, 5)
        self.assertTrue(getattr(stack1, 'singles') == 1 and getattr(stack1, 'fives') == 2 and
                        getattr(stack1, 'tens') == 3 and getattr(stack1, 'twenties') == 4 and
                        getattr(stack1, 'hundreds') == 5, "Verifying that the __init__ method is correct")

    def test_2(self):
        stack1 = MoneyStack(1, 1, 1, 2, 3)
        stack2 = MoneyStack(2, 0, 0, 1, 5)
        stack3 = stack1 + stack2
        self.assertTrue(stack3.singles == 3 and stack3.fives == 1 and stack3.tens == 1 and stack3.twenties == 3
                        and stack3.hundreds == 8, "Verifying that moneystack of (1, 1, 1, 2, 3) <br>"
                        "added to moneystack of (2, 0, 0, 1, 5) <br>"
                        "gives a new stack of (3, 1, 1, 3, 8).<br>"
                        "Actual result is:"
                        "<br>singles: " + str(stack3.singles) +
                        "<br>fives: " + str(stack3.fives) +
                        "<br>tens: " + str(stack3.tens) +
                        "<br>twenties: " + str(stack3.twenties) +
                        "<br>hundreds: " + str(stack3.hundreds))

    def test_3(self):
        stack1 = MoneyStack(4, 1, 1, 2, 3)
        stack2 = MoneyStack(9, 2, 2, 5, 9)
        stack3 = stack1 + stack2
        # TODO could the next one just be stack3 == MoneyStack(3, 1, 1, 4, 13)?
        self.assertTrue(stack3.singles == 3 and stack3.fives == 1 and stack3.tens == 1 and stack3.twenties == 4
                        and stack3.hundreds == 13, "Verifying that moneystack of (4, 1, 1, 2, 3) <br>"
                        "added to moneystack of (9, 2, 2, 5, 9) <br>"
                        "gives a new stack of (3, 1, 1, 4, 13).<br>"
                        "Actual result is:"
                        "<br>singles: " + str(stack3.singles) +
                        "<br>fives: " + str(stack3.fives) +
                        "<br>tens: " + str(stack3.tens) +
                        "<br>twenties: " + str(stack3.twenties) +
                        "<br>hundreds: " + str(stack3.hundreds))



if __name__ == '__main__':
    unittest.main()
