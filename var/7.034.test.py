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
        self.assertTrue(getattr(goofy, name_key) == 'Goofy' and
                        getattr(goofy, pocket_key) == ['wallet', 'paper', 'rock', 'scissors'])

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
        self.assertEqual(['wallet', 'paper', 'rock', 'scissors', 'meatball'], getattr(goofy, pocket_key),
                         "Added 'meatball' to Goofy with ['wallet', 'paper', 'rock', 'scissors'] "
                         "<br>Expect to get Goofy with ['wallet', 'paper', 'rock', 'scissors', 'meatball']"
                         "Goofy pocket is " + str(goofy.pocket))

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
        self.assertEqual(['wallet', 'paper', 'rock', 'scissors'], getattr(goofy, pocket_key),
                         "Added Dr. Wu (of type DisneyBody) to Goofy with ['strawberries']<br>"
                         "Expect to get Goofy with ['wallet', 'paper', 'rock', 'scissors'] (i.e. no change"
                         "to Goofy, Goofy does'nt care about strawberries.<br>"
                         "Goofy pocket is " + str(goofy.pocket))

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

        self.assertEqual(['wallet', 'paper', 'rock', 'scissors', 'pancreas', 'liver', 'heart'],
                         getattr(goofy, pocket_key),
                         "Added Dr. Wu (of type DisneyBody) to Goofy with "
                         "['pancreas', 'liver', 'heart', 'strawberries']<br>"
                         "Expect to get Goofy with ['wallet', 'paper', 'rock', 'scissors', 'pancreas', 'liver', "
                         "'heart']] (i.e. Goofy does'nt care about strawberries but does care about organs.<br>"
                         "Goofy pocket is " + str(goofy.pocket)
                         )

    def test_5(self):
        from contextlib import redirect_stdout

        goofy = DisneyBody('Goofy', ['wallet', 'paper', 'rock', 'scissors'])

        f = io.StringIO()
        with redirect_stdout(f):
            print(goofy)
        print_string = f.getvalue()
        match_1 = len(re.findall(r"wallet", print_string, re.X | re.M | re.S))
        match_2 = len(re.findall(r"paper", print_string, re.X | re.M | re.S))
        match_3 = len(re.findall(r"rock", print_string, re.X | re.M | re.S))
        match_4 = len(re.findall(r"scissors", print_string, re.X | re.M | re.S))
        self.assertTrue(match_1 > 0 and match_2 > 0 and match_3 > 0 and match_4 > 0,
                        "Expect the __str__ method to return Goofy's pocket contents."
                        "Goofy's pocket is  ['wallet', 'paper', 'rock', 'scissors'] <br>so return "
                        "should include wallet, paper, rock, scissors.<br>"
                        "Found this many matches:<br>"
                        "Wallet: " + str(match_1) + "<br>" + "paper: " + str(match_2) +
                        "<br> rock: " + str(match_3) + "<br>"
                                                       "scissors: " + str(
                            match_4) + "<br> in this output: " + print_string + "<br>")


if __name__ == '__main__':
    unittest.main()
