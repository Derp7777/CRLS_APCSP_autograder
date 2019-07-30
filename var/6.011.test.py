import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
    def test_1(self):
        bob_dict = {'wth': 'What the heck'}
        self.assertEqual(bob_kraft_translator(bob_dict, 'wth'), 'What the heck')

    def test_2(self):
        bob_dict = {'wth': 'What the heck',
                    'aymm': 'Ay yo my man',
                    }
        self.assertEqual(bob_kraft_translator(bob_dict, 'aymm'), 'Ay yo my man')

    def test_3(self):
        bob_dict = {'wth': 'What the heck',
                    'aymm': 'Ay yo my man',
                    }
        answer = bob_kraft_translator(bob_dict, 'asdfasdf')
        print(answer)
        self.assertTrue(re.search("do \s not \s know", answer, re.X | re.M | re.S))


if __name__ == '__main__':
    unittest.main()
