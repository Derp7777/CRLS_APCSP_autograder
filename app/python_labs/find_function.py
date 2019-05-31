# Inputs: p_filename_data, contents of the file (string).
#         p_function_name, function name I am looking for (string)
#         p_num_parameters, number of parameters I expect (integer)
# Output: Dictionary of test_function_exists
# This module finds if there is a function with a certain name and certain parameters


def find_function(p_filename, p_function_name, p_num_parameters):
    import re
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
    print(cmd_string)
    print(cmd)
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