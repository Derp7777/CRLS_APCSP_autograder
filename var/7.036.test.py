

import random
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
    def test_1(self):
        cocaine = Contraband('Pure cocaine', 3000)
        attribute_dict = vars(cocaine)
        error_msg = ''
        for key in attribute_dict:
            if isinstance(getattr(cocaine, key), int):
                street_value = getattr(cocaine, key)
                value_key = key
            else:
                description = attribute_dict[key]
                description_key = key
        success = False
        if getattr(cocaine, description_key) == 'Pure cocaine' and \
                getattr(cocaine, value_key) == 3000:
            success = True
        else:
            error_msg = 'Expected description of "Pure cocaine" but got this: ' +  getattr(cocaine, description_key)
            error_msg += 'Expected value of 3000 but got this:' + str(getattr(cocaine, value_key))
        self.assertEqual(True, success, error_msg)


    def test_2(self):
        smuggler = Ship('S. S. smuggler', ['apples', 'bananas'])
        attribute_dict = vars(smuggler)
        error_msg = ''
        for key in attribute_dict:
            if isinstance(getattr(smuggler, key), list):
                cargo_key = key
            else:
                description_key = key
        success = False
        if getattr(smuggler, description_key) == 'S. S. smuggler' and \
                getattr(smuggler, cargo_key) == ['apples', 'bananas']:
            success = True
        else:
            error_msg = 'Expected name of "S. S. smuggler" but got this: ' +  getattr(smuggler, description_key)
            error_msg += "Expected cargo of  ['apples', 'bananas'] but got this:" + str(getattr(smuggler, cargo_key))
        self.assertEqual(True, success, error_msg)


    def test_3(self):
        smuggler = Ship('S. S. smuggler', ['apples', 'bananas'])
        smuggler.load('oranges')

        self.assertEqual(smuggler.cargo, ['apples', 'bananas', 'oranges'],
                         "Added oranges to a ship object with Goofy with ['apples', 'bananas'].<br>"
                         "Expected ['apples', 'bananas', 'oranges'], got "+ str(smuggler.cargo) + "<br>")

    def test_4(self):
        smuggler = Ship('S. S. smuggler', ['apples', 'bananas'])
        cocaine = Contraband('Pure cocaine', 3000)
        smuggler.load(cocaine)
        smuggler.load('oranges')
        smuggler.dump()
        self.assertEqual(smuggler.cargo, ['apples', 'bananas', 'oranges'],
                         "Started with ship of ['apples', 'bananas']. <br>"
                         "loaded object cocaine of type Contraband. <br>"
                         "loaded 'oranges. <br>"
                         "ran method dump <br>"
                         "Expected ['apples', 'bananas', 'oranges'], got " + str(smuggler.cargo) + "<br>"
                         )


    def test_5(self):
        import re
        from contextlib import redirect_stdout

        smuggler = Ship('S. S. smuggler', ['apples', 'bananas'])
        f = io.StringIO()
        with redirect_stdout(f):
            print(smuggler)
        print_string = f.getvalue()
        match_1 = len(re.findall(r"apples", print_string, re.X | re.M | re.S))
        match_2 = len(re.findall(r"bananas", print_string, re.X | re.M | re.S))
        passed = False
        if match_1 > 0 and match_2 > 0 :
            passed = True
        self.assertEqual(True, passed, "Expect the __str__ method to return cargo of Ship object. "
                                       "Ship's cargo is ['apples', 'bananas'] <br>"
                                       "Got: " + str(smuggler.cargo))

if __name__ == '__main__':
    unittest.main()
