import math

class brickLayer(object):
    def __init__(self, x, y, direction, *, draw_targets={}):
        self.x = x
        self.y = y
        self.direction = math.radians(direction)
        self.draw_targets = draw_targets
        self.penupdown = True

    def move(self, amount):
        print("start of move selfx {} selfy {} ".format(self.x, self.y))

        orig_x = self.x
        orig_y = self.y
        amount = int(amount)
        print(self.direction)
        self.y += round(math.cos(self.direction) * amount)
        self.x += round(math.sin(self.direction) * amount)
        print("enf of moveselfx {} selfy {} ".format(self.x, self.y))
        if ((orig_x, orig_y), (self.x, self.y)) in self.draw_targets.keys():
            self.draw_targets[((orig_x, orig_y), (self.x, self.y))] = 0
            return True
        elif ((self.x, self.y), (orig_x, orig_y) ) in self.draw_targets.keys():
            self.draw_targets[((self.x, self.y), (orig_x, orig_y))] = 0
            return True
        else:
            return False

    def turn(self, amount):
        self.direction += amount


def do_sprite(p_sprite, moves, success):
    """
    This function does the sprite movements
    :param p_sprite: The sprite object
    :param moves: moves sprite will try (list, looks like scripts in main code)
    :param success: What it returns  If false then exit right away
    :return: True/False depending on if crash or maximum fly exceeded.
    """
    if success is False:
        return False
    for i, move in enumerate(moves):
        if isinstance(move, list):
            do_sprite(p_sprite, moves[i], success)
        else:
            print("IN do-sprite selfx {} selfy {} dir {} ".format(p_sprite.x, p_sprite.y, p_sprite.direction))

            print("ggg move {}".format(move))
            if move == 'motion_movesteps':
                amount = moves[i+1]
                ret_val = p_sprite.move(amount)
                if ret_val is False:
                    success = False
                print("IN do-sprite after move selfx {} selfy {} dir {}".format(p_sprite.x, p_sprite.y,
                                                                                p_sprite.direction))

            elif move == 'motion_turnleft':
                degrees = float(moves[i+1])
                degrees = -math.radians(degrees)
                p_sprite.turn(degrees)
            elif move == 'motion_turnright':
                degrees = float(moves[i+1])
                degrees = math.radians(degrees)
                p_sprite.turn(degrees)


def press_zero(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch import match_string

    p_test = {"name": "Checking that there is a script that has 'when 0 key is pressed' along with a "
                      "pen down, goto -240 -180, clear, and point 90. (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "We found the strings in the code!<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Code does not find string we were looking for.<br>"
                              "Be sure that there is only one 'when 0 key is pressed'<br>",
              "points": 0
              }
    test_pendown = match_string(r"\['event_whenkeypressed', '0'] .+ 'pen_penDown'", p_scripts)
    if test_pendown is False:
        p_test['fail_message'] += "Did not find a when 0 pressed followed by a pen erase all.<br>"
    test_clear = match_string(r"\['event_whenkeypressed', '0'] .+ 'pen_clear'", p_scripts)
    if test_clear is False:
        p_test['fail_message'] += "Did not find a when 0 pressed followed by an erase all.<br>"
    test_point = match_string(r"\['event_whenkeypressed', '0'] .+ \['motion_pointindirection', \s '90'],",
                              p_scripts)
    if test_point is False:
        p_test['fail_message'] += "Did not find a when 0 pressed followed by a point in direction 90.<br>"
    test_goto = match_string(r"\['event_whenkeypressed', '0'] .+ \['motion_gotoxy', \s '-240', \s '-180'],",
                             p_scripts)
    if test_goto is False:
        p_test['fail_message'] += "Did not find a when 0 pressed followed by goto -240 -180.<br>"
    test_color = match_string(r"\['event_whenkeypressed', '0'] .+ \['pensetPenColorToColor'",
                              p_scripts)
    if test_color is False:
        p_test['fail_message'] += "Did not find a when 0 pressed followed by changing of pen color.<br>"
    if test_pendown and test_clear and test_point and test_goto and test_color:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def press_one(p_scripts, p_points):
    p_test = {"name": "Checking that press one draws a single brick (assuming 0 is pressed first) "
                      "" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Press one draws a single brick (assuming 0 is pressed first).<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Press one does NOT draw a single brick (assuming 0 is pressed first)<br>"
                              "Checker assumes you pressed 0 first, so you start in bottom left corner.<br>",
              "points": 0
              }
    target_list = (((0, 0), (40, 0)), ((40, 0), (40, 20)), ((40, 20), (0, 20)), ((0, 0), (0, 20)), )
    target_dict = {}
    for target in target_list:
        if target not in target_dict.keys():
            target_dict[target] = 1
    print(target_dict)
    sprite = brickLayer(0, 0, 90, draw_targets=target_dict)
    success = False
    for key in p_scripts:
        script = p_scripts[key]
        if script[0] == ['event_whenkeypressed', '1']:
            success = do_sprite(sprite, script, True)
            if success:
                break
    print("ggg sprite.x {} sprite.y {} dir {} targets {}".format(sprite.x, sprite.y, sprite.direction,
                                                                 sprite.draw_targets))
    if success:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test

