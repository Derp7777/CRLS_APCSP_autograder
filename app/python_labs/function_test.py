# Input parameters: lab i.e. 3.026 (string)
#                   test number (1,2,3,4)
# Output: Dictionary of test_list_created
# This module runs tests


def function_test(p_lab, p_test_number, p_points):
    import delegator
    import re

    p_test_function = {"name": "Testing calling functions, test " + str(p_test_number) + ".  (" + str(p_points) +
                               " points )",
                       "pass": True,
                       "pass_message": "Pass! Test number " + str(p_test_number) + " gave expected result. <br>",
                       "fail_message": "Fail. Test number " + str(p_test_number) + " gave unexpected result. <br>",
                       }

    cmd = 'python3 /tmp/' + str(p_lab) + '.test.py testAutograde.test_' + str(p_test_number) + " 2>&1 "
    c = delegator.run(cmd)

    print(cmd)
    error = re.search('Error', c.out, re.X | re.M | re.S)
    failed_assertion = re.search('AssertionError', c.out, re.X | re.M | re.S)
    OK = re.search('^OK$', c.out, re.X | re.M | re.S)

    formatted_cout = re.sub(r"\n", "<br>", c.out)
    if failed_assertion:
        p_test_function['pass'] = False
        p_test_function['fail_message'] += "Function ran but gave the wrong result. <br>"
        p_test_function['fail_message'] += formatted_cout + "<br>"
    elif error:
        p_test_function['pass'] = False
        p_test_function['fail_message'] += "Function didn't run at all.  Check for coding errors. <br>"
        p_test_function['fail_message'] += formatted_cout + "<br>"
    return p_test_function


# Inputs: p_filename, filename with python in it
# This module creates a testing file to run unit tests
def create_testing_file(p_filename):
    import delegator
    import sys
    import os
    import re

    from app.python_labs import YEAR

    if sys.platform == 'darwin':
        var_dir = '/Users/dimmyfinster/PycharmProjects/CRLS_APCSP_autograder/var'
        # This is Eric's home computer
    else:
        var_dir = '/home/ewu/CRLS_APCSP_autograder/var'
    if os.path.isdir(var_dir) is False:
        raise Exception("Cannot find the var dir")

    p_functions_filename = p_filename.replace('.py', '.functions.py')

    p_var_filename = re.sub('/tmp/', '', p_filename)
    p_var_filename = re.sub(YEAR + '_', '', p_var_filename)
    p_var_filename = re.sub('.py', '.test.py', p_var_filename)
    p_var_filename = re.sub('.+_', '', p_var_filename)
    cmd = ' cat ' + p_functions_filename + " " + var_dir + "/" + p_var_filename + "  > /tmp/" + p_var_filename
    c = delegator.run(cmd)

    if c.err:
        raise Exception("There as a problem creating the python test file " + cmd)


# Inputs: p_filename, filename to extract functions from
#         p_points, number of points this is worth.
# Output: none
# This module extracts all functions from a python file and puts them in a file outputfile.functions.py
def extract_all_functions(orig_file):
    import re
    outfile_name = orig_file.replace('.py', '.functions.py')
    outfile = open(outfile_name, 'w')
    with open(orig_file, 'r', encoding='utf8') as infile:
        line = True
        while line:
            line = infile.readline()
            start_def = re.search("^(def|class) \s+ .+ " , line,  re.X | re.M | re.S)
            if start_def:
                outfile.write(line)
                in_function = True
                while in_function:
                    line = infile.readline()
                    end_of_function = re.search("^[a-zA-Z]", line, re.X | re.M | re.S)
                    new_function = re.search("^(def|class) \s+ .+ " , line,  re.X | re.M | re.S)

                    if end_of_function and not new_function:
                        in_function = False
                        start_def = False
                    elif end_of_function and new_function:
                        in_function = True
                        start_def = True
                        outfile.write(line)

                    else:
                        outfile.write(line)


def extract_single_function(p_orig_file, p_function):
    import re
    function_file = p_orig_file.replace('.py', '.functions.py')
    extracted_function = ''
    with open(function_file, 'r', encoding='utf8') as infile:
        line = True
        while line:
            print("looking for this function : " + p_function)
            line = infile.readline()
            start_def = re.search(r"^(def|class) \s+ " + p_function , line,  re.X | re.M | re.S)
            if start_def:
                print("entering function!")
                print('writing this' + str(line))
                extracted_function += line
                print("reading this" + str(line))
                inside_function = True
                while inside_function:
                    print('reading this ' + str(line))
                    line = infile.readline()
                    inside_function = re.search(r"^(\s+ | \# ) .+ " , line,  re.X | re.M | re.S)
                    if inside_function:
                        print("writing this inside function " + str(line))
                        extracted_function += line
                extracted_function += line
    print(extracted_function)
    return extracted_function
