# Inputs: p_filename_data, contents of the file (string).
#         p_search_string, what you are looking for, literally (string)
# Output: Dictionary of test_find_string
# This module finds if there is a list


def find_string(p_filename_data, p_search_string):
    import re
    import warnings

    # test for a list that is created (i.e. abc = [asdf]
    p_search_object = re.search(p_search_string, p_filename_data, re.X | re.M | re.S)

    p_test_find_string = {"name": "Testing that this string is there: " + p_search_string,
                          "pass": True,
                          "pass_message": "Pass! Found this string: " + p_search_string,
                          "fail_message": "Fail.  Didn't find this string:" + p_search_string,
                   }
    if p_search_object:
        p_test_find_string['pass'] = True
    else:
        p_test_find_string['pass'] = False
    return p_test_find_string
