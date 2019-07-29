import random
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
    def test_1(self):
        self.assertAlmostEqual(fried_chicken_problem_1(100, 0), 25.0)

    def test_2(self):
        self.assertTrue(2902 < fried_chicken_problem_1(10000, .25) < 2904)

    def test_3(self):
        self.assertTrue(24.8 < fried_chicken_problem_2(100, 0) < 25.2)

    def test_4(self):
        self.assertTrue(2902.2 < fried_chicken_problem_1(10000, .25) < 2903.7)


if __name__ == '__main__':
    unittest.main()
