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
        elif self.direction == 3:
            proposed_square = [self.x - 5, self.y]
        else:
            raise Exception("Direction can only be 0 - 3.  Direction is: " + str(self.direction))
        return proposed_square not in self.barriers

    def turnleft(self):
        self.direction = (self.direction + 3) % 4

    def move(self):
        if self.front_is_clear():
            print(f"MOVING {self.direction} {self.x} {self.y}  beepers {self.num_beepers}")
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
        print(f"coordinate {coordinate}, self beepers {self.beepers}")

        if coordinate in self.beepers:
            self.beepers.remove(coordinate)
            self.num_beepers += 1
            return True
        else:
            return False


def _karel_helper():
    print("yes")


def do_karel(p_karel, moves, success):
    if success is False:
        return False
    # print(f"AAA entirety of moves {moves}")
    print(f"position and direction beginning {p_karel.x} {p_karel.y} {p_karel.direction} ")
    for i, move in enumerate(moves):
        print(f"MOVE {move} i {i}")
        if isinstance(move, list):
            print(f"LIST HERE {move}")
            do_karel(p_karel, moves[i], success)
        else:
            if move == 'move':
                if p_karel.move() is False:
                    success = False
                    break
            elif move == 'turnleft':
                p_karel.turnleft()
            elif move == 'pickbeeper':
                if p_karel.pickbeeper() is False:
                    success = False
                    break
                else:
                    print(f"PICKUP  up beeper {p_karel.num_beepers}")
            elif move == 'control_repeat':
                print("BBB FOUND A REPEAT")
                times = int(moves[i + 1])
                for _ in range(times):
                    do_karel(p_karel, moves[2], success)
                break
        print(f"position and direction end {p_karel.x} {p_karel.y} {p_karel.direction} ")

    print(f"entirety of before return moves {moves}")

    print(f"success! {success}")
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
                print(f"OPCODE INSIDE CHECK BLOCK {opcode}")
                if opcode == 'control_repeat':
                    times = p_blocks[key]['inputs']['TIMES'][1][1]
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


def sub_user_blocks(p_main_script, p_user_blocks):
    """
    Similar to simplify_blocks, except with user scripts (like turnright)
    :param p_main_script:  main block
    (something like  ['move', 'move', 'turnleft', 'turnright'])  (list)
    :param p_user_blocks: something like
    {'turnright' : ['turnleft', 'turnleft', 'turnleft']} (dictionary)
    :return: p_main_script
    """
    _sub_user_blocks_helper(p_main_script, p_user_blocks)
    for i, item in enumerate(p_main_script):
        if isinstance(item, list):
            p_main_script[i] = sub_user_blocks(p_main_script[i], p_user_blocks)
    return p_main_script


def _order_procedure_blocks(starting_block_id, p_target):
    """
    Called by arrange_blocks, to traverse a scratch procedure json, finding sequential blocks until it hits the end
    for blocks, two checks = there is a substack or there is a next (or both)
    :param starting_block_id: Key of the block with which o start the script
    :param p_target: json info for block that is starting the script (value of dictionary with key starting_block-id)
    :return: list.   values is list of block JSON info for each item in the script
    """

    # I didn't change the other script at all.  I think the change comes in clean
    temp_block = p_target['blocks'][starting_block_id]
    temp_block['ID'] = starting_block_id  # #stick the ID onto the dictionary
    script = [temp_block]
    print(f"SCRIPT OF STARTING ID {script} BLOCK {starting_block_id}")
    current_block_id = starting_block_id
    if 'mutation' in p_target['blocks'][starting_block_id].keys():
        print(f"current block info {p_target['blocks'][starting_block_id]['mutation']['proccode']}")
    next_block_id = p_target['blocks'][current_block_id]['next']
    print(f"next block id to add {next_block_id}")
    # substack_block_id = None
    # if 'inputs' in p_target['blocks'][starting_block_id]:
    #     if 'SUBSTACK' in p_target['blocks'][starting_block_id]['inputs']:
    #         substack_block_id = p_target['blocks'][starting_block_id]['inputs']['SUBSTACK'][1]
    #         script.append([p_target['blocks'][substack_block_id]])
    # if substack_block_id:
    # #     print("SUBSTACK BLOCK_ID FOUND 1")
    #
    #     script.append(['control_repeat', p_target['blocks'][substack_block_id]])
    #     substack_block_id = None
    #    while next_block_id is not None or substack_block_id is not None:
    while next_block_id is not None:
        temp_block = p_target['blocks'][next_block_id]
        temp_block['ID'] = next_block_id  # #stick the ID onto the dictionary
        script.append(temp_block)
        current_block_id = next_block_id
        next_block_id = p_target['blocks'][current_block_id]['next']
        print(f"CURRENT BLOCK {p_target['blocks'][current_block_id]}  BLOCK ID {current_block_id}")
        # if 'inputs' in p_target['blocks'][current_block_id]:
        #     print("INPUT IS HERE")
        #     print(p_target['blocks'][current_block_id])
        #     if 'SUBSTACK' in p_target['blocks'][current_block_id]['inputs']:
        #         substack_block_id = p_target['blocks'][current_block_id]['inputs']['SUBSTACK'][1]
        #         print("SUBSTACK IS HERE")
        # if substack_block_id:
        #     print("SUBSTACK BLOCK_ID FOUND 2")
        #     subscript = _order_procedure_blocks(p_target['blocks'][substack_block_id], p_target)
        #     script.append(subscript)
        #     substack_block_id = None
        # if next_block_id is not None:
        #     # print(f"WHAT {p_target['blocks'][next_block_id]}")
        #     if 'inputs' in p_target['blocks'][next_block_id].keys():
        #         if 'SUBSTACK' in p_target['blocks'][next_block_id]['inputs']:
        #             repeat_script = _order_procedure_blocks(p_target['blocks'][next_block_id]['inputs']['SUBSTACK'][1],
        #                                                 p_target)
        #             script.append([repeat_script])

    return script


# get starting block
# if substack, add that first.
# add the control repeat
# add the repeat stuff as a list.  call itself - script = p_target['blocks'][block ID of first thing in repeat]
# append that script to main script as a list.
# if next next next next then keep adding straight up.

# move move
# define, control
# define, l, l, l

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
    scripts = {}
    given_blocks = ['move', 'turnleft', 'pickbeeper', 'putbeeper', 'turnoff', ]
    user_blocks = {}
    main_script = []
    repeat_scripts = {}
    for target in p_json['targets']:
        if target['blocks']:
            for block_id in target['blocks']:
                if 'opcode' in target['blocks'][block_id]:
                    print(f"working this code {block_id}, this opcode {target['blocks'][block_id]['opcode']}")
                    if target['blocks'][block_id]['opcode'] == "procedures_prototype":  # Get the procedures
                        if target['blocks'][block_id]['mutation']['proccode'] not in given_blocks:
                            parent_id = target['blocks'][block_id]['parent']  # get the procedures_definition
                            block_start_id = target['blocks'][parent_id]['next']  # get the actual first thing
                            script = _order_procedure_blocks(block_start_id, target)

                            print(f"FINAL SCRIPT {script}")
                            cleaned_custom_block = []
                            for item in script:
                                print(f"ITEM NOW {item} ID {block_id}")
                                if 'mutation' in item.keys():
                                    cleaned_custom_block.append(item['mutation']['proccode'])
                                elif 'inputs' in item.keys():
                                    if 'SUBSTACK' in item['inputs'].keys():
                                        # if item['opcode'] == 'control_repeat':
                                        #     print(item['inputs']['TIMES'])
                                        #     times = item['inputs']['TIMES'][1][1]
                                        #     action = 'control_repeat_' + str(times)
                                        # cleaned_custom_block.append(item['inputs']['SUBSTACK'][1])
                                        cleaned_custom_block.append(item['ID'])
                            # cleaned_custom_block = [item['mutation']['proccode']
                            #                         if 'mutation' in item.keys() else item['inputs']['SUBSTACK'][1]
                            #                         for item in script]
                            user_blocks[target['blocks'][block_id]['mutation']['proccode']] = cleaned_custom_block
                    elif target['blocks'][block_id]['opcode'] == "procedures_definition":  # can skip, previous if does
                        pass
                    elif target['blocks'][block_id]['opcode'] == "event_whenbroadcastreceived":  # Get the start
                        script = _order_procedure_blocks(block_id, target)
                        for item in script:
                            if item['opcode'] == 'event_whenbroadcastreceived' or \
                                    item['opcode'] == 'data_setvariableto':
                                pass
                            elif 'mutation' in item.keys():
                                main_script.append(item['mutation']['proccode'])
                            elif 'inputs' in item.keys():
                                if 'SUBSTACK' in item['inputs'].keys():
                                    main_script.append(item['ID'])
                    elif target['blocks'][block_id]['parent'] is None and \
                            target['blocks'][block_id]['opcode'] != 'procedures_call':
                        print("hmm.  these are scripts hanging out in nowhere"
                              " {} {} ".format(block_id, target['blocks'][block_id]))
                        script = _order_procedure_blocks(block_id, target)
                        scripts[block_id] = script
                    elif target['blocks'][block_id]['parent'] is not None:
                        parent_id = target['blocks'][block_id]['parent']
                        print("Hm I believe these are scripts that part of a script they have parents."
                              "But Im gonna check that they have parents and I only am looking for the"
                              "first one of a c-loop")
                        if target['blocks'][parent_id]['inputs']:
                            if 'SUBSTACK' in target['blocks'][parent_id]['inputs']:
                                if target['blocks'][parent_id]['inputs']['SUBSTACK'][1] == block_id:
                                    script = _order_procedure_blocks(block_id, target)
                                    print("MORE DONE")
                                    print(script)
                                    temp_repeat_commands = []
                                    for item in script:
                                        if item['opcode'] == 'event_whenbroadcastreceived' or \
                                                item['opcode'] == 'data_setvariableto':
                                            pass
                                        elif 'mutation' in item.keys():
                                            temp_repeat_commands.append(item['mutation']['proccode'])
                                        else:
                                            temp_repeat_commands.append('karelloop_' + item['inputs']['SUBSTACK'][1])
                                    print("REPEATER")
                                    print(temp_repeat_commands)
                                    #                                    repeat_scripts[block_id] = temp_repeat_commands
                                    repeat_scripts[parent_id] = temp_repeat_commands

    print("main script, pre:")
    print(main_script)
    replace_items = True
    main_script_string = str(main_script)
    while replace_items:
        updated_script = sub_user_blocks(main_script, user_blocks)
        print(f"AAA MAIN SCRIPT AFTER USER SUB {updated_script} {main_script}")
        updated_script = simplify_blocks(updated_script, repeat_scripts, p_json['targets'][0]['blocks'])
        print(f"AAA MAIN SCRIPT AFTER SIMPLIFY {str(updated_script)}  main string {main_script_string}")

        if str(updated_script) == main_script_string:
            replace_items = False
        else:
            main_script_string = str(updated_script)
    print(f"FINALLY! REPEAT BLOCKS")
    for key in repeat_scripts:
        print(f"key {key} block {repeat_scripts[key]}")
    print(f"FINALLY! USER BLOCKS")

    for key in user_blocks:
        print(f"key {key} block {user_blocks[key]}")
    return [main_script, user_blocks, repeat_scripts]


def find_turnright(p_user_blocks, p_points):
    """
    finds if there is a user defined block named turnright that turns left 3x.
    :param p_user_blocks: Dictionary of user defined blocks.  LIke this:
    'turnright': [['control_repeat', '3', ['turnleft']]]
    :param p_points: number of points this is worth (int)
    :return:true of false
    """
    p_test = {"name": "Testing that there is a user-defined turn right (" + str(p_points) + " points) <br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>"
                              "There is a user-defined turn right!"
                              " <br> ",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5>  ",
              'points': 0
              }
    if 'turnright' in p_user_blocks.keys():
        p_test['fail_message'] += "There is a user-defined turnright block (pass)<br>"
        print("AAA TURNRIGHT")
        print(p_user_blocks['turnright'])
        if p_user_blocks['turnright'] == [['control_repeat', '3', ['turnleft']]] or \
                p_user_blocks['turnright'] == ['turnleft', 'turnleft', 'turnleft']:
            p_test['points'] += p_points
        else:
            p_test['pass'] = False
            p_test['fail_message'] += "turnright needs to turn right (2 possible definitions will pass) (fail)"
    else:
        p_test['pass'] = False
        p_test['fail_message'] += "There is not a user-defined turnright block (fail)."
    return p_test


def extract_coder_json(p_json):
    """

    extracts the code json from Karel file (from project.json)
    :param p_json: json for entire file
    :return: json for just the code
    """
    blocks_to_delete = [i for i, sprite in enumerate(p_json['targets']) if sprite['name'] != 'Coder']
    # blocks_to_delete = []
    # for i, sprite in enumerate(p_json['targets']):
    #     if not sprite['name'] == 'Coder':
    #         blocks_to_delete.append(i)
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
    blocks_to_delete = [i for i, sprite in enumerate(p_json['targets']) if sprite['name'] != 'Coder']
    # blocks_to_delete = []
    # for i, sprite in enumerate(p_json['targets']):
    #     if sprite['name'] == 'Coder':
    #         pass
    #     else:
    #         blocks_to_delete.append(i)

    p_coder_json = p_json
    counter = 0
    for block in blocks_to_delete:
        p_coder_json['targets'].pop(block - counter)
        counter += 1

    return p_coder_json
