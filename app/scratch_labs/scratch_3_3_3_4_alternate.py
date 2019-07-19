def day_of_week_works(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string

    p_test = {"name": "Checking that the day_of_week custom block with one argument works"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "The day_of_week custom block with one argument works.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The day_of_week custom block with one argument does not appear to work."
                              "Is the input parameter named day?<br>"
                              "BE SURE INPUT PARAMETER IS NAMED day OTHERWISE THIS TEST BREAKS.<br>",
              "points": 0
              }
    if 'day_of_week %s' in p_scripts.keys():
        sprite = brickLayer(0, 0, 0, pendown=False, variables={"day": 1})
        script = p_scripts['day_of_week %s']
        day_success_1 = do_sprite(sprite, script, True)
        print("VALHALLA {}".format(sprite.say_history))
        test_1 = match_string(r'(sunday|Sunday|SUNDAY)', sprite.say_history)
        if test_1['pass'] is False:
            p_test['fail_message'] += "Didn't find the word 'sunday' or 'Sunday' or 'SUNDAY' " \
                                      "in say output when I called custom block day_of_week" \
                                      "with input parameter 1<br>"
        sprite = brickLayer(0, 0, 0, pendown=False, variables={"day": 5})
        script = p_scripts['day_of_week %s']
        day_success_2 = do_sprite(sprite, script, True)
        print("VALHALLA {}".format(sprite.say_history))
        test_2 = match_string(r'(friday|Friday|FRIDAY)', sprite.say_history)
        if test_2['pass'] is False:
            p_test['fail_message'] += "Didn't find the word 'friday', 'Friday', or 'FRIDAY' " \
                                      "in say output when I called custom block day_of_week" \
                                      "with input parameter 5<br>  Got back this: <br>" \
                                      + sprite.say_history
        if day_success_1 and day_success_2 and test_1['pass'] and test_2['pass']:
            p_test['pass'] = True
            p_test['points'] += p_points
    return p_test


def if_ifelse(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch import match_string

    p_test = {"name": "Checking that the day_of_week custom block with one argument has good use of if/ifelse"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "The day_of_week custom block with one argument has good use of if/ifelse.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The day_of_week custom block with one argument does not appear to have good use"
                              "of if/ifelse.<br>",
              "points": 0
              }
    if 'day_of_week %s' in p_scripts.keys():
        script = p_scripts['day_of_week %s']
        match_if = match_string(r"control_if'", script, num_matches=4)
        match_ifelse = match_string(r"control_if_else'", script, num_matches=4)

        if match_ifelse['pass'] is False:
            p_test['fail_message'] += 'Expect to see a bunch of if statements or if/else statements ' \
                                      'for this block to work.<br>'
        if match_if['pass']:
            p_test['fail_message'] += 'There are many if statements.  This block can be written more efficiently ' \
                                      'with if/elses.  Ask the teacher if this does not make sense.<br>'

        if match_if['pass'] is False and match_ifelse['pass'] is True:
            p_test['pass'] = True
            p_test['points'] += p_points
    return p_test


def find_day_of_week(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch import procedure_exists
    p_test = {"name": "Checking that there is a custom block called 'day_of_week' with one input parameter"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a custom block called 'day_of_week' with one input parameter named 'day'.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not a custom block called 'day_of_week' with one input parameter named 'day'."
                              "<br>"
                              "The script must be named EXACTLY day_of_week with exactly one input parameter named "
                              "'day'.<br>"
                              "Capitalization and using the underscore matter.<br>",
              "points": 0
              }
    test_procedure = procedure_exists('day_of_week %s', p_scripts)
    if test_procedure:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def find_min(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch import procedure_exists
    p_test = {"name": "Checking that there is a custom block called 'min' with two input parameters"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a custom block called 'min' with two input parameters named 'number1' and"
                              " 'number2'.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not a custom block called 'min' with two input parameters named 'number1' "
                              "and 'number2'."
                              "<br>"
                              "The script must be named EXACTLY 'min' with exactly two input parameters named "
                              "'number1' and 'number2'.<br>"
                              "Capitalization and using the underscore matter.<br>",
              "points": 0
              }
    test_procedure = procedure_exists('min %s %s', p_scripts)
    if test_procedure:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def min_works(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string

    p_test = {"name": "Checking that the day_of_week custom block with one argument works"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "The day_of_week custom block with one argument works.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The day_of_week custom block with one argument does not appear to work."
                              "Is the input parameter named day?<br>"
                              "BE SURE INPUT PARAMETER IS NAMED day OTHERWISE THIS TEST BREAKS.<br>",
              "points": 0
              }
    if 'day_of_week %s' in p_scripts.keys():
        sprite = brickLayer(0, 0, 0, pendown=False, variables={"number1": 5, "number2": 8})
        script = p_scripts['min %s %s']
        day_success_1 = do_sprite(sprite, script, True)
        print("VALHALLA {}".format(sprite.say_history))
        test_1 = match_string(r'5', sprite.say_history)
        if test_1['pass'] is False:
            p_test['fail_message'] += "Called custom block 'min' with number1 = 5 and number2 = 8" \
                                      "Expect back '5', got this:<br>" + sprite.say_history

        sprite = brickLayer(0, 0, 0, pendown=False, variables={"number1": 555, "number2": -8})
        script = p_scripts['min %s %s']
        day_success_2 = do_sprite(sprite, script, True)
        print("VALHALLA {}".format(sprite.say_history))
        test_2 = match_string(r'555', sprite.say_history)
        if test_2['pass'] is False:
            p_test['fail_message'] += "Called custom block 'min' with number1 = 555 and number2 = -8" \
                                      "Expect back '555', got this:<br>" + sprite.say_history
        if day_success_1 and day_success_2 and test_1['pass'] and test_2['pass']:
            p_test['pass'] = True
            p_test['points'] += p_points
    return p_test



def minif_ifelse(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch import match_string

    p_test = {"name": "Checking that the min custom block with two arguments has good use of if/ifelse"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "The the min custom block with two arguments has good use of if/ifelse.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The the min custom block with two arguments does not appear to have good use"
                              "of if/ifelse.<br>",
              "points": 0
              }
    if 'day_of_week %s' in p_scripts.keys():
        script = p_scripts['min %s %s']
        match_if = match_string(r"control_if'", script, num_matches=1)
        match_ifelse = match_string(r"control_if_else'", script, num_matches=1)

        if match_ifelse['pass'] is False:
            p_test['fail_message'] += 'Expect to see a if statements or if/else statements ' \
                                      'for this block to work.<br>'
        if match_if['pass']:
            p_test['fail_message'] += ' This block can be written more efficiently ' \
                                      'with if/else instead of if.  Ask the teacher if this does not make sense.<br>'

        if match_if['pass'] is False and match_ifelse['pass'] is True:
            p_test['pass'] = True
            p_test['points'] += p_points
    return p_test


def find_between(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch import procedure_exists
    p_test = {"name": "Checking that there is a custom block called 'between' with three input parameters"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a custom block called 'between' with three input parameters named 'number1' and"
                              " 'number2' and 'number3'.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not a custom block called 'between' with three input parameters named 'number1' "
                              "and 'number2' and 'number3'."
                              "<br>"
                              "The script must be named EXACTLY between with exactly three input parameters named "
                              "'number1' and 'number2' and 'number3'."
                              "Capitalization and using the underscore matter.<br>",
              "points": 0
              }
    test_procedure = procedure_exists('between %s %s %s', p_scripts)
    if test_procedure:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test
