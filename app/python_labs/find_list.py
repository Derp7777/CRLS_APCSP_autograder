# Inputs: p_filename_data, contents of the file (string).
# Output: Dictionary of test_list_created
# This module finds if there is a list


def list_created(p_filename_data):
    import re

    # test for a list that is created (i.e. abc = [asdf]
    p_search_object = re.search(r". \s* = \s* \[ .* \]", p_filename_data, re.X | re.M | re.S)

    p_test_list = {"name": "Testing that there is something that looks like a list being created.",
                   "pass": True,
                   "pass_message": "Pass! Submitted file has something that looks like a list being created.",
                   "fail_message": "Submitted file does not look like it has a list being created.",
                   }
    if p_search_object:
        p_test_list['pass'] = True
    else:
        p_test_list['pass'] = False
    return p_test_list
