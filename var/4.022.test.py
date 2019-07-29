
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
    def test_1(self):
        self.assertEqual(bad_lossy_compression('The rain in spain falls mainly in the plain'),
                         'Therai inspan fllsmaily n te pain', 'Expected "Therai inspan fllsmaily n te pain"')

    def test_2(self):
        self.assertEqual(bad_lossy_compression('I am sick and tired of these darned snakes on this darned plane'),
                         'I a sik ad tredof hes danedsnaes n tis arnd pane',
                         'Expected "I a sik ad tredof hes danedsnaes n tis arnd pane"')

    def test_3(self):
        self.assertEqual(bad_lossy_compression('Madness?!?!?!?! THIS IS SPARTA!!!!'),
                         'Madess!?!!?!THI ISSPATA!!!',
                         'Expected "Madess!?!!?!THI ISSPATA!!!"')


if __name__ == '__main__':
    unittest.main()
