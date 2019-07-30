def press_zero(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch import match_string

    p_test = {"name": "Checking that there is a script that has 'when 0 key is pressed' along with a "
                      "pen down, goto 0 0, clear, and point 90. (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "We found the strings in the code!<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Code does not find string we were looking for.<br>"
                              "Be sure that there is only one 'when 0 key is pressed'<br>",
              "points": 0
              }
    test_pendown = match_string(r"\['event_whenkeypressed', '0'] .+ 'pen_penDown'", p_scripts)
    if test_pendown['pass'] is False:
        p_test['fail_message'] += "Did not find a when 0 pressed followed by a pen erase all.<br>"
    test_clear = match_string(r"\['event_whenkeypressed', '0'] .+ 'pen_clear'", p_scripts)
    if test_clear['pass'] is False:
        p_test['fail_message'] += "Did not find a when 0 pressed followed by an erase all.<br>"
    test_point = match_string(r"\['event_whenkeypressed', '0'] .+ \['motion_pointindirection', \s '90'],",
                              p_scripts)
    if test_point['pass'] is False:
        p_test['fail_message'] += "Did not find a when 0 pressed followed by a point in direction 90.<br>"
    test_goto = match_string(r"\['event_whenkeypressed', '0'] .+ \['motion_gotoxy', \s '0', \s '0'],",
                             p_scripts)
    if test_goto['pass'] is False:
        p_test['fail_message'] += "Did not find a when 0 pressed followed by goto 0 0.<br>"
    test_color = match_string(r"\['event_whenkeypressed', '0'] .+ \['pensetPenColorToColor'",
                              p_scripts)
    if test_color['pass'] is False:
        p_test['fail_message'] += "Did not find a when 0 pressed followed by changing of pen color.<br>"
    if test_pendown and test_clear and test_point and test_goto and test_color:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def press_one(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch import match_string, unique_coordinates, is_square
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite

    p_test = {"name": "Checking that there is a script that has 'when 1 key is pressed' that draws a square"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a script that has 'when 1 key is pressed' that draws a "
                              "square.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not a script that has 'when 1 key is pressed' that draws a "
                              "square<br>",
              "points": 0
              }
    test_repeat = match_string(r"'control_repeat',\s'4'", p_scripts)
    test_two = match_string(r"'event_whenkeypressed',\s'1'", p_scripts)
    sprite = brickLayer(0, 0, 0, pendown=False)
    if test_two['pass'] is False:
        p_test['fail_message'] += "Did not find a 'when key 1 is pressed' in the code .<br>"
    if test_repeat['pass'] is False:
        p_test['fail_message'] += "Did not find a repeat block that repeats the expected number of times.<br>"
    move_success = False
    if test_two['pass']:
        for key in p_scripts:
            script = p_scripts[key]
            if len(script) > 1:
                if script[0] == ['event_whenkeypressed', '1']:
                    move_success = do_sprite(sprite, script, True)
    coords = unique_coordinates(sprite.move_history)
    if len(coords) != 4:
        p_test['fail_message'] += "After pressing 1, sprite should land on 4 unique coordinates, but does not.<br>"
    square = is_square(coords)
    if square is False:
        p_test['fail_message'] += "Failed test for square <br>.<br>"
    if test_two['pass'] and test_repeat['pass'] and square and move_success:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def press_two(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch import match_string, unique_coordinates, is_equilateral_triangle
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite

    p_test = {"name": "Checking that there is a script that has 'when 2 key is pressed' that draws an "
                      "equilateral triangle. (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a script that has 'when 2 key is pressed' that draws an "
                              "equilateral triangle.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not a script that has 'when 2 key is pressed' that draws an "
                              "equilateral triangle.<br>",
              "points": 0
              }
    test_repeat = match_string(r"'control_repeat',\s'3'", p_scripts)
    test_two = match_string(r"'event_whenkeypressed',\s'2'", p_scripts)
    sprite = brickLayer(0, 0, 0, pendown=False)
    if test_two['pass'] is False:
        p_test['fail_message'] += "Did not find a 'when key 2 is pressed' in the code .<br>"
    if test_repeat['pass'] is False:
        p_test['fail_message'] += "Did not find a repeat block that repeats the expected number of times.<br>"
    move_success = False
    if test_two['pass']:
        for key in p_scripts:
            script = p_scripts[key]
            if len(script) > 1:
                if script[0] == ['event_whenkeypressed', '2']:
                    move_success = do_sprite(sprite, script, True)
    coords = unique_coordinates(sprite.move_history)
    if len(coords) != 3:
        p_test['fail_message'] += "After pressing 2, sprite should land on 3 unique coordinates, but does not.<br>"
    equilateral = is_equilateral_triangle(coords)
    if equilateral is False:
        p_test['fail_message'] += "Failed test for equilateral triangle (all sides equal length) <br>.<br>"
    if test_two['pass'] and test_repeat['pass'] and equilateral and move_success:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def find_make_triangle(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch import procedure_exists
    p_test = {"name": "Checking that there is a custom block called 'make_triangle' with one input parameter.  Input"
                      "parameter must be named 'size'."
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a custom block called 'make_triangle' with one input parameter.  "
                              "Input parameter must be named 'sized'.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not a custom block called 'make_triangle' with one input parameter."
                              "<br>"
                              "The script must be named EXACTLY make_triangle with exactly one input parameter.<br>"
                              "Input parameter must be named 'size'.<br>"
                              "Capitalization and using the underscore matter.<br>",
              "points": 0
              }
    test_procedure = procedure_exists('make_triangle %s', p_scripts)
    if test_procedure:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def make_triangle_works(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import unique_coordinates, is_equilateral_triangle, distance

    p_test = {"name": "Checking that the make_triangle custom block with one argument works"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "The make_triangle custom block with one argument works.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The make_triangle custom block with one argument does not appear to work."
                              "Is the input parameter named size?<br>"
                              "BE SURE INPUT PARAMETER IS NAMED SIZE OTHERWISE THIS TEST BREAKS.<br>",
              "points": 0
              }

    test_run_one = False
    test_run_two = False
    if 'make_triangle %s' in p_scripts.keys():
        sprite = brickLayer(0, 0, 0, pendown=False, variables={"size": 60})
        script = p_scripts['make_triangle %s']
        print("iii script {}".format(script))
        move_success_1 = do_sprite(sprite, script, True)
        coords = unique_coordinates(sprite.move_history)
        if len(coords) != 3:
            p_test['fail_message'] += "make_triangle custom block should land on 3 unique coordinates," \
                                      " but does not.<br>"
            return p_test
        equilateral = is_equilateral_triangle(coords)
        if equilateral is False:
            p_test['fail_message'] += "make_triangle custom block should create equilateral triangle but does not.<br>"
        first_move_distance = distance(sprite.move_history[0], sprite.move_history[1])
        if abs(60 - first_move_distance) > 60 * 0.01:
            p_test['fail_message'] += "Distance between first and second move should be around 60 steps if I call" \
                                      "block with input of 60. <br> Instead, it's " \
                                      "this distance:" + str(first_move_distance) + "<br>"
        else:
            test_run_one = True
        sprite = brickLayer(0, 0, 0, pendown=False, variables={"size": 100})
        script = p_scripts['make_triangle %s']
        move_success_2 = do_sprite(sprite, script, True)
        second_move_distance = distance(sprite.move_history[0], sprite.move_history[1])
        if abs(100 - second_move_distance) > 100 * 0.01:
            p_test['fail_message'] += "Distance between first and second move should be around 100 steps if I call" \
                                      "block with input of 100. <br> Instead, it's " \
                                      "this distance:" + str(second_move_distance) + "<br>"
        else:
            test_run_two = True
    else:
        p_test['fail_message'] += "Does not look like there is a custom block make_triangle with one input parameter."
    if move_success_1 and move_success_2 and equilateral and test_run_one and test_run_two:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def press_three(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that there is a script 'when 3 key is pressed' that calls make_triangle custom block "
                      "with one argument. (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a script 'when 3 key is pressed' that calls make_triangle custom block "
                              "with one argument.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not a script 'when 3 key is pressed' that calls make_triangle custom block "
                              "with one argument.<br>"
                              "The script must be named EXACTLY make_triangle with exactly one input parameter.<br>",
              "points": 0
              }
    test_three = match_string(r"'event_whenkeypressed', \s* '3'], \s* 'make_triangle \s* \%s'", p_scripts)

    if test_three['pass']:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def find_happy_birthday(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch import procedure_exists
    p_test = {"name": "Checking that there is a custom block called 'happy_birthday' with one input parameter"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a custom block called 'happy_birthday' with one input parameter.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not a custom block called 'happy_birthday' with one input parameter."
                              "<br>"
                              "The script must be named EXACTLY make_triangle with exactly one input parameter."
                              "Capitalization and using the underscore matter.<br>",
              "points": 0
              }
    test_procedure = procedure_exists('happy_birthday %s', p_scripts)
    if test_procedure:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def happy_birthday_works(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string

    p_test = {"name": "Checking that the happy_birthday custom block with one argument works"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "The happy_birthday custom block with one argument works.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The happy_birthday custom block with one argument does not appear to work."
                              "Is the input parameter named name?<br>"
                              "BE SURE INPUT PARAMETER IS NAMED name OTHERWISE THIS TEST BREAKS.<br>",
              "points": 0
              }
    if 'happy_birthday %s' in p_scripts.keys():
        sprite = brickLayer(0, 0, 0, pendown=False, variables={"name": 'McGlathery'})
        script = p_scripts['happy_birthday %s']
        word_success_1 = do_sprite(sprite, script, True)
        print("VALHALLA {}".format(sprite.say_history))
        test_1a = match_string(r'McGlathery', sprite.say_history)
        test_1b = match_string(r'(birthday|Birthday|BIRTHDAY)', sprite.say_history)
        if test_1a['pass'] is False:
            p_test['fail_message'] += "Didn't find the word 'McGlathery' in say output when I called custom block" \
                                      "with input parameter 'McGlathery'<br>"
        if test_1b['pass'] is False:
            p_test['fail_message'] += "Didn't find the word 'birthday', 'Birthday', or 'BIRTHDAY'" \
                                      " in say output when I called custom block" \
                                      "with input parameter 'McGlathery'<br>"
        sprite = brickLayer(0, 0, 0, pendown=False, variables={"name": 'MichaelJordan'})
        script = p_scripts['happy_birthday %s']
        word_success_2 = do_sprite(sprite, script, True)
        test_2a = match_string(r'MichaelJordan', sprite.say_history)
        test_2b = match_string(r'(birthday|Birthday|BIRTHDAY)', sprite.say_history)
        if test_2a['pass'] is False:
            p_test['fail_message'] += "Didn't find the word 'MichaelJordan' in say output when I called custom block " \
                                      "with input parameter 'MichaelJordan'<br>"
        if test_2b['pass'] is False:
            p_test['fail_message'] += "Didn't find the word 'birthday', 'Birthday', or 'BIRTHDAY' " \
                                      "in say output when I called custom block " \
                                      "with input parameter 'MichaelJordan'<br>"

        if word_success_1 and word_success_2 and test_1a['pass'] and test_1b['pass'] and test_2a['pass'] and \
                test_2b['pass']:
            p_test['pass'] = True
            p_test['points'] += p_points
    return p_test


def press_four(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that there is a script 'when 4 key is pressed' that calls happy birthday custom block "
                      "with one argument. (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a script 'when 4 key is pressed' that calls happy_birthday custom block "
                              "with one argument.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not a script 'when 4 key is pressed' that calls happy_birthday custom block "
                              "with one argument.<br>"
                              "The script must be named EXACTLY happy_birthday with exactly one input parameter.",
              "points": 0
              }
    test_four = match_string(r"'event_whenkeypressed', \s* '4'], \s* 'happy_birthday \s* \%s'", p_scripts)
    if test_four['pass']:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test
