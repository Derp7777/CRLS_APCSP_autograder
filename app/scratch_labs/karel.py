class robot(object):
    def __init__(self, x, y, direction, barriers, beepers, *, num_beepers=0):
        self.x = x
        self.y = y
        self.direction = direction
        self.barriers = barriers
        self.beepers = beepers
        self.num_beepers = num_beepers

    def front_is_clear(self):
        if self.direction == 0:
            proposed_square = [self.x, self.y + 5]
        elif self.direction == 1:
            proposed_square = [self.x + 5, self.y]
        elif self.direction == 2:
            proposed_square = [self.x, self.y - 5]
            if proposed_square[1] < 0:
                return False
        elif self.direction == 3:
            proposed_square = [self.x - 5, self.y]
        else:
            raise Exception("Direction can only be 0 - 3.  Direction is: " + str(self.direction))
        if proposed_square in self.barriers:
            return False
        else:
            return True

    def turnleft(self):
        self.direction = (self.direction + 3) % 4

    def move(self):
        if self.front_is_clear():
            if self.direction == 0:
                self.y += 10
            elif self.direction == 1:
                self.x += 10
            elif self.direction == 2:
                self.y -= 10
            elif self.direction == 3:
                self.x -= 10
            return True
        else:
            return False

    def pickbeeper(self):
        print("PICKING UP A BEEPER")
        coordinate = [self.x, self.y]
        print(f"coordinate {coordinate}, self beeters {self.beepers}")

        if coordinate in self.beepers:
            self.beepers.remove(coordinate)
            self.num_beepers += 1
            return True
        else:
            return False


def do_karel(p_karel, moves, success, *, max_fly=False, max_height=0):
    """
    This function does the karel movements
    :param p_karel: The Karel object
    :param moves: What it returns  If false then exit right away
    :param max_fly: Optional variable that checks to see if Karel is flying instead of jumping
    :param max_height: Maximum height to check if Karel is exceeding for 5 turns
    :return: True/False depending on if crash or maximum fly exceeded.
    """
    max_height_counter = 5
    if success is False:
        return False
    for i, move in enumerate(moves):
        if isinstance(move, list):
            # print(f"ooo LIST rerun the move {move}")
            do_karel(p_karel, moves[i], success)
        else:
            if move == 'move':
                print(f"max height {max_height_counter}")
                if max_fly:
                    if p_karel.y >= max_height:
                        max_height_counter -= 1
                    if max_height_counter == 0:
                        return False
                print("aaa move")
                if p_karel.move() is False:
                    success = False
                    break
            elif move == 'turnleft':
                print("aaa turnleft")

                p_karel.turnleft()
            elif move == 'pickbeeper':
                if p_karel.pickbeeper() is False:
                    success = False
                    break
                else:
                    print(f"PICKUP  up beeper {p_karel.num_beepers}")
            elif move == 'control_repeat':
                print("aaa control repeat")

                times = int(moves[i + 1])
                for _ in range(times):
                    print(f"ooo repeat time {_}")
                    do_karel(p_karel, moves[2], success)
                break
            elif move == 'control_repeat_until':
                print("aaa control repeat until")

                if(moves[i + 1][0] == 'frontIsClear' and moves[i + 1][1] == '=' and moves[i + 1][2] == 'True') or \
                        (moves[i + 1][0] == 'True' and moves[i + 1][1] == '=' and moves[i + 1][2] == 'frontIsClear'):
                    while p_karel.front_is_clear() is False:
                        print("checking front is clear")
                        print(f"sending this in {moves[2]}")
                        do_karel(p_karel, moves[2], success)
                        print("exiting")
                        if abs(p_karel.x) > 150 or abs(p_karel.y) > 150:
                            break
                elif (moves[i + 1][0] == 'frontIsClear' and moves[i + 1][1] == '=' and moves[i + 1][2] == 'False') or \
                        (moves[i + 1][0] == 'False' and moves[i + 1][1] == '=' and moves[i + 1][2] == 'frontIsClear'):
                    while p_karel.front_is_clear():
                        do_karel(p_karel, moves[2], success)
                        if abs(p_karel.x) > 150 or abs(p_karel.y) > 150:
                            break

                break
            elif move == 'control_if_else':
                print("aaa control ifelse")
                if (moves[i+1][0] == 'frontIsClear' and moves[i+1][1] == '=' and moves[i+1][2] == 'True') or\
                        (moves[i + 1][0] == 'True' and moves[i + 1][1] == '=' and moves[i + 1][2] == 'frontIsClear'):
                    if p_karel.front_is_clear():
                        do_karel(p_karel, moves[2], success)
                    else:
                        do_karel(p_karel, moves[3], success)
                elif (moves[i + 1][0] == 'frontIsClear' and moves[i + 1][1] == '=' and moves[i + 1][2] == 'False') or \
                        (moves[i + 1][0] == 'False' and moves[i + 1][1] == '=' and moves[i + 1][2] == 'frontIsClear'):
                    if p_karel.front_is_clear():
                        do_karel(p_karel, moves[3], success)
                    else:
                        do_karel(p_karel, moves[2], success)
                break
        print(f"at end position and direction end {p_karel.x} {p_karel.y} {p_karel.direction} ")
    return success


def karel1a(p_moves, p_points):
    barriers = [[20, 35], [25, 30], [25, 20], [30, 15], [40, 15], [50, 15], [55, 15],
                [55, 20], [55, 30], [55, 40], [55, 50], [50, 55], [40, 55], [30, 55],
                [25, 50], [20, 45],
                ]
    beepers = [[20, 20]]
    karel = robot(30, 20, 3, barriers, beepers)
    success = True
    print("BBB ABOUT TO START MOVING NOW!")
    karel_result = do_karel(karel, p_moves, success)
    p_test = {"name": "Testing that karel1 works (" + str(p_points) + " points) <br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>"
                              "Karel picked up beeper, and is back inside at same spot."
                              " <br> ",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5>  ",
              'points': 0
              }
    test_original_spot = False
    test_beeper = False
    if len(p_moves) > 3 and karel_result and karel.x == 30 and karel.y == 20:
        test_original_spot = True
        p_test['fail_message'] += "Karel was moved and  is now be back at its original spot (pass).<br>"
    else:
        p_test['fail_message'] += "Karel needs to have moved and now be back at its original spot (fail).<br>"
    if karel.num_beepers == 1:
        test_beeper = True
        p_test['fail_message'] += "Karel picked up the beeper and still has it (pass).<br>"
    else:
        p_test['fail_message'] += "Karel needs to have picked up a beeper and kept it but did not (fail).<br>"
    if test_original_spot is False or test_beeper is False:
        p_test['pass'] = False
    else:
        p_test['points'] += p_points
    print(f"x{karel.x} y {karel.y} beepers {karel.num_beepers}")
    print(f"success? {karel_result}")
    return p_test


def karel2a(p_moves, p_points):
    barriers = []
    beepers = [[20, 10], [30, 10], [40, 10], [50, 10], [60, 10],
               [20, 20], [30, 20], [40, 20], [50, 20], [60, 20],
               [20, 30], [30, 30], [40, 30], [50, 30], [60, 30],
               [20, 40], [30, 40], [40, 40], [50, 40], [60, 40],
               [20, 50], [30, 50], [40, 50], [50, 50], [60, 50],
               [20, 60], [30, 60], [40, 60], [50, 60], [60, 60], ]
    karel = robot(10, 10, 1, barriers, beepers)
    success = True
    karel_result = do_karel(karel, p_moves, success)
    p_test = {"name": "Testing that karel2 works (" + str(p_points) + " points) <br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>"
                              "Karel picked up all beepers."
                              " <br> ",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5>  ",
              'points': 0
              }
    if karel.num_beepers == 30:
        p_test['points'] += p_points
    else:
        p_test['pass'] = False
        p_test['fail_message'] += "Karel needed to pick up 30 beepers.  Karel picked up this many: <br>" \
                                  "" + str(karel.num_beepers)
    print(f"x{karel.x} y {karel.y} beepers {karel.num_beepers}")
    print(f"success? {karel_result}")
    return p_test


def karel2b(p_moves, p_points):
    barriers = []
    beepers = [[50, 10], [40, 20], [60, 20], [30, 30], [50, 30],
               [70, 30], [20, 40], [40, 40], [60, 40], [80, 40],
               [30, 50], [50, 50], [70, 50], [40, 60], [60, 60],
               [50, 70], ]
    karel = robot(50, 0, 0, barriers, beepers)
    success = True
    karel_result = do_karel(karel, p_moves, success)
    p_test = {"name": "Testing that karel2 works (" + str(p_points) + " points) <br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>"
                              "Karel picked up all beepers."
                              " <br> ",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5>  ",
              'points': 0
              }
    if karel.num_beepers == 16:
        p_test['points'] += p_points
    else:
        p_test['pass'] = False
        p_test['fail_message'] += "Karel needed to pick up 16 beepers.  Karel picked up this many: <br>" \
                                  "" + str(karel.num_beepers)
    print(f"x{karel.x} y {karel.y} beepers {karel.num_beepers}")
    print(f"success? {karel_result}")
    return p_test


def karel3a_1(p_moves, p_points):
    barriers = [[45, 0]]
    beepers = []
    karel = robot(0, 0, 1, barriers, beepers)
    success = True
    karel_result = do_karel(karel, p_moves, success, max_fly=True, max_height=10)
    p_test = {"name": "Testing that karel3a_1 works. One barrier at [4.5, 0] (" + str(p_points) + " points) <br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>"
                              "Karel made it to at least [9,0] without crashing."
                              " <br> ",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5>  ",
              'points': 0
              }
    if karel_result and karel.x >= 90 and karel.y == 0:
        p_test['points'] += p_points
    else:
        p_test['pass'] = False
        p_test['fail_message'] += "Karel needed to land on or past [9,0] without crashing, but did not<br>" \
                                  "Karel coordinates are<br>" \
                                  "X: " + str(karel.x) + "<br>" \
                                  "Y: " + str(karel.y) + "<br>"\
                                  "Karel is also not allowed to go above 10 height for 5 steps.<br>"

    print(f"success? {karel_result}")
    return p_test


def karel3a_2(p_moves, p_points):
    barriers = [[5, 0], [25, 0], [35, 0], [55, 0], [65, 0], ]
    beepers = []
    karel = robot(0, 0, 1, barriers, beepers)
    success = True
    karel_result = do_karel(karel, p_moves, success, max_fly=True, max_height=10)
    p_test = {"name": "Testing that karel3a_2 works.  Barriers at "
                      "[.5, 0], [2.5, 0], [3.5, 0], [5.5, 0], [6.5,0] (" + str(p_points) + " points) <br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>"
                              "Karel made it to at least [9,0] without crashing."
                              " <br> ",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5>  ",
              'points': 0
              }
    if karel_result and karel.x >= 90 and karel.y == 0:
        p_test['points'] += p_points
    else:
        p_test['pass'] = False
        p_test['fail_message'] += "Karel needed to land on or past [9,0] without crashing, but did not<br>" \
                                  "Karel coordinates at end of run are this:<br>" \
                                  "X: " + \
                                  str(karel.x) +\
                                  "<br>" \
                                  "Y: " + str(karel.y) + "<br>" \
                                  "Karel is also not allowed to go above 10 height for 5 steps.<br>"

    print(f"success? {karel_result}")
    return p_test


def karel3b_1(p_moves, p_points):
    barriers = [[15, 0], [25, 0], [35, 0], [45, 0], [45, 10], ]
    beepers = []
    karel = robot(0, 0, 1, barriers, beepers)
    success = True
    print("KAREL3B BARRIERS")
    print(barriers)
    karel_result = do_karel(karel, p_moves, success, max_fly=True, max_height=30)
    p_test = {"name": "Testing that karel3b_1 works. Barriers at [15, 0], [25, 0], [35, 0], [45, 0], [45, 10],"
                      " (" + str(p_points) + " points) <br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>"
                              "Karel made it to at least [9,0] without crashing."
                              " <br> ",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5>  ",
              'points': 0
              }
    if karel_result and karel.x >= 90 and karel.y == 0:
        p_test['points'] += p_points
    else:
        p_test['pass'] = False
        p_test['fail_message'] += "Karel needed to land on or past [9,0] without crashing, but did not<br>" \
                                  "Karel coordinates are<br>" \
                                  "X: " + str(karel.x) + "<br>" \
                                  "Y: " + str(karel.y) + "<br>" \
                                  "Karel is also not allowed to go above 30 height for 5 steps.<br>"

    print(f"success? {karel_result}")
    return p_test


def karel3b_2(p_moves, p_points):
    barriers = [[5, 0], [5, 10], [5, 20], [25, 0], [35, 0], [45, 0], [45, 10], [65, 0], [65, 10], [65, 20]]
    beepers = []
    karel = robot(0, 0, 1, barriers, beepers)
    success = True
    karel_result = do_karel(karel, p_moves, success, max_fly=True, max_height=30)
    p_test = {"name": "Testing that karel3b_2 works.  Barriers are [5, 0], [5, 10], [5, 20], [25, 0], [35, 0], [45, 0],"
                      " [45, 10], [65, 0], [65, 10], [65, 20] (" + str(p_points) + " points) <br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>"
                              "Karel made it to at least [9,0] without crashing."
                              " <br> ",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5>  ",
              'points': 0
              }
    if karel_result and karel.x >= 90 and karel.y == 0:
        p_test['points'] += p_points
    else:
        p_test['pass'] = False
        p_test['fail_message'] += "Karel needed to land on or past [9,0] without crashing, but did not<br>" \
                                  "Karel coordinates are<br>" \
                                  "X: " + str(karel.x) + "<br>" \
                                  "Y: " + str(karel.y) + "<br>" \
                                  "Karel is also not allowed to go above 30 height for 5 steps.<br>"

    print(f"success? {karel_result}")
    return p_test


def karel3c_1(p_moves, p_points):
    barriers = [[15, 0], [25, 0], [35, 0], [45, 0], [45, 10], [45, 20], [45, 30], [45, 40], [45, 50], ]
    beepers = []
    karel = robot(0, 0, 1, barriers, beepers)
    success = True
    karel_result = do_karel(karel, p_moves, success, max_fly=True, max_height=60)
    p_test = {"name": "Testing that karel3c_1 works. Barriers at [15, 0], [25, 0], [35, 0], [45, 0], [45, 10], "
                      "[45, 20], [45, 30], [45, 40], [45, 50] "
                      " (" + str(p_points) + " points) <br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>"
                              "Karel made it to at least [9,0] without crashing."
                              " <br> ",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5>  ",
              'points': 0
              }
    if karel_result and karel.x >= 90 and karel.y == 0:
        p_test['points'] += p_points
    else:
        p_test['pass'] = False
        p_test['fail_message'] += "Karel needed to land on or past [9,0] without crashing, but did not<br>" \
                                  "Karel coordinates are<br>" \
                                  "X: " + str(karel.x) + "<br>" \
                                  "Y: " + str(karel.y) + "<br>" \
                                  "Karel is also not allowed to go above 60 height for 5 steps.<br>"

    print(f"success? {karel_result}")
    return p_test


def karel3c_2(p_moves, p_points):
    barriers = [[5, 0], [5, 10], [5, 20], [5, 30], [5, 40], [5, 50], [5, 60],
                [25, 0], [35, 0], [45, 0], [45, 10], [45, 20], [45, 30], [45, 40], [45, 50], [45, 60],
                [65, 0], [65, 10], [65, 20]]
    beepers = []
    karel = robot(0, 0, 1, barriers, beepers)
    success = True
    karel_result = do_karel(karel, p_moves, success,  max_fly=True, max_height=70)
    p_test = {"name": "Testing that karel3c_2 works.  Barriers are [5, 0], [5, 10], [5, 20],  [5, 30],"
                      " [5, 40], [5, 50],"
                      " [5, 60], [25, 0], [35, 0], [45, 0],"
                      " [45, 10],  [45, 20], [45, 30], [45, 40], [45, 50], [45, 60], "
                      "[65, 0], [65, 10], [65, 20] (" + str(p_points) + " points) <br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>"
                              "Karel made it to at least [9,0] without crashing."
                              " <br> ",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5>  ",
              'points': 0
              }
    if karel_result and karel.x >= 90 and karel.y == 0:
        p_test['points'] += p_points
    else:
        p_test['pass'] = False
        p_test['fail_message'] += "Karel needed to land on or past [9,0] without crashing, but did not<br>" \
                                  "Karel coordinates are<br>" \
                                  "X: " + str(karel.x) + "<br>" \
                                  "Y: " + str(karel.y) + "<br>" \
                                  "Karel is also not allowed to go above 70 height for 5 steps.<br>"

    print(f"success? {karel_result}")
    return p_test


def karel3d_1(p_moves, p_points):
    barriers = [[15, 0], [25, 0], [35, 0], [45, 0], [45, 10], [45, 20], [45, 30], [45, 40], [45, 50], [50, 55],
                [60, 55], [70, 55], [75, 50], [75, 40], [75, 30], [75, 20], [75, 10], [75, 0], ]
    beepers = []
    karel = robot(0, 0, 1, barriers, beepers)
    success = True
    print("WTF BARRIERS")
    print(barriers)
    karel_result = do_karel(karel, p_moves, success)
    p_test = {"name": "Testing that karel3d_1 works. Barriers at [15, 0], [25, 0], [35, 0], [45, 0], [45, 10], "
                      "[45, 20], [45, 30], [45, 40], [45, 50], [50, 55], [60, 55], [70, 55], [75, 50], [75, 40], "
                      "[75, 30], [75, 20], [75, 10], [75, 0],   "
                      " (" + str(p_points) + " points) <br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>"
                              "Karel made it to at least [9,0] without crashing."
                              " <br> ",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5>  ",
              'points': 0
              }
    if karel_result and karel.x >= 90 and karel.y == 0:
        p_test['points'] += p_points
    else:
        p_test['pass'] = False
        p_test['fail_message'] += "Karel needed to land on or past [9,0] without crashing, but did not<br>" \
                                  "Karel coordinates are<br>" \
                                  "X: " + str(karel.x) + "<br>" \
                                  "Y: " + str(karel.y) + "<br>"

    print(f"success? {karel_result}")
    return p_test


def karel3d_2(p_moves, p_points):
    barriers = [[15, 0], [25, 0], [30, 5], [40, 5], [50, 5], [60, 5], [70, 5], [75, 0], ]
    beepers = []
    karel = robot(0, 0, 1, barriers, beepers)
    success = True
    karel_result = do_karel(karel, p_moves, success)
    p_test = {"name": "Testing that karel3b_2 works.  Barriers are [15, 0], [25, 0], [30, 5], [40, 5],"
                      " [50, 5], [60, 5], [70, 5], [75, 0], (" + str(p_points) + " points) <br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>"
                              "Karel made it to at least [9,0] without crashing."
                              " <br> ",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5>  ",
              'points': 0
              }
    if karel_result and karel.x >= 90 and karel.y == 0:
        p_test['points'] += p_points
    else:
        p_test['pass'] = False
        p_test['fail_message'] += "Karel needed to land on or past [9,0] without crashing, but did not<br>" \
                                  "Karel coordinates are<br>" \
                                  "X: " + str(karel.x) + "<br>" \
                                  "Y: " + str(karel.y) + "<br>"

    print(f"success? {karel_result}")
    return p_test


def karel_final_spot(p_moves, p_points):
    barriers = [[5, 0], [25, 0], [35, 0], [55, 0], [65, 0], ]
    beepers = []
    karel = robot(0, 0, 1, barriers, beepers)
    success = True
    karel_result = do_karel(karel, p_moves, success)
    p_test = {"name": "Testing that Karel finishes at [9,0] (" + str(p_points) + " points) <br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>"
                              "Karel finishes at [9,0]."
                              " <br> ",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5>  ",
              'points': 0
              }
    if karel_result and karel.x == 90 and karel.y == 0:
        p_test['points'] += p_points
    else:
        p_test['pass'] = False
        p_test['fail_message'] += "Karel needed to land on [9,0] without crashing, but did not<br>" \
                                  "Karel coordinates at end of run are this:<br>" \
                                  "X: " + str(karel.x/10) + "<br>" \
                                                            "Y: " + str(karel.y/10) + "<br>"

    print(f"success? {karel_result}")
    return p_test


def _check_block(p_main_script, p_repeat_blocks, p_blocks):
    """
    Loops over main script
     (something like  ['move', 'move', 'turnleft', 'turnright', '}3^M_-;zNA]20=x3PXv#'])  (list)
    and looks for repeat blocks something like
    }3^M_-;zNA]20=x3PXv#   ['move', 'move', 'turnleft', ']!2m_%;@FCB^?cJ3*gi+'] (dictionary)
    Because it's a list, just modifies it in place.
    :param p_main_script:
    :param p_repeat_blocks:
    :return: NONE
    """
    for i, item in enumerate(p_main_script):
        for key in p_repeat_blocks:
            if item == key:
                opcode = p_blocks[key]['opcode']
                if opcode == 'control_repeat':
                    times = p_blocks[key]['inputs']['TIMES'][1][1]
                    print("aaa TIMES HERE {} ".format(times))

                    p_main_script[i] = ['control_repeat', times, p_repeat_blocks[key]]
                else:
                    p_main_script[i] = p_repeat_blocks[key]


def simplify_blocks(p_main_script, p_repeat_blocks, p_blocks):
    """
    takes the main block and substitutes in what's in the repeat
    :param p_main_script:  main block
    (something like  ['move', 'move', 'turnleft', 'turnright', '}3^M_-;zNA]20=x3PXv#'])  (list)
    :param p_repeat_blocks: something like
    }3^M_-;zNA]20=x3PXv#   ['move', 'move', 'turnleft', ']!2m_%;@FCB^?cJ3*gi+'] (dictionary)
    :param p_blocks:coder blocks
    :return: whatever the heck recursion returns
    """
    _check_block(p_main_script, p_repeat_blocks, p_blocks)
    for i, item in enumerate(p_main_script):
        if isinstance(item, list):
            p_main_script[i] = simplify_blocks(p_main_script[i], p_repeat_blocks, p_blocks)
        else:
            continue
    return p_main_script


def _sub_user_blocks_helper(p_main_script, p_user_blocks):
    """
    Helper script for sub_user_blocks.  Checks main script for user blocks
    :param p_main_script: (something like  ['move', 'move', 'turnleft', 'turnright', ])  (list)
    :param p_user_blocks: something like
    {'turnright' : ['turnleft', 'turnleft', 'turnleft']} (dictionary)
    :return:
    """
    for i, item in enumerate(p_main_script):
        for key in p_user_blocks:
            if item == key:
                p_main_script[i] = p_user_blocks[key]


def sub_user_blocks(p_main_script, p_user_blocks, p_blocks):
    """
    Similar to simplify_blocks, except with user scripts (like turnright)
    :param p_main_script:  main block
    (something like  ['move', 'move', 'turnleft', 'turnright'])  (list)
    :param p_user_blocks: something like
    {'turnright' : ['turnleft', 'turnleft', 'turnleft']} (dictionary)
    :param p_blocks:coder blocks
    :return: p_main_script
    """
    _sub_user_blocks_helper(p_main_script, p_user_blocks)
    for i, item in enumerate(p_main_script):
        if isinstance(item, list):
            p_main_script[i] = sub_user_blocks(p_main_script[i], p_user_blocks, p_blocks)
        else:
            continue
    return p_main_script


def _sub_dict_into_list_helper(p_list, p_dict, p_blocks):
    """
    Helper script for sub_dict_into_list.  Checks main script for user blocks
    :param p_list: (something like  ['move', 'move', 'turnleft', 'turnright', ])  (list)
    :param p_dict: something like
    {'turnright' : ['turnleft', 'turnleft', 'turnleft']} (dictionary)
    :param p_blocks:coder blocks
    :return:
    """

    from copy import deepcopy
    p_dict = deepcopy(p_dict)
    for i, item in enumerate(p_list):
        for key in p_dict:
            if isinstance(item, str):
                if item == key:
                    opcode = p_blocks[item]['opcode']
                    if opcode == 'control_repeat':
                        times = p_blocks[item]['inputs']['TIMES'][1][1]
                        p_list[i] = [['control_repeat', times, p_dict[key][0]]]
                        if len(p_dict[key]) > 1:
                            p_list[i].extend(p_dict[key][1:])
                    elif opcode == 'control_repeat_until':
                        print("YOOO!!!!")
                        print(item)
                        substack_id = p_blocks[item]['inputs']['SUBSTACK'][1]
                        condition_id = p_blocks[item]['inputs']['CONDITION'][1]
                        # print(f"AAA SUBSTACK ID {substack_id}")
                        # print(f"AAA CONDITION ID {condition_id}")


                        #p_dict_subbed[key][i] = ['control_repeat_until', condition_id, substack_id]
                    else:
                        p_list[i] = p_dict[key]
    return p_list


def sub_dict_into_list(p_list, p_dict, p_blocks):
    """
    Similar to simplify_blocks, except with user scripts (like turnright)
    :param p_list:  main block
    (something like  ['move', 'move', 'turnleft', 'turnright'])  (list)
    :param p_dict: something like
    {'turnright' : ['turnleft', 'turnleft', 'turnleft']} (dictionary)
    :param p_blocks:coder blocks
    :return: p_list
    """
    for i, item in enumerate(p_list):
        if isinstance(item, list):
            p_list[i] = sub_dict_into_list(p_list[i], p_dict, p_blocks)
        else:
            _sub_dict_into_list_helper(p_list, p_dict, p_blocks)
    return p_list


def _sub_dict_into_dict_helper(p_dict_subbed, p_dict_subber, p_blocks):
    """
    Helper script for sub_user_blocks.  Checks user scripts for repeat scripts
    Similar to simplify_blocks, except with user scripts (like turnright)
    :param p_dict_subbed:  user_scripts
    (something like  {'turnright':['turnleft', 'turnleft', 'turnleft'],
                      'getrow' :['=sQ`qkS%jV2Vq.QeMW@d']} (ldictionaries)
    :param p_dict_subber: something like
    {'=sQ`qkS%jV2Vq.QeMW@d' = '['move', 'pickbeeper']'} (dictionary)
    where I am subbing the value of '=sQ`qkS%jV2Vq.QeMW@d' into getrow
    :param p_blocks:coder blocks
    :return: a VALUE to sub in
    """
    from copy import deepcopy
    p_dict_subber = deepcopy(p_dict_subber)
    for key in p_dict_subbed:
        for i, item in enumerate(p_dict_subbed[key]):
            if isinstance(item, str):
                if item in p_dict_subber.keys():
                    opcode = p_blocks[item]['opcode']
                    if opcode == 'control_repeat' or opcode == 'control_forever':
                        if opcode == 'control_forever':
                            times = 150
                        else:
                            times = p_blocks[item]['inputs']['TIMES'][1][1]
                        p_dict_subbed[key][i] = ['control_repeat', times, p_dict_subber[item]]
                    elif opcode == 'control_repeat_until':

                        substack_id = p_blocks[item]['inputs']['SUBSTACK'][1]
                        condition_id = p_blocks[item]['inputs']['CONDITION'][1]
                        # print(f"AAA SUBSTACK ID {substack_id}")
                        # print(f"AAA CONDITION ID {condition_id}")
                        # repeat_script = build_karel_script(substack_id, p_target)
                        # condition_script = build_karel_script(condition_id, p_target)
                        # script.append(['control_repeat_until', condition_script, repea

                        p_dict_subbed[key][i] = ['control_repeat_until', condition_id, substack_id]
                    else:
                        p_dict_subbed[key][i] = p_dict_subber[item]
    return p_dict_subbed[key]


def sub_dict_into_dict(p_dict_subbed, p_dict_subber, p_blocks):
    """
    Similar to simplify_blocks, except with user scripts (like turnright)
    :param p_dict_subbed:  something like user_scripts
    (something like  {'turnright':['turnleft', 'turnleft', 'turnleft'],
                      'getrow' :['=sQ`qkS%jV2Vq.QeMW@d']} (ldictionaries)
    :param p_dict_subber: something like
    {'=sQ`qkS%jV2Vq.QeMW@d' = '['move', 'pickbeeper']'} (dictionary)
    where I am subbing the value of '=sQ`qkS%jV2Vq.QeMW@d' into getrow
    :param p_blocks:coder blocks
    :return: p_dict_subbed
    """
    _sub_dict_into_dict_helper(p_dict_subbed, p_dict_subber, p_blocks)
    for key in p_dict_subbed:
        print(f"aaa simplify this key: {key}")
        print(f"aaa enumerate {p_dict_subbed[key]} type  {type(p_dict_subbed[key])}")
        for i, item in enumerate(p_dict_subbed[key]):
            if isinstance(item, list):
                if p_dict_subbed[key][i][0] == 'control_repeat' or p_dict_subbed[key][i][0] == 'control_forever'\
                        or p_dict_subbed[key][i][0] == 'control_repeat_until':
                    p_dict_subbed[key][i][2] = sub_dict_into_list(p_dict_subbed[key][i][2], p_dict_subber,
                                                                  p_blocks)
                else:
                    p_dict_subbed[key][i] = sub_dict_into_dict(p_dict_subbed[key][i],
                                                               p_dict_subber, p_blocks)
            else:
                continue
    return p_dict_subbed


def _order_procedure_blocks(starting_block_id, p_target):
    """
    Called by arrange_blocks, to traverse a scratch procedure json, finding sequential blocks until it hits the end
    for blocks, two checks = there is a substack or there is a next (or both)
    :param starting_block_id: Key of the block with which o start the script
    :param p_target: json info for block that is starting the script   the script
    """

    # I didn't change the other script at all.  I think the change comes in clean
    temp_block = p_target['blocks'][starting_block_id]
    temp_block['ID'] = starting_block_id  # #stick the ID onto the dictionary
    script = [temp_block]
    current_block_id = starting_block_id
    if 'mutation' in p_target['blocks'][starting_block_id].keys():
        print(f"current block info {p_target['blocks'][starting_block_id]['mutation']['proccode']}")
    next_block_id = p_target['blocks'][current_block_id]['next']
    while next_block_id is not None:
        temp_block = p_target['blocks'][next_block_id]
        temp_block['ID'] = next_block_id  # #stick the ID onto the dictionary
        script.append(temp_block)
        current_block_id = next_block_id
        next_block_id = p_target['blocks'][current_block_id]['next']
    return script


def build_karel_script(starting_block_id, p_target):
    temp_block = p_target['blocks'][starting_block_id]
    temp_block['ID'] = starting_block_id
    current_block_id = starting_block_id
    next_block_id = "continue"
    script = []
    while next_block_id is not None:
        if p_target['blocks'][current_block_id]['opcode'] == 'control_repeat' or \
                p_target['blocks'][current_block_id]['opcode'] == 'control_forever':
            substack_id = p_target['blocks'][current_block_id]['inputs']['SUBSTACK'][1]
            repeat_script = build_karel_script(substack_id, p_target)
            if p_target['blocks'][current_block_id]['opcode'] == 'control_forever':
                times = 150
            else:
                times = p_target['blocks'][current_block_id]['inputs']['TIMES'][1][1]
            script.append(['control_repeat', times, repeat_script])
        elif p_target['blocks'][current_block_id]['opcode'] == 'procedures_call':
            script.append(p_target['blocks'][current_block_id]['mutation']['proccode'])
        elif p_target['blocks'][current_block_id]['opcode'] == 'control_if_else':
            substack_1_id = p_target['blocks'][current_block_id]['inputs']['SUBSTACK'][1]
            substack_2_id = p_target['blocks'][current_block_id]['inputs']['SUBSTACK2'][1]
            condition_id = p_target['blocks'][current_block_id]['inputs']['CONDITION'][1]
            if_script = build_karel_script(substack_1_id, p_target)
            else_script = build_karel_script(substack_2_id, p_target)
            condition_script = build_karel_script(condition_id, p_target)
            script.append(['control_if_else', condition_script, if_script, else_script])
        elif p_target['blocks'][current_block_id]['opcode'] == 'control_repeat_until':
            substack_id = p_target['blocks'][current_block_id]['inputs']['SUBSTACK'][1]
            condition_id = p_target['blocks'][current_block_id]['inputs']['CONDITION'][1]
            repeat_script = build_karel_script(substack_id, p_target)
            condition_script = build_karel_script(condition_id, p_target)
            script.append(['control_repeat_until', condition_script, repeat_script])
        elif p_target['blocks'][current_block_id]['opcode'] == 'operator_equals':
            operand1 = p_target['blocks'][current_block_id]['inputs']['OPERAND1'][1][1]
            operand2 = p_target['blocks'][current_block_id]['inputs']['OPERAND2'][1][1]
            script = [operand1, '=', operand2]
        next_block_id = p_target['blocks'][current_block_id]['next']
        current_block_id = next_block_id
    return script


def arrange_karel_blocks(p_json):
    """
    Looks for a particular script in the code.  Algorithms:
    1. Find all the parents and populate new dictionary.
    2. Keys are keys of the parents.  Values are lists, each item is a block starting at the top of the tree.
    3. Look for "next" key and add that to the value list.

    :param p_json: json info for the coder block usually
    :return: scripts - dictionary of scripts.  Keys are block ID's of parent.  values are lists of individual blocks
    under the parent
    """
    from copy import deepcopy

    scripts = {}
    given_blocks = ['move', 'turnleft', 'pickbeeper', 'putbeeper', 'turnoff', ]
    user_blocks = {}
    main_script = []
    repeat_scripts = {}
    if_scripts = {}
    operator_scripts = {}
    for target in p_json['targets']:
        if target['blocks']:
            for block_id in target['blocks']:
                if 'opcode' in target['blocks'][block_id]:
                    if target['blocks'][block_id]['opcode'] == "procedures_prototype":  # Get the procedures
                        if target['blocks'][block_id]['mutation']['proccode'] not in given_blocks:
                            parent_id = target['blocks'][block_id]['parent']   # get the procedures_definition
                            block_start_id = target['blocks'][parent_id]['next']  # get the actual first thing
                            script = _order_procedure_blocks(block_start_id, target)
                            cleaned_custom_block = []
                            for item in script:
                                if 'mutation' in item.keys():
                                    cleaned_custom_block.append(item['mutation']['proccode'])
                                elif 'inputs' in item.keys():
                                    if 'SUBSTACK' in item['inputs'].keys():
                                        cleaned_custom_block.append(item['ID'])
                            user_blocks[target['blocks'][block_id]['mutation']['proccode']] = cleaned_custom_block

                    if target['blocks'][block_id]['opcode'] == "control_repeat" or \
                            target['blocks'][block_id]['opcode'] == "control_forever" or \
                            target['blocks'][block_id]['opcode'] == "control_repeat_until":
                        print(f"yyy {block_id} doing repeat now.   ")
                        if 'inputs' in target['blocks'][block_id]:
                            if 'SUBSTACK' in target['blocks'][block_id]['inputs']:
                                repeat_scripts[block_id] = [target['blocks'][block_id]['inputs']['SUBSTACK'][1]]
                    if target['blocks'][block_id]['opcode'] == "operator_equals":
                        print(f"yyy {block_id} doing operator equal now.   ")
                        if 'inputs' in target['blocks'][block_id]:
                            if 'OPERAND1' in target['blocks'][block_id]['inputs']:
                                operator_scripts[block_id] = [target['blocks'][block_id]['inputs']['OPERAND1'][1][1],
                                                              '=',
                                                              target['blocks'][block_id]['inputs']['OPERAND2'][1][1]]
                    if target['blocks'][block_id]['opcode'] == "control_if_else":
                        print(f"yyy {block_id} doing if/else now.   ")
                        if 'inputs' in target['blocks'][block_id]:
                            if 'SUBSTACK' in target['blocks'][block_id]['inputs']:
                                if_scripts[block_id] = [target['blocks'][block_id]['inputs']['CONDITION'][1],
                                                        target['blocks'][block_id]['inputs']['SUBSTACK'][1],
                                                        target['blocks'][block_id]['inputs']['SUBSTACK2'][1]]
                    elif 'parent' in target['blocks'][block_id]:
                        if target['blocks'][block_id]['parent'] is not None:
                            parent_id = target['blocks'][block_id]['parent']
                            print(f"yyy {block_id} doing repeat substacks now .")
                            if target['blocks'][parent_id]['inputs']:
                                if 'SUBSTACK' in target['blocks'][parent_id]['inputs']:
                                    print("yyy maybe it's a repeat block with a parent")
                                    if target['blocks'][parent_id]['inputs']['SUBSTACK'][1] == block_id:
                                        script = _order_procedure_blocks(block_id, target)
                                        temp_repeat_commands = []
                                        for item in script:
                                            if item['opcode'] == 'event_whenbroadcastreceived' or \
                                                    item['opcode'] == 'data_setvariableto':
                                                pass
                                            elif 'mutation' in item.keys():
                                                temp_repeat_commands.append(item['mutation']['proccode'])
                                            else:
                                                temp_repeat_commands.append(item['inputs']['SUBSTACK'][1])
                                        repeat_scripts[block_id] = temp_repeat_commands
                    if target['blocks'][block_id]['opcode'] == "procedures_definition":  # can skip, previous if does
                        # print("yyy this is procedure defintion skip")
                        pass
                    elif target['blocks'][block_id]['opcode'] == "data_setvariableto":  # Get the start
                        print("A NEW BEGINNING")
                        main_script = build_karel_script(block_id, target)
                        print("THIS IS THE MAIN SCRIPT MAYBE")
                        print(main_script)

    user_blocks_orig = deepcopy(user_blocks)
    print(f"repeat blocks pre simplification of repeat ")
    for key in repeat_scripts:
        print(f"key {key} block {repeat_scripts[key]}")
    print(f"user blocks pre simplification os user BLOCKS")
    for key in user_blocks:
        print(f"key {key} block {user_blocks[key]}")
    replace_items = True
    print(f"OPERATOR scripts")
    for key in operator_scripts:
        print(f"key {key} block {operator_scripts[key]}")
    user_blocks_string = str(user_blocks)
    counter = 1
    updated_scripts = user_blocks
    print("what the heck, updated scripts here: {}".format(updated_scripts))
    print("what the heck, repeat scripts here: {}".format(repeat_scripts))

    print("ddd TRYING TO SIMPLIFY THE USER SCRIPTS")
    while replace_items:
        counter += 1
        if counter > 20 or not user_blocks:
            break
        updated_script = sub_dict_into_dict(updated_scripts, repeat_scripts, p_json['targets'][0]['blocks'])
        print(f"AAA simplifying inside loop SCRIPT AFTER SIMPLIFY {str(updated_scripts)} ")
        print(f"AAA simplifying inside loop AFTER SIMPLIFY if different loop again{user_blocks_string}")
        if str(updated_script) == user_blocks_string:
            replace_items = False
        else:
            user_blocks_string = str(updated_scripts)
    print(f"FINALLY again! REPEAT BLOCKS")
    for key in repeat_scripts:
        print(f"key {key} block {repeat_scripts[key]}")
    print(f"FINALLY again! USER BLOCKS")
    for key in user_blocks:
        print(f"key {key} block {user_blocks[key]}")
    print("\n\n\n")
    # do main script
    print("\n\n\n\n\n\nDDD main script, pre substitution of repeat scripts:")
    print(main_script)
    replace_items = True
    main_script_string = str(main_script)
    updated_script = main_script
    while replace_items:

        print("\n\n\n\n\n\nDDD main script, pre substitution of repeat scripts:")
        print(main_script)
        updated_script = sub_dict_into_list(updated_script, repeat_scripts, p_json['targets'][0]['blocks'])
        print(f"updated script subbing repeats {str(updated_script)}")

        print("DDD main script, post substitution of repeat script:")
        print("DDD \n\n\n\n")

        print("DDD main script, pre subbing in user blocks:")
        print(main_script)
        print("DDD \n\n\n\n")

        updated_script = sub_user_blocks(updated_script, user_blocks, p_json['targets'][0]['blocks'])

        print("DDD main script, post subbing in user blocks:")

        print("DDD main script, pre subbing in operator blocks:")
        print(main_script)
        print("DDD \n\n\n\n")

        updated_script = sub_user_blocks(updated_script, operator_scripts, p_json['targets'][0]['blocks'])

        print("DDD main script, post subbing in operator blocks:")
        print(main_script)
        print("\n\n\n")
        if str(updated_script) == main_script_string:
            replace_items = False
        else:
            main_script_string = str(updated_script)

    return [main_script, user_blocks, repeat_scripts]


def find_turnright(p_user_blocks, p_points):
    """
    finds if there is a user defined block named turnright that turns left 3x.
    :param p_user_blocks: Dictionary of user defined blocks.  LIke this:
    'turnright': [['control_repeat', '3', ['turnleft']]]
    :param p_points: number of points this is worth (int)
    :return:true of false
    """
    p_test = {"name": "Testing that there is a user-defined turnright (" + str(p_points) + " points) <br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>"
                              "There is a user-defined turn right!"
                              " <br> ",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5>  ",
              'points': 0
              }
    if 'turnright' in p_user_blocks.keys():
        p_test['fail_message'] += "There is a user-defined turnright block (pass)<br>"
        if p_user_blocks['turnright'] == [['control_repeat', '3', ['turnleft']]] or \
                p_user_blocks['turnright'] == [['control_repeat', '3', [['turnleft']]]] or \
                p_user_blocks['turnright'] == ['turnleft', 'turnleft', 'turnleft']:
            p_test['points'] += p_points
        else:
            p_test['pass'] = False
            p_test['fail_message'] += "turnright needs to turn right (2 possible definitions will pass) (fail)"
    else:
        p_test['pass'] = False
        p_test['fail_message'] += "There is not a user-defined turnright block (fail).<br>" \
                                  "The block needs to be named <b> exactly </b> turnright."
    return p_test


def find_repeatfive(p_user_blocks, p_points):
    """
    finds if there is a user defined block named that repeats something 5x.
    :param p_user_blocks: Dictionary of user defined blocks.  LIke this:
    'turnright': [['control_repeat', '3', ['turnleft']]]
    :param p_points: number of points this is worth (int)
    :return:true of false
    """
    p_test = {"name": "Testing that there is a user-defined block with a repeat with a correct number of times"
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>"
                              "There is a block with a repeat with a correct number of times."
                              " <br> ",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5>  ",
              'points': 0
              }
    for key in p_user_blocks:
        if str(p_user_blocks[key]) == "[['control_repeat', '5', [['move', 'pickbeeper']]]]" or \
                str(p_user_blocks[key]) == "[['control_repeat', '5', [['pickbeeper', 'move']]]]":
            p_test['points'] += p_points
            p_test['pass'] = True
            break
    if p_test['pass'] is False:
        p_test['fail_message'] += "There needs to be a block that repeats the correct number of times" \
                                      "(fail)"

    return p_test


def find_repeatfour(p_user_blocks, p_points):
    """
    finds if there is a user defined block named that repeats something 4x.
    :param p_user_blocks: Dictionary of user defined blocks.  LIke this:
    'turnright': [['control_repeat', '3', ['turnleft']]]
    :param p_points: number of points this is worth (int)
    :return:true of false
    """
    import re
    p_test = {"name": "Testing that there is a user-defined block with a repeat with a correct number of times"
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>"
                              "There is a block with a repeat with a correct number of times."
                              " <br> ",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5>  ",
              'points': 0
              }
    for key in p_user_blocks:
        match = re.search(r"'control_repeat', \s* '4'", str(p_user_blocks[key]), re.M | re.X | re.S)
        if match:
            p_test['points'] += p_points
            p_test['pass'] = True
            break
    if p_test['pass'] is False:
        p_test['fail_message'] += "There needs to be a block that repeats the correct number of times" \
                                      "(fail)"

    return p_test


def extract_coder_json(p_json):
    """

    extracts the code json from Karel file (from project.json)
    :param p_json: json for entire file
    :return: json for just the code
    """
    blocks_to_delete = []
    for i, sprite in enumerate(p_json['targets']):
        if sprite['name'] == 'Coder':
            pass
        else:
            blocks_to_delete.append(i)
    p_coder_json = p_json
    counter = 0
    for block in blocks_to_delete:
        p_coder_json['targets'].pop(block - counter)
        counter += 1

    return p_coder_json


def extract_block_names(p_json):
    """
    extracts block names from output of extract_code_json. End up with something like [move, move, turnleft, eat_fish]
    or whatever.
    :param p_json: json for just the coder
    :return: list of moves
    """
    blocks_to_delete = []
    for i, sprite in enumerate(p_json['targets']):
        if sprite['name'] == 'Coder':
            pass
        else:
            blocks_to_delete.append(i)

    p_coder_json = p_json
    counter = 0
    for block in blocks_to_delete:
        p_coder_json['targets'].pop(block - counter)
        counter += 1

    return p_coder_json
