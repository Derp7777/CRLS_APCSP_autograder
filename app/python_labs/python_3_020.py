def ten_runs(p_filename):

    import delegator
    import re

    from app.python_labs.io_test import _var_dir, _var_filename

    var_dir = _var_dir()
    p_var_filename = _var_filename(p_filename, 1)

    cmd = 'python3 ' + p_filename + ' < ' + var_dir + '/' + p_var_filename
    c = delegator.run(cmd)
    if c.err:
        raise Exception('Failed, trying to run ' + cmd)

    p_matches = len(re.findall(r'\s of \s', c.out, re.X | re.M | re.S))
    p_ten_runs = {"name": "The code should draw 10 cards."
                          "(4 points) <br>",
                  "pass": True,
                  "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  The code drew 10 cards",
                  "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                                  "The code does not draw 10 cards.  Looking for a string like 'X  of  Y'. <br>"
                                  "Found this many matches:" + str(p_matches) + ' in this output: <br>' + c.out,
                  "points": 0,
                  }
    if p_matches < 10:
        p_ten_runs['pass'] = False
    else:
        p_ten_runs['points'] += 4
    return p_ten_runs


def check_random(p_filename):

    import delegator
    import re

    from app.python_labs.io_test import _var_dir, _var_filename

    var_dir = _var_dir()
    p_var_filename = _var_filename(p_filename, 1)

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
                  "pass_message": "<h5 style=\"color:green;\">Pass!</h5> The code drew different cards",
                  "fail_message": "<h5 style=\"color:red;\">Fail.</h5> The code does not draw different cards. <br>"
                                  "Attempt 1 drew this:" + str(out1) + " <br>"
                                                                       "Attempt 2 drew this:" + str(out2),
                  "points": 0,
                  }
    if out1 == out2:
        p_ten_runs['pass'] = False
    else:
        p_ten_runs['points'] += 4
    return p_ten_runs
