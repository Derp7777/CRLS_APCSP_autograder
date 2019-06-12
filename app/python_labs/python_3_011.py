def python_3_011(p_filename, p_filename_data):
    from app.python_labs.io_test import io_test
    from app.python_labs.find_items import find_list_items, find_all_strings
    import sys
    import os

    import delegator
    import re

    from app.python_labs import YEAR
    from app.python_labs.read_file_contents import read_file_contents

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
    p_var_filename = re.sub('\.in', '-1.in', p_var_filename)

    cmd = 'python3 ' + p_filename + ' < ' + var_dir + '/' + p_var_filename
    c = delegator.run(cmd)
    if c.err:
        raise Exception('Failed, trying to run ' + cmd)

    # cmd = 'python3 ' + p_filename + ' < ' + var_dir + '/' + p_var_filename + ' > ' + p_filename_output
    # c = delegator.run(cmd)
    # if c.err:
    #     raise Exception('Failed, trying to run ' + cmd)
    #
    # outfile_data = read_file_contents(p_filename_output)
    # p_string = p_string.replace(' ', '\s')
    # p_string = p_string.replace('$', '\$')
    # p_string = p_string.replace('+', '\+')

    p_io_test = {"name": "Run the code 300 times.  Through 120 runs, should get at least one of each house "
                         "(10 points) <br>",
                 "pass": True,
                 "pass_message": "Pass!  After 120 runs, got at least one of each house",
                 "fail_message": "Fail. Didn't get all of the houses. <br>"
                                 "For example, if you have 7 houses in your list, after 120 runs, every house should"
                                 "come up at least once <br>.",
                 "score": 0,
                 }

    houses = find_list_items(p_filename_data, 'houses')

    answers = []
    for x in range(110):
        c = delegator.run(cmd)
        if c.err:
            raise Exception('Failed, trying to run ' + cmd + " with error " + c.err)
        for house in houses:
            if re.search(house, c.out):
                answers.append(house)

    print("houses "  + str(houses))
    print("answers" + str(answers))
    for house in houses:
        if house not in answers:
            p_io_test['pass'] = False
            p_io_test['fail_message'] += "Did not find this house in 300 runs of answers: " + house + ". <br>"
    return p_io_test