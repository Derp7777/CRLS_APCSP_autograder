# Inputs: p_filename_data, contents of the file (string).
# Output: Dictionary of test_list_created
# This module finds if there is a list


def find_list(p_filename_data):
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

# Inputs: p_filename_data, contents of the file (string).
#         p_function_name, function name I am looking for (string)
#         p_num_parameters, number of parameters I expect (integer)
# Output: Dictionary of test_function_exists
# This module finds if there is a function with a certain name and certain parameters


def find_function(p_filename, p_function_name, p_num_parameters):
    import delegator


    # Check for function return_min
    cmd_string = ''
    if p_num_parameters == 0:
        cmd_string = 'grep "^def ' + p_function_name + '(\s*):"'
    elif p_num_parameters == 1:
        cmd_string = 'grep "^def ' + p_function_name + '(\s*[a-zA-Z_]\+[^,]\s*)"'
    elif p_num_parameters == 2:
        cmd_string = 'grep "^def ' + p_function_name + '(\s*[a-zA-Z_]\+,\s*[a-zA-Z_]\+[^,]\s*)"'
    elif p_num_parameters == 3:
        cmd_string = 'grep "^def ' + p_function_name + '(\s*[a-zA-Z_]\+,\s*[a-zA-Z_]\+,\s*[a-zA-Z_]\+[^,])\s*"'

    p_test_function_exists = {"name": "Testing that there is a function " + p_function_name +
                                      " with " + str(p_num_parameters) + " input parameters.",
                              "pass": True,
                              "pass_message": "Pass! There is a function " + p_function_name +
                                              " with " + str(p_num_parameters) + " input parameters. <br>",
                              "fail_message": "There is NOT a function " + p_function_name +
                                              " with " + str(p_num_parameters) + " input parameters. <br>",
                   }

    cmd = cmd_string + ' ' + p_filename
    c = delegator.run(cmd)
    if c.err:
        p_test_function_exists['pass'] = False
        p_test_function_exists['fail_message'] += "Error message: " + c.err
    elif c.out:
        p_test_function_exists['pass_message'] += "Found this: " + c.out
    else:
        p_test_function_exists['pass'] = False
        cmd = 'grep "def" ' + p_filename
        c = delegator.run(cmd)
        p_test_function_exists['fail_message'] += "The file " + p_filename + " has these functions: <br> " +\
                                                c.out + "<br>" + " but not " + p_function_name + " with" +\
                                                " exactly " + str(p_num_parameters) + " input parameter(s). <br>"
    return p_test_function_exists


if __name__ == "__main__":
    print("yes")
    find_function('/tmp/abc.py', 'hello', 3)