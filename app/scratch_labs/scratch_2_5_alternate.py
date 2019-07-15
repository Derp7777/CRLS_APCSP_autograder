def test_prizes(p_json, p_points):
    from app.scratch_labs.scratch import find_variable
    p_test = {"name": "Testing that there are 4 variables named prize1, prize2, prize3, and prize4"
                      " (" + str(p_points) + " points).",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>"
                              " There are 4 variables named prize1, prize2, prize3, and prize4.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              " Does not appear that there are 4 variables named prize1, prize2, prize3, and prize4."
                              "<br>",
              'points': 0
              }
    test_prize1 = find_variable(p_json, 'prize1', 0)
    test_prize2 = find_variable(p_json, 'prize2', 0)
    test_prize3 = find_variable(p_json, 'prize3', 0)
    test_prize4 = find_variable(p_json, 'prize4', 0)
    if test_prize1['pass'] is False:
        test_prize1['fail_message'] += 'Did not find a variable called "prize1" in program.<br>'
    if test_prize2['pass'] is False:
        test_prize2['fail_message'] += 'Did not find a variable called "prize2" in program.<br>'
    if test_prize3['pass'] is False:
        test_prize3['fail_message'] += 'Did not find a variable called "prize3" in program.<br>'
    if test_prize4['pass'] is False:
        test_prize4['fail_message'] += 'Did not find a variable called "prize4" in program.<br>'
    if test_prize1['pass'] and test_prize2['pass'] and test_prize3['pass'] and test_prize4['pass']:
        p_test['points'] += p_points
        p_test['pass'] = True
    return p_test


def test_prizes_defined(p_scripts, p_points):
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Testing that 4 variables named prize1, prize2, prize3, and prize4 are set to values"
                      " (" + str(p_points) + " points).",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>"
                              " There are 4 variables named prize1, prize2, prize3, and prize4 are set to values. <br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              " Does not appear that there are variables named prize1, prize2, prize3, and prize4 that "
                              "are all set to values."
                              "<br>",
              'points': 0
              }
    test_one = match_string(r'data_setvariableto .+ VARIABLE_prize1\', \s* .+? [a-z] .+? ] ', p_scripts)
    if test_one['pass'] is False:
        p_test['fail_message'] += "Value for variable prize1 does not appear to be set.<br>"
    test_two = match_string(r'data_setvariableto .+ VARIABLE_prize2\', \s* .+? [a-z] .+? ] ', p_scripts)
    if test_two['pass'] is False:
        p_test['fail_message'] += "Value for variable prize2 does not appear to be set.<br>"
    test_three = match_string(r'data_setvariableto .+ VARIABLE_prize3\', \s* .+? [a-z] .+? ] ', p_scripts)
    if test_three['pass'] is False:
        p_test['fail_message'] += "Value for variable prize3 does not appear to be set.<br>"
    test_four = match_string(r'data_setvariableto .+ VARIABLE_prize4\', \s* .+? [a-z] .+? ] ', p_scripts)
    if test_four['pass'] is False:
        p_test['fail_message'] += "Value for variable prize4 does not appear to be set.<br>"
    if test_one['pass'] and test_two['pass'] and test_three['pass'] and test_four['pass']:
        p_test['points'] += p_points
        p_test['pass'] = True
    return p_test


def any_conditional(p_scripts, p_points):
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Testing that at least one prize works"
                      " (" + str(p_points) + " points).",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>"
                              " At least one prize works. <br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              " Does not appear that there at least one prize works.  You need an if, an 'equals' "
                              "operator, and a say."
                              "<br>",
              'points': 0
              }

    test = match_string(r'control_if .+? = .+? looks_say', p_scripts)
    if test['pass'] is False:
        p_test['fail_message'] += 'Looked for <br> control_if .+ = looks_say .+ inside this: <br>' + str(p_scripts)
    if test['pass']:
        p_test['points'] += p_points
        p_test['pass'] = True
    return p_test


def four_prizes(p_scripts, p_points):
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Testing that at all four prizes work"
                      " (" + str(p_points) + " points).",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>"
                              " At least all four prizes works. <br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              " Does not appear that all 4 prizes work.  You need an if, an 'equals' "
                              "operator, and a say for each prize."
                              "<br>",
              'points': 0
              }
    test_one = match_string(r"control_if .+ = .+ looks_say .+ VARIABLE_prize1 .+", p_scripts)
    test_two = match_string(r"control_if .+ = .+ looks_say .+ VARIABLE_prize2 .+", p_scripts)
    test_three = match_string(r"control_if .+ = .+ looks_say .+ VARIABLE_prize3 .+", p_scripts)
    test_four = match_string(r"control_if .+ = .+ looks_say .+ VARIABLE_prize4 .+", p_scripts)
    if test_one['pass'] is False:
        p_test['fail_message'] += "Did not appear that prize1 works."
    if test_two['pass'] is False:
        p_test['fail_message'] += "Did not appear that prize2 works."
    if test_three['pass'] is False:
        p_test['fail_message'] += "Did not appear that prize3 works."
    if test_four['pass'] is False:
        p_test['fail_message'] += "Did not appear that prize4 works."
    if test_one['pass'] and test_two['pass'] and test_three['pass'] and test_four['pass']:
        p_test['points'] += p_points
        p_test['pass'] = True
    return p_test


def no_if_if(p_scripts, p_points):
    import re
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Testing for efficiency (if if if is bad)"
                      " (" + str(p_points) + " points).",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>"
                              " Code is efficient (no if if if). <br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              " Code is not efficient (if if if). If you don't know why this is bad, ask the teacher."
                              "<br>",
              'points': 0
              }
    found = len(re.findall(r"'control_if'", str(p_scripts), re.X | re.M | re.S))
    if found >= 4 and found != 0:
        p_test['fail_message'] += "Too many ifs (or else there were none and you haven't gotten this far this yet)." \
                                  "  Found this many:<br>" \
                                  "Matches: " + str(found)
    else:
        p_test['points'] += p_points
        p_test['pass'] = True
    return p_test


def find_else(p_scripts, p_points):
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Testing that there is an else if you don't answer between 1-4"
                      " (" + str(p_points) + " points).",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>"
                              " There is an else if you don't answer between 1-4. <br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              " Does not appear that there is an else if you don't answer between 1-4.<br> "
                              "You pretty much need 5 if/else blocks to make this work."
                              "<br>",
              'points': 0
              }

    test = match_string(r"control_if .+ looks_say .+ VARIABLE_prize1 .+ \[\[ 'control_if .+ looks_say .+ "
                        r"VARIABLE_prize2 .+ \[\[ 'control_if .+ looks_say .+ VARIABLE_prize3 .+ "
                        r"\[\[ 'control_if .+ looks_say .+ VARIABLE_prize4 .+? looks_say", p_scripts)
    if test['pass'] is False:
        p_test['fail_message'] += r"Looked for <br> control_if .+ looks_say .+ VARIABLE_prize1 .+ \[\[ 'control_if .+ " \
                                  r"looks_say .+ VARIABLE_prize2 .+ \[\[ 'control_if .+ looks_say .+ VARIABLE_prize3 .+ " \
                                  r"\[\[ 'control_if .+ looks_say .+ VARIABLE_prize4 .+? looks_say <br> inside this:" \
                                  r" <br>" + str(p_scripts)
    if test['pass']:
        p_test['points'] += p_points
        p_test['pass'] = True
    return p_test
