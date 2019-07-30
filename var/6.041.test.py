import random
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
    def test_1(self):
        kann_list = ['fantastic spaghetti', 'fantastic spaghetti', 'garlic bread',
                     'noodles noodles', 'noodles noodles', 'Gooey gelato', 'fantastic spaghetti']
        answer = item_list_to_dictionary(kann_list)
        self.assertEqual(answer,
                         {'fantastic spaghetti': 3, 'garlic bread': 1, 'noodles noodles': 2, 'Gooey gelato': 1},
                         "<br>Checking that item_list_to_dictionary works.<br>   Input "
                         "['fantastic spaghetti', 'fantastic spaghetti', 'garlic bread', "
                         "'noodles noodles', "
                         "'noodles noodles', 'Gooey gelato', 'fantastic spaghetti'] "
                         "<br>Expected {'fantastic spaghetti': 3, 'garlic bread': 1, 'noodles noodles':2,"
                         "'Gooey gelato':1}) <br>Got this: " + str(answer)
                         )

    def test_2(self):
        kann_dict = {'fantastic spaghetti': 3, 'garlic bread': 1, 'noodles noodles': 2, 'Gooey gelato': 99}
        answer = min_item(kann_dict)
        self.assertEqual(answer, 'garlic bread', "<br>Call min_item with input"
                                                 " {'fantastic spaghetti': 3, 'garlic bread': 1, "
                                                 "'noodles noodles':2, "
                                                 "'Gooey gelato':99}.<br> "
                                                 "<br> Expect output 'garlic bread'). "
                                                 "<br>Got this: " + str(answer))


if __name__ == '__main__':
    unittest.main()
