def run_unit_test(p_lab, p_test_number, p_points):
    """
    unit test runs the unit tests.  It assumes that there is a file /tmp/<lab number>.test.py and runs one test
    :param p_lab: lab number (str) i.e. 4.021
    :param p_test_number: test number within the test suite to run
    :param p_points: number of points this is worth
    :return: test dictionary
    """
    import delegator
    import re

    p_unit_test = {"name": "Testing calling functions, test " + str(p_test_number) + ".  (" + str(p_points) +
                           " points )",
                   "pass": True,
                   "pass_message": "<h5 style=\"color:green;\">Pass!</h5> Test number " + str(p_test_number) +
                                   " gave expected result. <br>",
                   "fail_message": "<h5 style=\"color:red;\">Fail.</h5> Test number " + str(p_test_number) +
                                   " gave unexpected result. <br>",
                   'points': 0
                   }

    cmd = 'python3 /tmp/' + str(p_lab) + '.test.py testAutograde.test_' + str(p_test_number) + " 2>&1 "
    c = delegator.run(cmd)

    error = re.search('Error', c.out, re.X | re.M | re.S)
    failed_assertion = re.search('AssertionError', c.out, re.X | re.M | re.S)
    ok = re.search(r'^OK$', c.out, re.X | re.M | re.S)

    formatted_cout = re.sub(r"\n", "<br>", c.out)
    if failed_assertion:
        p_unit_test['pass'] = False
        p_unit_test['fail_message'] += "Function ran but gave the wrong result. <br>"
        p_unit_test['fail_message'] += formatted_cout + "<br>"
    elif error:
        p_unit_test['pass'] = False
        p_unit_test['fail_message'] += "Function didn't run at all.  Check for coding errors. <br>"
        p_unit_test['fail_message'] += formatted_cout + "<br>"
    else:
        p_unit_test['points'] += p_points
    return p_unit_test


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
    """
    Extracts all functions
    :param orig_file: The name of the python file (string)
    :return: Nothing. It writes everything to the file <python file>.functions.py
    """
    import re
    outfile_name = orig_file.replace('.py', '.functions.py')
    outfile = open(outfile_name, 'w')

    with open(orig_file, 'r', encoding='utf8') as infile:
        line = True

        while line:
            line = infile.readline()
            start_def = re.search(r"^(def|class) \s+ .+ ", line,  re.X | re.M | re.S)
            # print(start_def)
            empty_counter = 0
            if start_def:

                outfile.write(line)
                in_function = True
                # counter = 0
                while in_function:
                    # counter += 1
                    # print("counter " + str(counter))
                    # if counter == 15:
                    #     raise Exception("what the heeck")
                    line = infile.readline()
                    if line == '':
                        break
                    # print("aaa next line " + line)
                    end_of_function = re.search(r"^[a-zA-Z]", line, re.X | re.M | re.S)
                    new_function = re.search(r"^(def|class) \s+ .+ ", line,  re.X | re.M | re.S)
                    # print("end? " + str(end_of_function))
                    # print("new?" + str(new_function))
                    if end_of_function and not new_function:
                        in_function = False
                        start_def = False
                    elif end_of_function and new_function:
                        in_function = True
                        start_def = True
                        outfile.write(line)
                    else:
                        outfile.write(line)
                    # print("aaa this line still " + str(line))
                    # print("in fucntion start_def " + str(in_function) + " " + str(start_def))


def extract_single_function(p_orig_file, p_function):
    import re
    function_file = p_orig_file.replace('.py', '.functions.py')
    extracted_function = ''
    with open(function_file, 'r', encoding='utf8') as infile:
        line = True
        while line:
            # print("looking for this function : " + p_function)
            line = infile.readline()
            start_def = re.search(r"^(def|class) \s+ " + p_function , line,  re.X | re.M | re.S)
            if start_def:
                # print("entering function!")
                # print('writing this' + str(line))
                extracted_function += line
                #print("reading this" + str(line))
                inside_function = True
                while inside_function:
                #     print('reading this ' + str(line))
                    line = infile.readline()
                    inside_function = re.search(r"^(\s+ | \# ) .+ " , line,  re.X | re.M | re.S)
                    if inside_function:
                        # print("writing this inside function " + str(line))
                        extracted_function += line
                extracted_function += line
    # print(extracted_function)
    return extracted_function
