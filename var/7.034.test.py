import random
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
    def test_1(self):
        goofy = DisneyBody('Goofy', ['wallet', 'paper', 'rock', 'scissors'])
        attribute_dict = vars(goofy)
        for key in attribute_dict:
            if isinstance(getattr(goofy, key), list):
                retrieved_pocket = getattr(goofy, key)
                pocket_key = key
            else:
                retrieved_name = attribute_dict[key]
                name_key = key
        success = False
        if getattr(goofy, name_key) == 'Goofy' and getattr(goofy,pocket_key) ==  ['wallet', 'paper', 'rock', 'scissors']:
            success = True
        self.assertEqual(True, success)


    def test_2(self):
        goofy = DisneyBody('Goofy', ['wallet', 'paper', 'rock', 'scissors'])
        goofy.add_content('meatball')
        attribute_dict = vars(goofy)
        for key in attribute_dict:
            if isinstance(getattr(goofy, key), list):
                retrieved_pocket = getattr(goofy, key)
                pocket_key = key
            else:
                retrieved_name = attribute_dict[key]
                name_key = key
        self.assertEqual(['wallet', 'paper', 'rock', 'scissors', 'meatball'], getattr(goofy, pocket_key))

    def test_3(self):
        goofy = DisneyBody('Goofy', ['wallet', 'paper', 'rock', 'scissors'])
        dr_wu = DisneyBody('Dr. Wu', ['strawberries'])
        goofy.add_content(dr_wu)
        attribute_dict = vars(goofy)
        for key in attribute_dict:
            if isinstance(getattr(goofy, key), list):
                retrieved_pocket = getattr(goofy, key)
                pocket_key = key
            else:
                retrieved_name = attribute_dict[key]
                name_key = key
        self.assertEqual(['wallet', 'paper', 'rock', 'scissors' ], getattr(goofy, pocket_key))

    def test_4(self):
        goofy = DisneyBody('Goofy', ['wallet', 'paper', 'rock', 'scissors'])
        dr_wu = DisneyBody('Dr. Wu', ['pancreas', 'liver', 'heart', 'strawberries'])
        goofy.add_content(dr_wu)
        attribute_dict = vars(goofy)
        for key in attribute_dict:
            if isinstance(getattr(goofy, key), list):
                retrieved_pocket = getattr(goofy, key)
                pocket_key = key
            else:
                retrieved_name = attribute_dict[key]
                name_key = key

        self.assertEqual(['wallet', 'paper', 'rock', 'scissors', 'pancreas', 'liver', 'heart'], getattr(goofy, pocket_key))


    def test_5(self):
        from contextlib import redirect_stdout

        goofy = DisneyBody('Goofy', ['wallet', 'paper', 'rock', 'scissors'])

        f = io.StringIO()
        with redirect_stdout(f):
            print(goofy)
        print_string = f.getvalue()
        search_object_1 = re.search(r"wallet", print_string, re.X| re.M | re.S)
        search_object_2 = re.search(r"paper", print_string, re.X| re.M | re.S)
        search_object_3 = re.search(r"rock", print_string, re.X| re.M | re.S)
        search_object_4 = re.search(r"scissors", print_string, re.X| re.M | re.S)
        passed = False
        if search_object_1 and search_object_2 and search_object_3 and search_object_4:
            passed = True
        self.assertEqual(True, passed)


if __name__ == '__main__':
    unittest.main()
