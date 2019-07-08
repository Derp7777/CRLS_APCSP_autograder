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
        if proposed_square in self.barriers:
            return False
        else:
            return True

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
        print(f"coordinate {coordinate}, self beeters {self.beepers}")

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
    print(f"ooo entirety of all moves {moves}")
    #print(f"position and direction beginning {p_karel.x} {p_karel.y} {p_karel.direction} ")
    for i, move in enumerate(moves):
        print(f"ooo MOVE {move} i {i}")
        if isinstance(move, list):
            print(f"ooo LIST rerun the move {move}")
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
                #print("BBB FOUND A REPEAT")
                times = int(moves[i + 1])
                for _ in range(times):
                    print(f"ooo repeat time {_}")
                    do_karel(p_karel, moves[2], success)
                break
        print(f"position and direction end {p_karel.x} {p_karel.y} {p_karel.direction} ")

    #print(f"ooo entirety of before return moves {moves}")

    #print(f"success! {success}")
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
    print("BBB ABOUT TO START MOVING NOW!")
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
    #print(f"inside simplify blocks main script {p_main_script}  repeat blocks {p_repeat_blocks} ")
    _check_block(p_main_script, p_repeat_blocks, p_blocks)
    for i, item in enumerate(p_main_script):
        if isinstance(item, list):
            p_main_script[i] = simplify_blocks(p_main_script[i], p_repeat_blocks, p_blocks)
        else:
            continue
    return p_main_script


def _sub_user_blocks_helper(p_main_script, p_user_blocks, p_blocks):
    """
    Helper script for sub_user_blocks.  Checks main script for user blocks
    :param p_main_script: (something like  ['move', 'move', 'turnleft', 'turnright', ])  (list)
    :param p_user_blocks: something like
    {'turnright' : ['turnleft', 'turnleft', 'turnleft']} (dictionary)
    :param p_blocks:coder blocks
    :return:
    """
    for i, item in enumerate(p_main_script):
        for key in p_user_blocks:
            if item == key:
                #print(f"CCC before failure item {item} key{key}   ")
                # blocks_key {p_blocks([key])}")

                # opcode = p_blocks[key]['opcode']
                # print(f"OPCODE INSIDE CHECK BLOCK  user blocks helper {opcode}")
                # if opcode == 'control_repeat':
                #     times = p_user_blocks[key]['inputs']['TIMES'][1][1]
                #     p_main_script[i] = ['control_repeat', times, p_user_blocks[key]]
                # else:
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
    _sub_user_blocks_helper(p_main_script, p_user_blocks, p_blocks)
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
                    if item == 'WyRUvHyzhO68?=UPX4DT':
                        print(f"fff in _sub_dict_into_list  item{item} key{key} \np_list{p_list} \np_dict{p_dict} i {i}")
                    opcode = p_blocks[item]['opcode']
                    #print(f"OPCODE INSIDE CHECK BLOCK {opcode}")
                    if opcode == 'control_repeat':
                        #print(f"ttt2 item{item} key{key} \np_list{p_list} \np_dict{p_dict}")
                        times = p_blocks[item]['inputs']['TIMES'][1][1]
                        #print(f"ttt2.5 item{item} key{key} \np_list{p_list} \np_dict{p_dict}")
                        print(f"MARBLES {p_dict[key]}")
                        p_list[i] = [['control_repeat', times, p_dict[key][0]]]
                        print(f"MARBLES 2 {p_list[i]}")
                        print(type(p_list[i]))
                        print(len(p_list[i]))

                        if len(p_dict[key]) > 1:
                            p_list[i].extend(p_dict[key][1:])
                        print(f"MARBLES 3 {p_list[i]}")

                        # #print(f"ttt3 item{item} key{key} \np_list{p_list} \np_dict{p_dict}")
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
    #print(f"rrr pre initial sub_dict_into_list p_list {p_list} \n p_dict {p_dict}")

    for i, item in enumerate(p_list):
        if isinstance(item, list):
            p_list[i] = sub_dict_into_list(p_list[i], p_dict, p_blocks)
        else:
            _sub_dict_into_list_helper(p_list, p_dict, p_blocks)
            #print(f"rrr post initial sub_dict_into_list  p_list {p_list} \n p_dict {p_dict}")

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
            #print(f"ddd _sub_dict_into_dict key{ key } \n item {item} \np_dict_subbed {p_dict_subbed} \np_dict_subber {p_dict_subber}")
            if isinstance(item, str):
                if item in p_dict_subber.keys():

                    print(f"ddd match! key{ key } item {item}")
                   # print(f"fff {p_blocks}")
                    # print(f"fff {p_blocks[item]}")

                    opcode = p_blocks[item]['opcode']
                    if opcode == 'control_repeat':
                        times = p_blocks[item]['inputs']['TIMES'][1][1]
                        p_dict_subbed[key][i] = ['control_repeat', times, p_dict_subber[item]]
                    else:
                        p_dict_subbed[key][i] = p_dict_subber[item]

                # i.e. first item of dict['getrow'] =  ['move', 'pickbeeper']
    print(f"ggg p_dict_subbed before return {p_dict_subbed}")
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
        print(f"aaa simplify this key key {key}")
        for i, item in enumerate(p_dict_subbed[key]):
            if isinstance(item, list):
                print(f"ggg item {item}")
              #  print(f"ggg p_dict_subbed[key] {p_dict_subbed[key]}")

               # print(f"ggg p_dict_subbed[key][i] {p_dict_subbed[key][i]}")
                if p_dict_subbed[key][i][0] == 'control_repeat':
             #       print(f"xxx p_dict_subbed[key][i][0] {p_dict_subbed[key][i][0]}")
             #       print(f"xxx p_dict_subbed[key][i][2] {p_dict_subbed[key][i][2]}")

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
        if p_target['blocks'][current_block_id]['opcode'] == 'control_repeat':
            substack_id = p_target['blocks'][current_block_id]['inputs']['SUBSTACK'][1]
            repeat_script = build_karel_script(substack_id, p_target)
            times = p_target['blocks'][current_block_id]['inputs']['TIMES'][1][1]
            script.append(['control_repeat', times, repeat_script])
        elif p_target['blocks'][current_block_id]['opcode'] == 'procedures_call':
            script.append(p_target['blocks'][current_block_id]['mutation']['proccode'])
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
    for target in p_json['targets']:
        if target['blocks']:
            for block_id in target['blocks']:
                if 'opcode' in target['blocks'][block_id]:
                    # print(f"working this code {block_id}, this opcode {target['blocks'][block_id]['opcode']}")
                    # print(f"hhh user blocks {user_blocks} ")
                    # print(f"hhh repeat blocks {repeat_scripts}")
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

                    if target['blocks'][block_id]['opcode'] == "control_repeat":
                        print(f"yyy {block_id} doing repeat now.   ")
                        if 'inputs' in target['blocks'][block_id]:
                            if 'SUBSTACK' in target['blocks'][block_id]['inputs']:
                                repeat_scripts[block_id] = [target['blocks'][block_id]['inputs']['SUBSTACK'][1]]
                    elif 'parent' in target['blocks'][block_id]:
                        if target['blocks'][block_id]['parent'] is not None:
                            parent_id = target['blocks'][block_id]['parent']
                            print(f"yyy {block_id} doing repeat substacks now .")
                            if target['blocks'][parent_id]['inputs']:
                                if 'SUBSTACK' in target['blocks'][parent_id]['inputs']:
                                    print("yyy maybe it's a repeat block with a parent")
                                    if target['blocks'][parent_id]['inputs']['SUBSTACK'][1] == block_id:

                                        script = _order_procedure_blocks(block_id, target)
                                        #print(script)
                                        temp_repeat_commands = []
                                        for item in script:
                                            if item['opcode'] == 'event_whenbroadcastreceived' or \
                                                    item['opcode'] == 'data_setvariableto':
                                                pass
                                            elif 'mutation' in item.keys():
                                                temp_repeat_commands.append(item['mutation']['proccode'])
                                            else:
                                                temp_repeat_commands.append(item['inputs']['SUBSTACK'][1])
                                        #print(f"temp repeat commands for {block_id}")
                                        #print(temp_repeat_commands)
                                        repeat_scripts[block_id] = temp_repeat_commands
                                        #repeat_scripts[parent_id] = temp_repeat_commands
                    if target['blocks'][block_id]['opcode'] == "procedures_definition":  # can skip, previous if does
                        # print("yyy this is procedure defintion skip")
                        pass
                    elif target['blocks'][block_id]['opcode'] == "data_setvariableto":  # Get the start
                        print("A NEW BEGINNING")
                        main_script = []
                        main_script = build_karel_script(block_id, target)
                        print("THIS IS THE MAIN SCRIPT MAYBE")
                        print(main_script)
                    #     print(f"yyy this is the starting block {block_id}")
                    #      script = _order_procedure_blocks(block_id, target)
                    #      for item in script:
                    #          if item['opcode'] == 'event_whenbroadcastreceived' or \
                    #                  item['opcode'] == 'data_setvariableto':
                    #              pass
                    #         elif 'mutation' in item.keys():
                    #             main_script.append(item['mutation']['proccode'])
                    #         elif 'inputs' in item.keys():
                    #             if 'SUBSTACK' in item['inputs'].keys():
                    #                 main_script.append(item['ID'])
                    # elif target['blocks'][block_id]['parent'] is None and \
                    #         target['blocks'][block_id]['opcode'] != 'procedures_call':
                    #     # print("hmm.  these are scripts hanging out in noewhere"
                    #     #       " {} {} ".format(block_id, target['blocks'][block_id]))
                    #     script = _order_procedure_blocks(block_id, target)
                    #     scripts[block_id] = script
                    #
                    # elif target['blocks'][block_id]['parent'] is not None:
                    #     parent_id = target['blocks'][block_id]['parent']
                    #     print(f"yyy {block_id} Has a parent. skip the ones that are in the middle of a script,"
                    #           "only looking to see if the parent is control_repeat for now.")
                    #     if target['blocks'][parent_id]['inputs']:
                    #         if 'SUBSTACK' in target['blocks'][parent_id]['inputs']:
                    #             print("yyy maybe it's a repeat block with a parent")
                    #             if target['blocks'][parent_id]['inputs']['SUBSTACK'][1] == block_id:
                    #
                    #                 script = _order_procedure_blocks(block_id, target)
                    #                 #print(script)
                    #                 temp_repeat_commands = []
                    #                 for item in script:
                    #                     if item['opcode'] == 'event_whenbroadcastreceived' or \
                    #                             item['opcode'] == 'data_setvariableto':
                    #                         pass
                    #                     elif 'mutation' in item.keys():
                    #                         temp_repeat_commands.append(item['mutation']['proccode'])
                    #                     else:
                    #                         temp_repeat_commands.append(item['inputs']['SUBSTACK'][1])
                    #                 #print(f"temp repeat commands for {block_id}")
                    #                 #print(temp_repeat_commands)
                    #                 repeat_scripts[block_id] = temp_repeat_commands
                    #                 #repeat_scripts[parent_id] = temp_repeat_commands



    user_blocks_orig = deepcopy(user_blocks)
    print(f"repeat blocks pre simplification of repeat ")
    for key in repeat_scripts:
        print(f"key {key} block {repeat_scripts[key]}")
    print(f"user blocks pre simplification os user BLOCKS")
    for key in user_blocks:
        print(f"key {key} block {user_blocks[key]}")
    replace_items = True
    user_blocks_string = str(user_blocks)
    counter = 1
    updated_scripts = user_blocks
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
    print("\n\n\n\n\n\nDDD main script, pre:")
    print(main_script)
    replace_items = True
    main_script_string = str(main_script)
    updated_script = main_script
    while replace_items:
    #     print("lll subbing in user blocks for main script")
    #     updated_script = sub_user_blocks(main_script, user_blocks, p_json['targets'][0]['blocks'])
    #     print(f"AAA MAIN SCRIPT AFTER USER SUB {updated_script} {main_script}")
    #     print("lll subbing in repeat scripts for main script")

        updated_script = sub_dict_into_list(updated_script, repeat_scripts, p_json['targets'][0]['blocks'])
        print(f"AAA MAIN SCRIPT after subbing in repeat scripts {str(updated_script)}  \nmain string {main_script_string}")
        # updated_script = sub_dict_into_list(updated_script, user_blocks_orig, p_json['targets'][0]['blocks'])
        # print(f"AAA MAIN SCRIPT AFTER subbing in user blocks {str(updated_script)}  main string {main_script_string}")
        if str(updated_script) == main_script_string:
            replace_items = False
        else:
            main_script_string = str(updated_script)

    # while replace_items:
    #     updated_script = sub_user_blocks(main_script, user_blocks, p_json['targets'][0]['blocks'])
    #     print(f"AAA MAIN SCRIPT AFTER USER SUB {updated_script} {main_script}")
    #     updated_script = simplify_blocks(updated_script, repeat_scripts, p_json['targets'][0]['blocks'])
    #     print(f"AAA MAIN SCRIPT AFTER SIMPLIFY {str(updated_script)}  main string {main_script_string}")
    #
    #     if str(updated_script) == main_script_string:
    #         replace_items = False
    #     else:
    #         main_script_string = str(updated_script)
    print("DDD main script, post:")
    print(main_script)
    print("DDD \n\n\n\n")

    print("DDD main script, pre sugging in user blocks:")
    print(main_script)
    print("DDD \n\n\n\n")
    replace_items = True
    main_script_string = str(main_script)
    updated_script = main_script
    while replace_items:
    #     print("lll subbing in user blocks for main script")
    #     updated_script = sub_user_blocks(main_script, user_blocks, p_json['targets'][0]['blocks'])
    #     print(f"AAA MAIN SCRIPT AFTER USER SUB {updated_script} {main_script}")
    #     print("lll subbing in repeat scripts for main script")

        updated_script = sub_user_blocks(updated_script, user_blocks, p_json['targets'][0]['blocks'])
        print(f"AAA MAIN SCRIPT after subbing in repeat scripts {str(updated_script)}  \nmain string {main_script_string}")
        # updated_script = sub_dict_into_list(updated_script, user_blocks_orig, p_json['targets'][0]['blocks'])
        # print(f"AAA MAIN SCRIPT AFTER subbing in user blocks {str(updated_script)}  main string {main_script_string}")
        if str(updated_script) == main_script_string:
            replace_items = False
        else:
            main_script_string = str(updated_script)
    print("DDD main script, post ugging in user blocks:")
    print(main_script)
    print("\n\n\n")
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
                p_user_blocks['turnright'] == [['control_repeat', '3', [['turnleft']]]] or \
                p_user_blocks['turnright'] == ['turnleft', 'turnleft', 'turnleft']:
            p_test['points'] += p_points
        else:
            p_test['pass'] = False
            p_test['fail_message'] += "turnright needs to turn right (2 possible definitions will pass) (fail)"
    else:
        p_test['pass'] = False
        p_test['fail_message'] += "There is not a user-defined turnright block (fail)."
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
    print("find repeat5 ")
    print(p_user_blocks)
    for key in p_user_blocks:
        print(f" IS THER A REPEAT5 {p_user_blocks[key]}")
        if str(p_user_blocks[key]) == "[['control_repeat', '5', [['move', 'pickbeeper']]]]" or \
                str(p_user_blocks[key]) == "[['control_repeat', '5', [['pickbeeper', 'move']]]]":
            p_test['points'] += p_points
            print("OH  YEHA")
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
