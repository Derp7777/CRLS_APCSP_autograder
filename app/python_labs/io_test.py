def _var_dir():
    """
    This helper function returns the var dir, depending on if code is run at CRLS or at Eric's Mac
    :return:The var dir for the CRLS autograder
    """
    import sys
    import os

    if sys.platform == 'darwin':
        var_dir = '/Users/dimmyfinster/PycharmProjects/CRLS_APCSP_autograder/var'  # This is Eric's home computer
    else:
        var_dir = '/home/ewu/CRLS_APCSP_autograder/var'
    if os.path.isdir(var_dir) is False:
        raise Exception("Cannot find the var dir" + var_dir)
    return var_dir


def _var_filename(p_filename, p_test_num):
    """ This helper function returns the var filename, depending on if the code is run on Unix or Eric's Mac
    :param p_filename: The filename to evaluate
    :param p_test_num: the IO input test number
    :return: The var filename for the CRLS autograder
    """
    import re
    from app.python_labs import YEAR

    p_var_filename = re.sub(r'/tmp/', '', p_filename)
    p_var_filename = re.sub(YEAR + '_', '', p_var_filename)
    p_var_filename = re.sub(r'.py', '.in', p_var_filename)
    p_var_filename = re.sub(r'.+_', '', p_var_filename)
    p_var_filename = re.sub(r'\.in', '-' + str(p_test_num) + '.in', p_var_filename)

    return p_var_filename

# Input parameters: p_filename - filename (string)
#                   p_test - the number of test to run
#                   p_string - regex string you are going to search the output for (string)
#                   p_occurences - number of times you want this string to show up (int)
#                   p_points - the number of points this test is worth
# Output: Dictionary of test_list_created
# This module runs tests and tries to find all strings in output

def io_test_find_string(p_filename, p_string, p_test_num, p_occurences, p_points):
    import delegator
    import re


    var_dir = _var_dir()
    var_filename = _var_filename(p_filename, p_test_num)

    cmd = 'python3 ' + p_filename + ' < ' + var_dir + '/' + var_filename
    c = delegator.run(cmd)
    if c.err:
        raise Exception('Failed, trying to run ' + cmd)
    outfile_data = c.out
    p_string = p_string.replace(' ', '\s')
    p_string = p_string.replace('$', '\$')
    p_string = p_string.replace('+', '\+')

    p_matches = len(re.findall(p_string, outfile_data, re.X | re.M | re.S))

    p_test_io = {"name": "Testing input/output  (" + str(p_points) + " points).<br>" +
                         "In output, looking for " + str(p_string) + " " + str(p_occurences) + " times. <br>",
                 "pass": True,
                 "pass_message": "Pass! Input/output gave expected result. <br>",
                 "fail_message": "Fail. Input/output gave unexpected result. <br>" +
                                 "Looked for this: " + str(p_string) + "<br>" +
                                 " in this: " + str(outfile_data) + ".<br>"
                                 "Found it " + str(p_matches) + " times.<br>",
                 }
    if p_matches < p_occurences:
        p_test_io['pass'] = False
        p_test_io['occurences'] = p_matches
    return p_test_io


def io_test(p_filename, p_string, p_test_num, *, points=0, occurrences=1):
    """
    This function runs a python program with a piped in file.  Then looks for certain strings.
    Returns a test dictionary.
    :param p_filename: filename of python code (string)
    :param p_string: regex string you are going to search the output for (string)
    :param p_test_num: the number of test to run (basically the input file for test)
    :param points: the number of points this test is worth
    :param occurrences: how many times you want the string to show up in the code output
    :return: Dictionary containing info for this test.
    """
    import delegator
    import re

    var_dir = _var_dir()
    var_filename = _var_filename(p_filename, p_test_num)

    cmd = 'python3 ' + p_filename + ' < ' + var_dir + '/' + var_filename
    c = delegator.run(cmd)
    if c.err:
        raise Exception('Failed, trying to run ' + cmd + ".  Try running the program manually to see what is wrong.")

    outfile_data = c.out

    p_test_io = {"name": "Testing input/output  (" + str(points) + " points).<br>" +
                         "In output, looking for " + str(p_string) + "<br>",
                 "pass": True,
                 "pass_message": "<h5 style=\"color:green;\">Pass!</h5> Input/output gave expected result. <br>",

                 "fail_message": "<h5 style=\"color:red;\">Fail.</h5> Input/output gave unexpected result. <br>" +
                                 "Looked for this: " + str(p_string) + "<br>" +
                                 " in this: " + str(outfile_data) + "<br>",
                 "points": 0
                 }

    p_string = p_string.replace(' ', r'\s')
    p_string = p_string.replace('$', r'\$')
    p_string = p_string.replace('.', r'\.')
    p_string = p_string.replace('+', r'\+')

    print("p_string")
    print(p_string)
    print("outfile_data")
    print(outfile_data)
    p_matches = len(re.findall(p_string, outfile_data, re.X | re.M | re.S))

    if p_matches < occurrences:
        p_test_io['pass'] = False
        p_test_io['fail_message'] += "Found this many matches: " + str(p_matches)
    else:
        p_test_io['points'] += points
    print("before")
    print(p_test_io)
    return p_test_io


def io_test_find_all(p_filename, p_strings, p_test_num, *, points=0):
    """
    This function runs a python program with a piped in file.  Then looks for certain strings X times, using io_test.
    :param p_filename: Filename of python code (strong)
    :param p_strings: regex strings you are going to search the output for (string)
    :param p_test_num: the number of test to run (basically the input file for test)
    :param points: Points this test is worth
    :return: Dictionary containing info for this test.
    """

    tests = []
    for regex_string in p_strings:
        this_test = io_test(p_filename, regex_string, p_test_num)
        tests.append(this_test)

    p_test_io = {"name": "Testing input/output  (" + str(points) + " points).<br>" +
                         "In output, looking for " + str(p_strings) + "<br>",
                 "pass": True,
                 "pass_message": "<h5 style=\"color:green;\">Pass!</h5>"
                                 " Input/output gave expected result. <br>",
                 "fail_message": "<h5 style=\"color:red;\">Fail</h5>."
                                 " Input/output gave unexpected result. <br>",
                 'points': 0
                 }

    for this_test in tests:
        if not this_test['pass']:
            p_test_io['pass'] = False
            p_test_io['fail_message'] += this_test['fail_message']
    if p_test_io['pass']:
        p_test_io['points'] += points

    return p_test_io



if __name__ == "__main__":
    print("yes")
    #  abc = io_test('/Users/dimmyfinster/PycharmProjects/untitled5/2019_ewu_1.040.py', 1, 'asdfsdf', 5)
    #  print(abc)
    # abc = io_test_find_all ('/Users/dimmyfinster/PycharmProjects/untitled5/2019_ewu_1.060.py',

    #                        ['(\^ | \s+ ) b2 (\s+ | \? | \. | , | !)'], 1, 5)
    abc = io_test_find_all('/home/ewu/CRLS_APCSP_Mac_Autograder/2.051/2019_ewu_1.040.py',
                            [r'(\^ | \s+ ) b2 (\s+ | \? | \. | , | !)'], 1, 5)

    print(abc)
