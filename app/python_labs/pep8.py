# Inputs: p_filename, filename to search for help.
#         p_points, number of points this is worth.
# Output: dictionary of test_help


def pep8(p_filename, p_max_points):
    import delegator

    # Find number of PEP8 errors
    pycodestyle_file = '/home/ewu/CRLS_APCSP_autograder/venv1/bin/pycodestyle'
    try:
        fh = open(pycodestyle_file, 'r')
    except FileNotFoundError:
        raise Exception("Could not find pycodestyle file " + pycodestyle_file)
    fh.close()

    cmd = pycodestyle_file + ' --ignore=E305,E226,E241,W504,W293,E126 --max-line-length=120 ' + p_filename + ' | wc -l '
    c = delegator.run(cmd)
    side_errors = int(c.out)
    test_pep8 = {"name": "Testing for PEP8 warnings and errors (14 points)",
                 "pass": True,
                 "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                 "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>" +
                                 "This translates to -" +
                                 str(max(p_max_points, side_errors)) +
                                 "point(s) deduction.<br>",
                 "pep8_errors": 0
                 }
    if side_errors != 0:
        test_pep8['pass'] = False
        test_pep8['pep8_errors'] = side_errors
    return test_pep8
