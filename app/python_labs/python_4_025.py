def win_all(p_filename):
    import re
    from app.python_labs.io_test import io_test

    print("yes")
    p_test = {"name": "Given a win % of 1.0, Wimbledon win% should be 1.0 (15 points) <br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  Given a win% of 1.0, Serena always wins "
                              "Wimbledon",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Given a win% of 1.0, Serena does NOT always wins Wimbledon.<br>"
                              "Check looks for a string that looks like this: 'Serena won Wimbledon 100.0% of the time'"
                              "<br>Spacing and percent symbols matter! 100.0 % or 100.0 will fail.<br>",
              "points": 0,
              }
    test1 = io_test(p_filename, r'NO_MATCH', 1)
    match = re.search(r'([.0-9]+)%', test1['fail_message'], re.X | re.M | re.S)
    if match:
        print(str(match.group(0)) + " " + str(match.group(1)))
        percent = float(match.group(1))
        if percent > 101.0 or percent < 99.0:
            p_test['pass'] = False
        else:
            p_test['points'] += 15
    else:
        p_test['pass'] = False
    if p_test['pass'] is False:
        p_test['fail_message'] += 'Test found that Serena wins this percentage of matches: ' + str(percent) +\
                                  '<br>  Expect her to win between 101 and 99% of matches.<br>' \
                                  'Sometimes this error is because game is slightly broken.  Test it in isolation, ' \
                                  'it should give a win every single time if winning_percentage is 1.0.<br> '
    return p_test


def win_most(p_filename):
    import re
    from app.python_labs.io_test import io_test

    print("yes")
    p_test = {"name": "Given a win % of .75, Wimbledon win% should be .75 (15 points) <br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  Given a win% of .75 Serena wins around 75% of "
                              "Wimbledon",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Given a win% of .75, Serena does NOT win Wimbledon correct % of times.<br>"
                              "Check looks for a string that looks like this: 'Serena won Wimbledon 75.0% of the time'"
                              "<br>Spacing and percent symbols matter! 75.0 % or 75.0 will fail.<br>",
              "points": 0,
              }
    test1 = io_test(p_filename, r'NO_MATCH', 2)
    match = re.search(r'([.0-9]+)%', test1['fail_message'], re.X | re.M | re.S)
    if match:
        print(str(match.group(0)) + " " + str(match.group(1)))
        percent = float(match.group(1))
        if percent < 12.5 or percent > 14.5:
            p_test['pass'] = False
        else:
            p_test['points'] += 15
    else:
        p_test['pass'] = False
    if p_test['pass'] is False:
        p_test['fail_message'] += 'Test found that Serena wins this percentage of matches: ' + str(percent) +\
                                  '<br>  Expect her to win between 12.5 and 14.5% of matches.<br>'
    return p_test
