def green_flag(p_scripts, p_points):
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Testing that there is a green flag.  The rest of your code should be under the green flag.<br>"
                      "There is also be a forever loop under the flag "
                      "(" + str(p_points) + " points)",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>"
                              "You have a green flag with a forever.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              "Did not find a green flag AND forever under it. <br>",
              'points': 0
              }
    test_flag = match_string(r'event_whenflagclicked', p_scripts)
    if test_flag['pass'] is False:
        p_test['fail_message'] += 'Did not find a green flag at all.'
    if test_flag['pass'] is False:
        p_test['fail_message'] += 'Did not find a green flag at all.'
    test_flag_and_forever = match_string(r'event_whenflagclicked .+ (control_repeat|control_forever)',
                                         p_scripts)
    if test_flag_and_forever['pass'] is False:
        p_test['fail_message'] += 'There needs to be a forever under the flag.'
    if test_flag['pass'] and test_flag_and_forever['pass']:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def test_top_1(p_scripts, p_points):
    from app.scratch_labs.scratch import match_string
    import re
    p_test = {"name": "Testing that sprite goes to top of screen at beginning "
                      "(" + str(p_points) + " points)",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>"
                              "Sprite goes to top of screen at beginning.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              "Sprite does NOT go to top of screen at beginning. <br>",
              'points': 0
              }
    test_flag_and_top = match_string(r'event_whenflagclicked .+ (motion_sety|motion_gotoxy)',
                                     p_scripts)
    if test_flag_and_top['pass'] is False:
        p_test['fail_message'] += 'There needs to be a block that moves the sprite to the top of the screen ' \
                                  'near the beginning of the script.'
    for key in p_scripts.keys():
        for block in p_scripts[key]:
            y = -300
            motion_sety = re.search(r"'motion_sety'", str(block), re.X | re.M | re.S)
            if motion_sety:
                test_high_enough = re.search(r"'motion_sety', \s+ '(-?[0-9]+)'", str(block), re.X | re.M | re.S)
                if test_high_enough:
                    y = test_high_enough.group(1)
                break
            motion_gotoxy = re.search(r"'motion_gotoxy'", str(block), re.X | re.M | re.S)
            if motion_gotoxy:
                motion_gotoxy = re.search(r"'operator_random'", str(block), re.X | re.M | re.S)
                if motion_gotoxy:
                    test_high_enough = re.search(r"'motion_gotoxy', \s+  \[\[ .+ ]],\s+ '([0-9]+)", str(block),
                                                 re.X | re.M | re.S)
                    if test_high_enough:
                        y = test_high_enough.group(1)
                        break
                else:
                    test_high_enough = re.search(r"motion_gotoxy', \s+ '-*[0-9]+', \s+ '([0-9]+)", str(block),
                                                 re.X | re.M | re.S)
                    if test_high_enough:
                        y = test_high_enough.group(1)
                        break
    if int(y) < 125:
        p_test['fail_message'] += 'Y position of sprite needs to be higher than 125.'
    if test_flag_and_top['pass'] and int(y) > 125:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def test_fall(p_scripts, p_points):
    import re
    p_test = {"name": "Testing that sprite falls "
                      "(" + str(p_points) + " points)",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>"
                              "Sprite falls.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              "Sprite does NOT appear to fall. <br>",
              'points': 0
              }
    falling = re.search(r"(control_repeat|control_forever) .+ motion_changeyby', \s '-[0-9]", str(p_scripts),
                        re.X | re.M | re.S)
    if falling:
        p_test['pass'] = True
        p_test['points'] += p_points
    else:
        p_test['fail_message'] += 'There needs to be a block inside a forever that makes the sprite fall.<br>'
    return p_test


def test_hit_ground(p_scripts, p_points):
    import re
    p_test = {"name": "Testing that sprite stops moving when it hits the ground "
                      "(" + str(p_points) + " points)",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>"
                              "Sprite stops falling when it hits the ground.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              "Sprite does NOT appear to stop falling when it hits the ground. <br>",
              'points': 0
              }
    not_touching_ground = re.search(r"(control_repeat|control_forever) .+ control_if .+ 'operator_not' .+ "
                                    r"'sensing_touchingobject' .+ 'sensing_touchingobjectmenu', \s* 'ground'",
                                    str(p_scripts),
                                    re.X | re.M | re.S)
    if_touching_ground_move_else_no_move = re.search(r"(control_repeat|control_forever) .+ control_if_else .+ "
                                                     r"'sensing_touchingobject' .+ 'sensing_touchingobjectmenu', "
                                                     r"\s* 'ground' .+? 'motion_changeyby',\s'0']], .+ "
                                                     r"'motion_changeyby',\s'-",
                                                     str(p_scripts),
                                                     re.X | re.M | re.S)
    repeat_until_touching = re.search(r"(control_repeat|control_forever) .+ control_repeat_until .+ "
                                      r"'sensing_touchingobject' .+ 'sensing_touchingobjectmenu', "
                                      r"\s* 'ground' .+? 'motion_changeyby',\s'-",
                                      str(p_scripts),
                                      re.X | re.M | re.S)
    if not_touching_ground is False:
        p_test['fail_message'] += 'Inside forever loop, if not touching ground move was not there.<br>'
    if if_touching_ground_move_else_no_move is False:
        p_test['fail_message'] += 'Inside forever loop if/else touching ground change y by 0, else move negative y ' \
                                  'was not there..<br>'
    if repeat_until_touching is False:
        p_test['fail_message'] += 'Inside forever loop repeat until touching move negative y was not there.<br>'
    if not_touching_ground or if_touching_ground_move_else_no_move or repeat_until_touching:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def test_random_x(p_scripts, p_points):
    import re
    p_test = {"name": "Testing that x coordinate is set randomly between -240 and 240 "
                      "(" + str(p_points) + " points)",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>"
                              "x coordinate is set randomly between -240 and 240.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              "x coordinate is not set randomly between -240 and 240. <br>"
                              "The range of x values must be between -240 and 240",
              'points': 0
              }
    gotoxy = re.search(r"'event_whenflagclicked' .+? 'motion_gotoxy', .+ 'operator_random', \s '-240', \s '240'",
                       str(p_scripts),
                       re.X | re.M | re.S)
    if gotoxy is False:
        p_test['fail_message'] += 'Looked for a random X between -240 and 240 in gotoxy block but did not find.<br>'
    setx = re.search(r"'event_whenflagclicked' .+? 'motion_setx', .+ 'operator_random', \s"
                     r" '-240', \s '240'",
                     str(p_scripts),
                     re.X | re.M | re.S)
    if setx is False:
        p_test['fail_message'] += 'Looked for a random X between -240 and 240 in setx block but did not find.<br>'
    if gotoxy or setx:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def platform_or_ground(p_scripts, p_points):
    import re
    p_test = {"name": "Testing that sprite stops when touching platform or ground "
                      "(" + str(p_points) + " points)",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>"
                              "There is a block that can test if sprite stops when touching platform or ground.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              "There is not a block that can est if sprite stops when touching platform or ground",
              'points': 0
              }
    match1 = re.search(r"sensing_touchingobject .+ sensing_touchingobjectmenu .+ ground .+ 'or', .+"
                       r"'sensing_touchingobject' .+ 'sensing_touchingobjectmenu .+ platform'",
                       str(p_scripts),
                       re.X | re.M | re.S)
    match2 = re.search(r"sensing_touchingobject .+ sensing_touchingobjectmenu .+ platform .+ 'or', .+"
                       r"'sensing_touchingobject' .+ 'sensing_touchingobjectmenu .+ platform'",
                       str(p_scripts),
                       re.X | re.M | re.S)
    if match1 or match2:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test
