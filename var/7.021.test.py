import random
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
    def test_1(self):
        leia = Collectible('Leia action figure', 'poor', 400)
        attribute_dict = vars(leia)
        value_key = ''
        retrieved_string1 = ''
        attr1 = ''
        attr2 = ''
        attr3 = ''
        for key in attribute_dict:
            print("key here " + key)
            if isinstance(getattr(leia, key), int):
                value_key = key
            else:
                print("retrieved string " + retrieved_string1)
                if not attr2:
                    attr2 = key
                else:
                    attr3 = key
        success = getattr(leia, value_key) == 400 and \
                  (getattr(leia, attr2) == 'Leia action figure' and getattr(leia, attr3) == 'poor' or
                   getattr(leia, attr3) == 'Leia action figure' and getattr(leia, attr2) == 'poor')
        self.assertEqual(True, success, 'Testing to see that attributes are set correctly.<br>'
                                        'Found these attributes for Leia object (expected "Leia action figure",'
                                        '"poor", and "400").  :<br>'
                                        'value 1: ' + value_key + ' attribute2: ' + attr2 + "<br> attribute3: " + attr3)

    def test_2(self):
        leia = Collectible('Leia action figure', 'poor', 400)
        rey = Collectible('Rey in her racer', 'new', 30)
        collectibles = [leia, rey]
        output = collectible_printer(collectibles)
        search_object = re.search(r"Leia \s action \ figure", output, re.X | re.M | re.S)
        search_object2 = re.search(r"Rey \s in \s her \ racer", output, re.X | re.M | re.S)
        self.assertTrue(search_object and search_object2, "<br>With list of two objects 'Leia action figure' and"
                                                          "'Rey in her racer', <br>I expect to see these strings "
                                                          "in the return value of collectible_printer.<br>"
                                                          "Output was this: " + output)

    def test_3(self):
        leia = Collectible('Leia action figure', 'poor', 400)
        rey = Collectible('Rey in her racer', 'new', 30)
        collectibles = [leia, rey]
        output = collectible_printer(collectibles)
        print(output)
        search_object = re.search(r"430", output, re.X | re.M | re.S)
        self.assertTrue(search_object, "<br>Ran collectible printer with two items of values 400 and 30.  "
                                       "<br>Expect to see 430 in the output.<br>  Output is this:" + str(output))


if __name__ == '__main__':
    unittest.main()
