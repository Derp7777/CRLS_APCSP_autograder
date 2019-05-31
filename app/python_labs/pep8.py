# Inputs: p_filename, filename to search for help.
#         p_points, number of points this is worth.
# Output: dictionary of test_help
# This module finds number of pep8 errors


def pep8(p_filename, p_max_points):
    import delegator
    import sys

    ignore_codes = 'E226,E241,W504,W293,E126'
    if sys.platform == 'darwin':
        pycodestyle_file = '/Users/dimmyfinster/PycharmProjects/CRLS_APCSP_autograder/venv1/bin/pycodestyle'
        # This is Eric's home computer
    else:
        pycodestyle_file = '/home/ewu/CRLS_APCSP_autograder/venv1/bin/pycodestyle'
    try:
        fh = open(pycodestyle_file, 'r')
    except FileNotFoundError:
        raise Exception("Could not find pycodestyle file " + pycodestyle_file)
    fh.close()

    cmd = pycodestyle_file + ' --ignore=' + ignore_codes + ' --max-line-length=120 ' + p_filename + ' | wc -l '
    c = delegator.run(cmd)
    if c.err:
        raise Exception(c.err)
    side_errors = int(c.out)
    error_msg = 'NONE'
    if side_errors != 0:
        cmd = pycodestyle_file + ' --ignore=' + ignore_codes + '--max-line-length=120 ' + p_filename
        c = delegator.run(cmd)
        error_msg = c.out
        error_msg = error_msg.replace(p_filename, '<br>' + p_filename)
    test_pep8 = {"name": "Testing for PEP8 warnings and errors (" + str(p_max_points) + " points)",
                 "pass": True,
                 "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                 "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>" +
                                 "This translates to -" +
                                 str(min(p_max_points, side_errors)) +
                                 " point(s) deduction.<br>" +
                                 " Warnings/Errors are:" + error_msg,
                 "pep8_errors": 0
                 }
    if side_errors != 0:
        test_pep8['pass'] = False
        test_pep8['pep8_errors'] = side_errors
    return test_pep8
