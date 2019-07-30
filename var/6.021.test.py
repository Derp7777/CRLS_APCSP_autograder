import random
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
    def test_1(self):
        martinez_list = ['Goku', 'Goku', 'Goku', 'Goku', 'Goku']
        self.assertEqual(martinez_dictionary(martinez_list), {'Goku': 500},
                         "Test for martinez_dictionary, ['Goku', 'Goku', 'Goku', 'Goku', 'Goku'], expect back"
                         "{'Goku': 500}' <br>")

    def test_2(self):
        martinez_list = ['Goku', 'Goku', 'Trunks', 'Vegeta', 'Vegeta', 'Krillan', 'Goku']
        self.assertEqual(martinez_dictionary(martinez_list),
                         {'Goku': 300, 'Trunks': 100, 'Vegeta': 200, 'Krillan': 100},
                         "Test for martinez_dictionary, "
                         "['Goku', 'Goku', 'Trunks', 'Vegeta', 'Vegeta', 'Krillan', 'Goku'], expect back"
                         "{'Goku': 300, 'Trunks': 100, 'Vegeta':200, 'Krillan':100}' <br>"
                         )

    def test_3(self):
        names = ['Brolly', 'Goku', 'Gohan', 'Piccolo', 'Vegeta']
        answer1 = data_generator(names, 20)
        answer2 = data_generator(names, 20)
        self.assertNotEqual(answer1, answer2, "These two should be different because of random numbers<br>"
                                              "Run 1: " + str(answer1) +
                            "Run 2: " + str(answer2) +
                            "<br>If not, something is screwy about your random numbers.<br>")

    def test_4(self):
        names = ['Brolly', 'Goku', 'Gohan', 'Piccolo', 'Vegeta']
        answer = data_generator(names, 100)
        success = False
        try:
            if 'Brolly' in answer and 'Goku' in answer and 'Gohan' in answer and 'Piccolo' in answer and 'Vegeta' \
                    in answer:
                success = True
        except TypeError:
            success = False
        self.assertEqual(True, success, 'This checks to see that the ALL of the characters in the input list are '
                                        'being accessed by random numbers.  If this fails, often it is because'
                                        'the random item in the list is being generated incorrectly.  Could be'
                                        'the upper and lower range of the random number is incorrect.')


if __name__ == '__main__':
    unittest.main()
