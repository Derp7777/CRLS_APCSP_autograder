
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
    def test_1(self):
        self.assertEqual(the_rock_says(['eggs', 'apple']), ['The Rock says eggs', 'The Rock says apple'],
                         "Expected ['The Rock says eggs', 'The Rock says apple']')")

    def test_2(self):
        self.assertEqual(the_rock_says(['eggs', 'smell']),  ['The Rock says eggs',
                                                             'Do you smell what The Rock is cooking'],
                         "Expected ['The Rock says eggs', 'Do you smell what The Rock is cooking'] ")

    def test_3(self):
        self.assertEqual(the_rock_says(['smog', 'smells', 'smashmouth']),
                         ['Do you smell what The Rock is cooking', 'Do you smellell what The Rock is cooking',
                          'Do you smellellellellellell what The Rock is cooking'],
                         "Expected [ 'Do you smell what The Rock is cooking', "
                         "'Do you smellell what The Rock is cooking', "
                         "'Do you smellellellellellell what The Rock is cooking']"
                         )


if __name__ == '__main__':
    unittest.main()
