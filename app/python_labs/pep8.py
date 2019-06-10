def pep8(p_filename, p_max_points):
    """
    This module fines the number of PEP8 errors
    :param p_filename: Name of the python file
    :param p_max_points: maximum number of points you can get for 0 pep8 errors or warnings
    :return: dictionary with test info
    """
    import delegator
    import sys

    ignore_codes = 'E226,E241,W504,W293,E126,W503'
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
        cmd = pycodestyle_file + ' --ignore=' + ignore_codes + ' --max-line-length=120 ' + p_filename
        print(cmd)
        c = delegator.run(cmd)
        error_msg = c.out
        error_msg = error_msg.replace(p_filename, '<br>' + p_filename)
    test_pep8 = {"name": "Testing for PEP8 warnings and errors (" + str(p_max_points) + " points)",
                 "pass": True,
                 "pass_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>" +
                                 "This translates to -" +
                                 str(min(p_max_points, side_errors)) +
                                 " point(s) deduction.<br>" +
                                 " Warnings/Errors are:" + error_msg + ".<br>",
                 "pep8_errors": 0,
                 'points': 0,
                 }
    test_pep8['fail_message'] = test_pep8['pass_message']
    if side_errors != 0:
        test_pep8['pep8_errors'] = side_errors
    test_pep8['points'] = max(0, int(p_max_points) - test_pep8['pep8_errors'])

    return test_pep8
