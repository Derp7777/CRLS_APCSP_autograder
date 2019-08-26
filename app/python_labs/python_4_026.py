def case_1(p_filename):
    import re
    from app.python_labs.io_test import io_test

    p_test = {"name": "Given 10000 sims, Atwood's dance party AND army taking over happens ~50% of the time"
                      " (10 points) <br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5> In 10,000 simulations, "
                              "dance party and undead taking over happens ~50% o the time",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "In 10,000 simulations, did not find something around 50%.<br>"
                              "Check looks for a string that looks like this: '50%'"
                              "<br>Spacing and percent symbols matter! 100.0 % or 100.0 will fail.<br>",
              "points": 0,
              }
    test1 = io_test(p_filename, r'NO_MATCH', 1)
    match = re.findall(r'([0-9]+\.[0-9]+)%', test1['fail_message'], re.X | re.M | re.S)
    if match:
        for number in match:
            percent = float(number)
            print('number ' + str(percent))
            if 47.0 < percent < 53.0:
                p_test['points'] += 10
                p_test['pass'] = True
                break
    else:
        p_test['pass'] = False
    if p_test['pass'] is False:
        p_test['fail_message'] += 'Found these percentages ' + str(match) +\
                                  '<br>  Expect to find a number between 47.0% and 53.0%<br> '
    return p_test


def case_2(p_filename):
    import re
    from app.python_labs.io_test import io_test

    p_test = {"name": "Given 10000 sims, Atwood's dance party but no army taking over happens ~33% of the time"
                      " (10 points) <br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5> In 10,000 simulations, "
                              "dance party only happens ~33.0% of the time",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "In 10,000 simulations, did not find something around 33%.<br>"
                              "Check looks for a string that looks like this: '33%'"
                              "<br>Spacing and percent symbols matter! 100.0 % or 100.0 will fail.<br>",
              "points": 0,
              }
    test1 = io_test(p_filename, r'NO_MATCH', 1)
    match = re.findall(r'([0-9]+\.[0-9]+)%', test1['fail_message'], re.X | re.M | re.S)
    if match:
        for number in match:
            percent = float(number)
            print("aaaa percent " + str(percent))
            if 30.0 < percent < 36.0:
                p_test['points'] += 10
                p_test['pass'] = True
                break
    else:
        p_test['pass'] = False
    if p_test['pass'] is False:
        p_test['fail_message'] += 'Found these percentages ' + str(match) +\
                                  '<br>  Expect to find a number between 33.0% and 36.0%<br> '
    return p_test


def case_3(p_filename):
    import re
    from app.python_labs.io_test import io_test

    p_test = {"name": "Given 10000 sims, No Atwood's dance party BUT army taking over happens ~12% of the time"
                      " (10 points) <br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5> In 10,000 simulations, "
                              "no dance party, undead takeover happens ~12.0% of the time",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "In 10,000 simulations, did not find something around 12%.<br>"
                              "Check looks for a string that looks like this: '50%'"
                              "<br>Spacing and percent symbols matter! 100.0 % or 100.0 will fail.<br>",
              "points": 0,
              }
    test1 = io_test(p_filename, r'NO_MATCH', 1)
    match = re.findall(r'([0-9]+\.[0-9]+)%', test1['fail_message'], re.X | re.M | re.S)
    if match:
        for number in match:
            percent = float(number)
            print("aaaa percent " + str(percent))
            if 10.0 < percent < 13.0:
                p_test['points'] += 10
                p_test['pass'] = True
                break
    else:
        p_test['pass'] = False
    if p_test['pass'] is False:
        p_test['fail_message'] += 'Found these percentages ' + str(match) +\
                                  '<br>  Expect to find a number between 10.0% and 13.0%<br> '
    return p_test


def case_4(p_filename):
    import re
    from app.python_labs.io_test import io_test

    p_test = {"name": "Given 10000 sims, no Atwood's dance party AND  noarmy taking over happens ~6.25% of the time"
                      " (10 points) <br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5> In 10,000 simulations, "
                              "no dance party no undead takeover only happens ~6.25% of the time",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "In 10,000 simulations, did not find something around 6.25%.<br>"
                              "Check looks for a string that looks like this: '6.2%'"
                              "<br>Spacing and percent symbols matter! 100.0 % or 100.0 will fail.<br>",
              "points": 0,
              }
    test1 = io_test(p_filename, r'NO_MATCH', 1)
    match = re.findall(r'([0-9]+\.[0-9]+)%', test1['fail_message'], re.X | re.M | re.S)
    if match:
        for number in match:
            percent = float(number)
            print("aaaa percent " + str(percent))
            if 5.0 < percent < 7.0:
                p_test['points'] += 10
                p_test['pass'] = True
                break
    else:
        p_test['pass'] = False
    if p_test['pass'] is False:
        p_test['fail_message'] += 'Found these percentages ' + str(match) +\
                                  '<br>  Expect to find a number between 5.0% and 7.0%<br> '
    return p_test


