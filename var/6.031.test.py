import random
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
    def test_1(self):
        mcglathery_dict = {}
        output = add(mcglathery_dict, 'fire', 'charmander')
        self.assertEqual(output, {'fire': ['charmander']},
                         "<br>Checking mcglathery_dictionary 1. Adding 'fire' and 'charmander',"
                         " expect output {'fire':'charmander'} <br> Got this: " + str(output))

    def test_2(self):
        mcglathery_dict = {'fire': ['charmander'], 'ice': ['iceperson']}
        output = add(mcglathery_dict, 'ice', 'iceperson2')
        self.assertEqual(output,
                         {'fire': ['charmander'], 'ice': ['iceperson', 'iceperson2']},
                         "<br>Checking mcglathery_dictionary 2.  Adding 'ice' and 'iceperson2' to "
                         "{'fire':['charmander'], 'ice':['iceperson']}."
                         "<br> Expect output {['fire':['charmander'], 'ice':['iceperson','iceperson2']} <br>"
                         "Got this: " + str(output))

    def test_3(self):
        mcglathery_dict = {'fire': ['charmander']}
        answer = get(mcglathery_dict, 'fire')
        search_object = re.search(r"charmander", answer, re.X | re.M | re.S)
        self.assertTrue(search_object, "<br>Checking mcglathery_dictionary 3.  Testing get function "
                                       "with input  {'fire':['charmander']} "
                                       "expecting something with 'fire'  <br>"
                                       "Instead, got this: " + str(answer))

    def test_4(self):
        mcglathery_dict = {'fire': ['charmander', 'fireperson']}
        answer = get(mcglathery_dict, 'fire')
        search_object = re.search(r"charmander", answer, re.X | re.M | re.S)
        search_object2 = re.search(r"fireperson", answer, re.X | re.M | re.S)
        self.assertTrue(search_object and search_object2, "<br>Checking mcglathery_dictionary 4.  "
                                                          "testing get function with input  "
                                                          "{'fire':['charmander','fireperson'} "
                                                          "expecting something"
                                                          "with 'fire' and 'fireperson   <br>"
                                                          "Got this: " + str(answer))


if __name__ == '__main__':
    unittest.main()
