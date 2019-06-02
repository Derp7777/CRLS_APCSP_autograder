# Input parameters: p_filename - filename (string)
#                   p_test - the number of test to run
#                   p_string - the regex string you are going to search the output for (string)
#                   p_points - the number of points this test is worth
# Output: Dictionary of test_list_created
# This module runs tests


def io_test(p_filename, p_string, p_test_num, p_points):
    import sys
    import os

    import delegator
    import re

    from app.python_labs import YEAR
    from app.python_labs.read_file_contents import read_file_contents

    var_dir = ''
    if sys.platform == 'darwin':
        var_dir = '/Users/dimmyfinster/PycharmProjects/CRLS_APCSP_autograder/var'
        # This is Eric's home computer
    else:
        var_dir = '/home/ewu/CRLS_APCSP_autograder/var'
    if os.path.isdir(var_dir) is False:
        raise Exception("Cannot find the var dir")

    p_var_filename = re.sub('/tmp/', '', p_filename)
    p_var_filename = re.sub(YEAR + '_', '', p_var_filename)
    p_var_filename = re.sub('.py', '.in', p_var_filename)
    p_var_filename = re.sub('.+_', '', p_var_filename)
    p_var_filename = re.sub('\.in', '-' + str(p_test_num) + '.in', p_var_filename)
    p_filename_output = p_filename + '.out'

    p_test_io = {"name": "Testing input/output  (" + str(p_points) + " points).<br>" +
                         "In output, looking for " + str(p_string) + "<br>",
                 "pass": True,
                 "pass_message": "Pass! Input/output gave expected result. <br>",
                 "fail_message": "Fail. Input/output gave unexpected result. <br>",
                 }

    cmd = 'python3 ' + p_filename + ' < ' + var_dir + '/' + p_var_filename + ' > ' + p_filename_output
    c = delegator.run(cmd)
    if c.err:
        raise Exception('Failed, trying to run ' + cmd)

    print(cmd)
    outfile_data = read_file_contents(p_filename_output)
    print("passed read")
    search_object = re.search(p_string, outfile_data, re.X | re.M | re.S)
    if not search_object:
        p_test_io['pass'] = False

    return p_test_io


if __name__ == "__main__":
    print("yes")
    abc = io_test('/Users/dimmyfinster/PycharmProjects/untitled5/2019_ewu_1.040.py', 1, 'asdfsdf', 5)
    print(abc)