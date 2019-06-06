def ten_runs(p_filename):

    import sys
    import os

    import delegator
    import re

    from app.python_labs import YEAR

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
    p_var_filename = re.sub('\.in', '-' + '1' + '.in', p_var_filename)
    p_filename_output = p_filename + '.out'

    cmd = 'python3 ' + p_filename + ' < ' + var_dir + '/' + p_var_filename
    c = delegator.run(cmd)
    if c.err:
        raise Exception('Failed, trying to run ' + cmd)

    p_matches = len(re.findall(r'\s of \s', c.out, re.X | re.M | re.S))
    p_ten_runs = {"name": "The code should draw 10 cards."
                         "(4 points) <br>",
                 "pass": True,
                 "pass_message": "Pass!  The code drew 10 cards",
                 "fail_message": "Fail. The code does not draw 10 cards.  Looking for a string like 'X  of  Y'. <br>"
                                 "Found this many matches:" + str(p_matches) + ' in this output: <br>' + c.out,
                 "score": 0,
                 }
    if p_matches < 10:
        p_ten_runs['pass'] = False
    return p_ten_runs

def check_random(p_filename):

    import sys
    import os

    import delegator
    import re

    from app.python_labs import YEAR

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
    p_var_filename = re.sub('\.in', '-' + '1' + '.in', p_var_filename)
    p_filename_output = p_filename + '.out'

    cmd = 'python3 ' + p_filename + ' < ' + var_dir + '/' + p_var_filename
    c = delegator.run(cmd)
    if c.err:
        raise Exception('Failed, trying to run ' + cmd)

    out1 = c.out
    cmd = 'python3 ' + p_filename + ' < ' + var_dir + '/' + p_var_filename
    c = delegator.run(cmd)
    if c.err:
        raise Exception('Failed, trying to run ' + cmd)

    out2 = c.out

    p_ten_runs = {"name": "The code should draw differently each time."
                         "(4 points) <br>",
                 "pass": True,
                 "pass_message": "Pass!  The code drew different cards",
                 "fail_message": "Fail. The code does not draw different cards. <br>"
                                 "Attempt 1 drew this:" + str(out1) + " <br>"
                                                                           "Attempt 2 drew this:" + str(out2),
                 "score": 0,
                 }
    if out1 == out2:
        p_ten_runs['pass'] = False
    else:
        p_ten_runs['score'] = 4
    return p_ten_runs