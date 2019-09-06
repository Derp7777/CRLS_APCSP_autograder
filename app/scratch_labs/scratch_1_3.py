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
    print("aaa asdfasdf {} ".format(p_scripts))
    test_pendown = match_string(r"\['event_whenkeypressed', \s* '0'] .+ 'pen_penDown'", p_scripts)
    if test_pendown['pass'] is False:
        p_test['fail_message'] += "Did not find a when 0 pressed followed by a pen erase all.<br>"
    test_clear = match_string(r"\['event_whenkeypressed', \s* '0'] .+ 'pen_clear'", p_scripts)
    if test_clear['pass'] is False:
        p_test['fail_message'] += "Did not find a when 0 pressed followed by an erase all.<br>"
    test_point = match_string(r"\['event_whenkeypressed', \s* '0'] .+ \['motion_pointindirection', \s '90'],",
                              p_scripts)
    if test_point['pass'] is False:
        p_test['fail_message'] += "Did not find a when 0 pressed followed by a point in direction 90.<br>"
    test_goto = match_string(r"\['event_whenkeypressed', \s* '0'] .+ \['motion_gotoxy', \s '0', \s '0'],",
                             p_scripts)
    if test_goto['pass'] is False:
        p_test['fail_message'] += "Did not find a when 0 pressed followed by goto 0 0 .<br>"
    if test_pendown['pass'] and test_clear['pass'] and test_point['pass'] and test_goto['pass']:
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
    test_two = match_string(r"'event_whenkeypressed',\s'1'", p_scripts)
    sprite = brickLayer(0, 0, 0, pendown=False)
    if test_two['pass'] is False:
        p_test['fail_message'] += "Did not find a 'when key 1 is pressed' in the code .<br>"
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
    if test_two['pass'] and square and move_success:
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
    test_two = match_string(r"'event_whenkeypressed',\s'2'", p_scripts)
    sprite = brickLayer(0, 0, 0, pendown=False)
    if test_two['pass'] is False:
        p_test['fail_message'] += "Did not find a 'when key 2 is pressed' in the code .<br>"
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
    if test_two['pass'] and equilateral and move_success:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def press_four(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch import match_string, unique_coordinates, is_pentagon
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite

    p_test = {"name": "Checking that there is a script that has 'when 4 key is pressed' that draws a pentagon"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a script that has 'when 4 key is pressed' that draws a "
                              "pentagon.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not a script that has 'when 4 key is pressed' that draws a "
                              "pentagon<br>",
              "points": 0
              }
    test_two = match_string(r"'event_whenkeypressed',\s'4'", p_scripts)
    sprite = brickLayer(0, 0, 0, pendown=False)
    if test_two['pass'] is False:
        p_test['fail_message'] += "Did not find a 'when key 4 is pressed' in the code .<br>"
    move_success = False
    if test_two['pass']:
        for key in p_scripts:
            script = p_scripts[key]
            if len(script) > 4:
                if script[0] == ['event_whenkeypressed', '4']:
                    move_success = do_sprite(sprite, script, True)
    coords = unique_coordinates(sprite.move_history)
    if len(coords) != 4:
        p_test['fail_message'] += "After pressing 1, sprite should land on 4 unique coordinates, but does not.<br>"
    pentagon = is_pentagon(coords)
    if pentagon is False:
        p_test['fail_message'] += "Failed test for pentagon <br>.<br>"
    if test_two['pass'] and pentagon and move_success:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def press_five(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch import match_string, unique_coordinates, is_parallelogram
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite

    p_test = {"name": "Checking that there is a script that has 'when 5 key is pressed' that draws a parallelogram"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a script that has 'when 5 key is pressed' that draws a "
                              "parallelogram.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not a script that has 'when 5 key is pressed' that draws a "
                              "parallelogram<br>",
              "points": 0
              }
    test_two = match_string(r"'event_whenkeypressed',\s'5'", p_scripts)
    sprite = brickLayer(0, 0, 0, pendown=False)
    if test_two['pass'] is False:
        p_test['fail_message'] += "Did not find a 'when key 5 is pressed' in the code .<br>"
    move_success = False
    if test_two['pass']:
        for key in p_scripts:
            script = p_scripts[key]
            if len(script) > 5:
                if script[0] == ['event_whenkeypressed', '5']:
                    move_success = do_sprite(sprite, script, True)
    coords = unique_coordinates(sprite.move_history)
    if len(coords) != 4:
        p_test['fail_message'] += "After pressing 1, sprite should land on 4 unique coordinates, but does not.<br>"
    parallelogram = is_parallelogram(coords)
    if parallelogram is False:
        p_test['fail_message'] += "Failed test for parallelogram <br>.<br>"
    if test_two['pass'] and parallelogram and move_success:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test
