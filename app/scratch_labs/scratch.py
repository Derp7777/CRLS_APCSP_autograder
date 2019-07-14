def scratch_filename_test(p_filename, p_lab):
    """
    Checks that the filename follows correct format i.e. 2019_ewu_1.3.sb3
    :param p_filename: the name of the file
    :param p_lab: the lab
    :return: a test dictionary
    """
    import re
    from app.python_labs import YEAR

    find_year = re.search(YEAR, p_filename)
    find_lab = re.search(p_lab, p_filename)
    find_all = re.search(YEAR + r"_ .+ _ " + p_lab + r".sb3", p_filename, re.X | re.M | re.S)
    p_test_filename = {"name": "Testing that file is named correctly",
                       "pass": True,
                       "pass_message": "<h5 style=\"color:green;\">Pass!</h5> File name looks correct "
                                       "(i.e. something like 2019_luismartinez_" + p_lab +
                                       ".sb3)",
                       "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                                       "File name of submitted file does not follow required convention. "
                                       " Rename and resubmit.<br>"
                                       "File name should be like this: <br> <br>"
                                       "2019_luismartinez_" + p_lab + ".sb3 <br><br>"
                                       "File must be scratch 3 file (ends in .sb3).<br>" 
                                       "A Google doc with code copy+pasted in is not accepted <br>"
                                       " Other tests not run. They will be run after filename is fixed.<br>",
                       'points': 0,
                       }
    if find_year and find_lab and find_all:
        p_test_filename['pass'] = True
    else:
        p_test_filename['pass'] = False
    return p_test_filename


def read_json_file():
    """
    Reads in json file
    :return: dictionary of what is in json file
    """
    import json

    with open('/tmp/project.json', 'r') as json_file:
        json_data = json.load(json_file)
    return json_data


def unzip_sb3(p_filename):
    """
    Unzips the file
    :param p_filename: name of file (string)
    :return: none
    """
    from zipfile import ZipFile
    with ZipFile(p_filename, 'r') as p_zip:
        p_zip.extractall('/tmp', )


def find_help(p_json, p_points):
    """
    Reads in json info (in dictionary form)
    :param p_json: json info (as dictionary)
    :param p_points: points this is worth
    :return: test dictionary
    """
    import re

    p_test_help = {"name": "Testing that you got a help and documented it as a comment (" + str(p_points) + " points)",
                   "pass": True,
                   "pass_message": "<h5 style=\"color:green;\">Pass (for now).<h5>"
                                   "  You have a comment with 'help' in it.  <br>"
                                   "Be sure your comment is meaningful, otherwise this can be overturned "
                                   "on review.",
                   "fail_message": "<h5 style=\"color:red;\">Fail.</h5>"
                                   "  Did not find a comment in your code with the word 'help' describing"
                                   " how somebody helped you with your code.  <br>"
                                   "This must be a MEANINGFUL help.<br>"
                                   "For example 'Luis helped by testing that input abc gave output def as expected'"
                                   "will score.  <br>"
                                   "Helps such as 'Joe helped test my code' will probably be overturned on review.<br>"
                                   "This translates to " + str(p_points) + " points deduction.<br>" +
                                   "Your help can NOT be from teachers Atwood, Wu, or Martinez",
                   'points': 0
                   }
    help_comments = 0
    for target in p_json['targets']:
        if target['comments']:
            for comment_id in target['comments']:
                helps = re.search('help', target['comments'][comment_id]['text'], re.X | re.M | re.S)
                teacher = re.search('(Wu|Martinez|Atwood)', target['comments'][comment_id]['text'], re.X | re.M | re.S)
                if helps and not teacher:
                    help_comments += 1
    if help_comments == 0:
        p_test_help['pass'] = False
    else:
        p_test_help['points'] += p_points
    return p_test_help


def find_variable(p_json, variable_name, p_points):
    """
    Find a particular variable in scratch. Retruns True/False
    :param p_json: The json
    :param variable_name: variable nmae you are looking for
    :param p_points: Number of points this test is worth
    :return: test dictionary
    """
    p_test = {"name": "Testing that variable '" +
                      variable_name +
                      "' is in the Scratch program "
                      "(" + str(p_points) + " points)",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>"
                              "Variable '" +
                              variable_name +
                              "' is in the Scratch program. <br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              "Did not find a variable '" +
                              variable_name +
                              "' in your code.  You must name the variable EXACTLY '" +
                              variable_name +
                              "' with correct spelling and capitalization.  <br>",
              'points': 0
              }

    sprites = p_json['targets']
    for sprite in sprites:
        if 'variables' in sprite:
            variables = sprite['variables']
            for key in variables:
                variable_list = variables[key]
                if variable_name == variable_list[0]:
                    p_test['pass'] = True
    if p_test['pass']:
        p_test['points'] += p_points
    return p_test


def find_question(p_json, question_string, p_points):
    """
    Find a particular string in all of the questions being asked in scratch. Retruns True/False
    :param p_json: The json
    :param question_string: String you are going to regex search in
    :param p_points: Number of points this test is worth
    :return: test dictionary
    """
    import re
    p_test = {"name": "Testing that a question with the string '" +
                      question_string +
                      "' is in the Scratch program "
                      "(" + str(p_points) + " points)",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>"
                              "Question with the string " +
                              question_string +
                              " is in the Scratch program. <br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              "Did not find a question with the string " +
                              question_string +
                              " in your code. <br>",
              'points': 0
              }

    sprites = p_json['targets']
    for sprite in sprites:
        if 'blocks' in sprite:
            blocks = sprite['blocks']
            for block_id in blocks:
                block = blocks[block_id]
                if block['opcode'] == 'sensing_askandwait':
                    question = block['inputs']['QUESTION'][1][1]
                    if re.search(question_string, question, re.X | re.M | re.S):
                        p_test['pass'] = True
    if p_test['pass']:
        p_test['points'] += p_points
    return p_test


def find_set_variable(p_json, variable, value, *, points=0):
    """
    Find a particular string in all of the questions being asked in scratch. Retruns True/False
    :param p_json: The json
    :param variable: the variable
    :param value: value
    :param p_points: Number of points this test is worth
    :return: test dictionary
    """
    p_test = {"name": "Testing that setting a variable '" +
              variable +
              "' to the value '" +
              value +
              "' is in the Scratch program  (" +
                      str(points) +
                      "  points)",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>" +
                              "A variable '" +
                              variable +
                              "' is set to the value '" +
                              value +
                              "' in the Scratch program  <br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              "Did not find  a variable '" +
                              variable +
                              "' with the value '" +
                              value +
                              "' in the Scratch program  <br>",
              'points': 0
              }

    sprites = p_json['targets']
    for sprite in sprites:
        if 'blocks' in sprite:
            blocks = sprite['blocks']
            for block_id in blocks:
                block = blocks[block_id]
                if block['opcode'] == 'data_setvariableto':
                    block_variable = block['fields']['VARIABLE'][0]
                    if isinstance(block['inputs']['VALUE'][1], str):
                        value_block_id = block['inputs']['VALUE'][1]
                        if blocks[value_block_id]['opcode'] == 'sensing_answer':
                            block_value = 'answer'
                    else:
                        block_value = block['inputs']['VALUE'][1][1]
                    if block_variable == variable and block_value == value:
                        p_test['pass'] = True
    if p_test['pass']:
        p_test['points'] += points
    return p_test


def _clean_block(block):
    """
    Helper function, gets rid of a bunch of keys to make more readable
    :param block is a scratch block (dictionary)
    :return: same block, but cleaned
    """

    if 'next' in block.keys():
        del block['next']
    if 'parent' in block.keys():
        del block['parent']
    del block['shadow']
    del block['topLevel']
    if 'x' in block.keys():
            del block['x']
            del block['y']
    return block


def _order_blocks(starting_block_id, p_target):
    """
    Called by arrange_blocks, to traverse a scratch block json, finding sequential blocks until it hits the end
    :param starting_block_id: Key of the block with which o start the script
    :param p_target: json info for block that is starting the script (value of dictionary with key starting_block-id)
    :return: list.   values is list of block JSON info for each item in the script
    """
    script = [p_target['blocks'][starting_block_id]]
    current_block_id = starting_block_id
    next_block_id = p_target['blocks'][current_block_id]['next']
    while next_block_id is not None:
        script.append(p_target['blocks'][next_block_id])
        current_block_id = next_block_id
        next_block_id = p_target['blocks'][current_block_id]['next']
    return script


def arrange_blocks(p_json):
    """
    Looks for a particular script in the code.  Algorithms:
    1. Find all the parents and populate new dictionary.
    2. Keys are keys of the parents.  Values are lists, each item is a block starting at the top of the tree.
    3. Look for "next" key and add that to the value list.

    :param p_json: json info (as dictionary)
    :return: scripts - dictionary of scripts.  Keys are block ID's of parent.  values are lists of individual blocks
    under the parent
    """

    scripts = {}
    for target in p_json['targets']:
        if target['blocks']:
            for block_id in target['blocks']:
                if 'parent' in target['blocks'][block_id]:  # Verify it hasn't been processed already
                    if target['blocks'][block_id]['parent'] is None:                   # Do parent blocks
                        script = _order_blocks(block_id, target)
                        scripts[block_id] = script
                    else:  # Do nested repeat blocks
                        parent_id = target['blocks'][block_id]['parent']
                        if target['blocks'][parent_id]['inputs']:
                            if 'SUBSTACK' in target['blocks'][parent_id]['inputs']:
                                if target['blocks'][parent_id]['inputs']['SUBSTACK'][1] == block_id:
                                    script = _order_blocks(block_id, target)
                                    for block in script:
                                        _clean_block(block)
                                    target['blocks'][parent_id]['inputs']['SUBSTACK'].append(script)

    for key in scripts:
        for block in scripts[key]:
            _clean_block(block)
        print("arrange blocks KEY!!")
        print(scripts[key])
    return scripts


def build_scratch_script(starting_block_id, p_blocks):
    """
    Same as build karel script but copied over so I cdon't break that one
    :param starting_block_id:
    :param p_blocks: al the blocks for this script
    :return: a combined script (dictionary)
    """
    temp_block = p_blocks[starting_block_id]
    temp_block['ID'] = starting_block_id
    current_block_id = starting_block_id
    next_block_id = "continue"
    script = []
    while next_block_id is not None:
        current_block = p_blocks[current_block_id]
        print(f"aaa {current_block_id}")
        if current_block['opcode'] == 'event_whenflagclicked':
            script.append('event_whenflagclicked')
        if current_block['opcode'] == 'event_broadcast':
            message = current_block['inputs']['BROADCAST_INPUT'][1][1]
            script.append(['event_broadcast', message])
        if current_block['opcode'] == 'event_whenbroadcastreceived':
            message = current_block['fields']['BROADCAST_OPTION'][0]
            script.append(['event_whenbroadcastreceived', message])
        elif current_block['opcode'] == 'control_repeat' or \
                current_block['opcode'] == 'control_forever':
            substack_id = current_block['inputs']['SUBSTACK'][1]
            repeat_script = build_scratch_script(substack_id, p_blocks)
            if current_block['opcode'] == 'control_forever':
                times = 150
            else:
                times = current_block['inputs']['TIMES'][1][1]
            script.append(['control_repeat', times, repeat_script])
        elif current_block['opcode'] == 'control_repeat_until':
            substack_id = current_block['inputs']['SUBSTACK'][1]
            condition_id = current_block['inputs']['CONDITION'][1]
            repeat_script = build_scratch_script(substack_id, p_blocks)
            condition_script = build_scratch_script(condition_id, p_blocks)
            script.append(['control_repeat_until', condition_script, repeat_script])
        elif current_block['opcode'] == 'sensing_askandwait':
            if len(current_block['inputs']['QUESTION']) == 2:
                question = current_block['inputs']['QUESTION'][1][1]
            else:
                join_block = current_block['inputs']['QUESTION'][1]
                question = build_scratch_script(join_block, p_blocks)
            script.append(['sensing_askandwait', question])
        elif current_block['opcode'] == 'looks_sayforsecs':
            if len(current_block['inputs']['MESSAGE']) == 3:
                words_id = current_block['inputs']['MESSAGE'][1]
                message = build_scratch_script(words_id, p_blocks)
            else:
                message = current_block['inputs']['MESSAGE'][1][1]  # does not reference anything else
            time = current_block['inputs']['SECS'][1][1]
            script.append(['looks_sayforsecs', message, time])
        elif current_block['opcode'] == 'sensing_answer':
            script.append('sensing_answer')
        elif current_block['opcode'] == 'data_setvariableto':
            if len(current_block['inputs']['VALUE']) == 2:
                value = current_block['inputs']['VALUE'][1][1]
            else:
                if isinstance(current_block['inputs']['VALUE'][1], list):
                    value = 'VARIABLE_' + current_block['inputs']['VALUE'][1][1]
                else:
                    next_id = current_block['inputs']['VALUE'][1]
                    value = build_scratch_script(next_id, p_blocks)
            variable = current_block['fields']['VARIABLE'][0]
            variable = 'VARIABLE_' + variable
            script.append(['data_setvariableto', variable, value])
        elif current_block['opcode'] == 'procedures_call':
            script.append(current_block['mutation']['proccode'])
        elif current_block['opcode'] == 'control_if':
            substack_1_id = current_block['inputs']['SUBSTACK'][1]
            condition_id = current_block['inputs']['CONDITION'][1]
            if_script = build_scratch_script(substack_1_id, p_blocks)
            condition_script = build_scratch_script(condition_id, p_blocks)
            script.append(['control_if', condition_script, if_script])
        elif current_block['opcode'] == 'control_if_else':
            print(f"bbb block {current_block_id}")
            print(f"bbb block {current_block}")
            substack_1_id = current_block['inputs']['SUBSTACK'][1]
            substack_2_id = current_block['inputs']['SUBSTACK2'][1]
            condition_id = current_block['inputs']['CONDITION'][1]
            print(f"IDS {substack_1_id} sub2 {substack_2_id} cond {condition_id}")
            if_script = build_scratch_script(substack_1_id, p_blocks)
            else_script = build_scratch_script(substack_2_id, p_blocks)
            condition_script = build_scratch_script(condition_id, p_blocks)
            script.append(['control_if_else', condition_script, if_script, else_script])
        elif current_block['opcode'] == 'operator_equals':
            if len(current_block['inputs']['OPERAND1']) == 2:
                operand1 = current_block['inputs']['OPERAND1'][1][1]
            else:
                if isinstance(current_block['inputs']['OPERAND1'][1], str):
                    operand1_id = current_block['inputs']['OPERAND1'][1]
                    operand1 = build_scratch_script(operand1_id, p_blocks)
                elif str(current_block['inputs']['OPERAND1'][1][0]) == str(12): #straight variable
                    operand1 = current_block['inputs']['OPERAND1'][1][1]
                    operand1 = "VARIABLE_" + operand1
            if len(current_block['inputs']['OPERAND2']) == 2:
                operand2 = current_block['inputs']['OPERAND2'][1][1]
            else:
                if isinstance(current_block['inputs']['OPERAND2'][1], str):
                    operand2 = current_block['inputs']['OPERAND2'][1][1]
                    operand2 = "VARIABLE_" + operand2
                elif str(current_block['inputs']['OPERAND2'][1][0]) == str(12):  # straight variable
                    operand2_id = current_block['inputs']['OPERAND2'][1]
                    operand2 = build_scratch_script(operand2_id, p_blocks)
            script = [operand1, '=', operand2]
        elif current_block['opcode'] == 'looks_switchbackdropto':
            backdrop_id = current_block['inputs']['BACKDROP'][1]
            backdrop = build_scratch_script(backdrop_id, p_blocks)
            script = ['looks_switchbackdropto', backdrop]
        elif current_block['opcode'] == 'looks_nextbackdrop':
            script = 'looks_nextbackdrop'
        elif current_block['opcode'] == 'looks_backdrops':
            backdrop = current_block['fields']['BACKDROP'][0]
            script = [backdrop]
        elif current_block['opcode'] == 'operator_join':
            if len(current_block['inputs']['STRING1'][1]) == 2:  # no change
                string1 = current_block['inputs']['STRING1'][1][1]
            elif str(current_block['inputs']['STRING1'][1][0]) == str(12):  #this is a varialbe
                string1 = "VARIABLE_" + current_block['inputs']['STRING1'][1][1]
            elif str(current_block['inputs']['STRING1'][0]) == str(3):  #this is a another block
                next_id = current_block['inputs']['STRING1'][1]
                string1 = build_scratch_script(next_id, p_blocks)

            if len(current_block['inputs']['STRING2'][1]) == 2:
                string2 = current_block['inputs']['STRING2'][1][1]
            elif str(current_block['inputs']['STRING2'][1][0]) == str(12):  #this is a varialbe
                string2 = "VARIABLE_" + current_block['inputs']['STRING2'][1][1]
            elif str(current_block['inputs']['STRING2'][0]) == str(3):  #this is a another block
                next_id = current_block['inputs']['STRING2'][1]
                string2 = build_scratch_script(next_id, p_blocks)
            script = [str(string1) + str(string2)]
        next_block_id = current_block['next']
        current_block_id = next_block_id
    return script


def arrange_blocks_v2(p_json):
    """
    More or less the same, but taking the lessons I learned from Karel.
    Looks for a particular script in the code.  Algorithms:
    :param p_json: json info (as dictionary)
    :return: scripts - dictionary of scripts.  Keys are block ID's of parent.  values are lists of individual blocks
    under the parent
    """
    from app.scratch_labs.karel import build_karel_script

    scripts = {}
    repeat_scripts = {}
    operator_scripts = {}
    if_scripts = {}
    sprites = p_json['targets']
    for sprite in sprites:
        if 'blocks' in sprite:
            blocks = sprite['blocks']
            for block_id in blocks:
                block = blocks[block_id]
                if block['opcode'] == "control_repeat" or \
                        block['opcode'] == "control_forever" or \
                        block['opcode'] == "control_repeat_until":
                    print(f"yyy {block_id} building repeat_scripts  ")
                    if 'inputs' in block:
                        if 'SUBSTACK' in block['inputs']:
                            repeat_scripts[block_id] = [block['inputs']['SUBSTACK'][1]]
                elif block['opcode'] == "operator_equals":
                    print(f"yyy {block_id} building operator scripts now.   ") #This may be jacked see later.
                    if 'inputs' in block:
                        if 'OPERAND1' in block['inputs']:
                            operator_scripts[block_id] = [block['inputs']['OPERAND1'][1][1],
                                                          '=',
                                                          block['inputs']['OPERAND2'][1][1]]
                elif block['opcode'] == "control_if_else":
                    print(f"yyy {block_id} building if scripts now.   ")
                    if 'inputs' in block:
                        if 'SUBSTACK' in block['inputs']:
                            if_scripts[block_id] = [block['inputs']['CONDITION'][1],
                                                    block['inputs']['SUBSTACK'][1],
                                                    block['inputs']['SUBSTACK2'][1]]
                elif block['opcode'] == "procedures_definition":  # can skip, previous if does
                    continue
                elif block['parent']:
                    parent_id = block['parent']
                    parent_block = blocks[parent_id]
                    if parent_block['inputs']:
                        if parent_block['opcode'] == 'control_repeat' or \
                                parent_block['opcode'] == 'control_forever':
                            if 'SUBSTACK' in parent_block['inputs']:
                                print(f"yyy {block_id} this block has a parent with substack. This is a repeat ")
                                if parent_block['inputs']['SUBSTACK'][1] == block_id:
                                    script = build_scratch_script(block_id, blocks)
                                    temp_repeat_commands = []
                                    for item in script:
                                        print(f"IN A REPEAT STACK item['opcode']" + str(item))
                                        if item['opcode'] == 'event_whenbroadcastreceived':
                                            continue
                                        else:
                                            temp_repeat_commands.append(item['inputs']['SUBSTACK'][1])
                                    repeat_scripts[block_id] = temp_repeat_commands
                elif block['parent'] is None:
                    print(f"yyy {block_id} doing things without parents now.")
                    script = build_scratch_script(block_id, blocks)
                    scripts[block_id] = script
    return scripts


def match_string(regex, p_json, *, points=0, num_matches=1):
    """
    Tries to match regex inside the json.
    :param regex: Regex we are looking for
    :param p_json: json of all blocks in the code(dict).
    :param points: How many points this is worth (int).
    :param num_matches: how many times you want to match (int).
    :return: Dictionary of the test
    """
    import re

    found = len(re.findall(regex, str(p_json), re.X | re.M | re.S))

    p_test = {"name": "Looking for a string in code (" + str(points) + " points)<br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "We found this string in the code:  " + str(regex) + "<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Code does not find string we were looking for.<br>"
                              "Looked for this string: " + str(regex) + "<br>" +
                              "Looked in this code: " + str(p_json) + "<br>" +
                              "Found this many matches : " + str(found) + "<br>",
              "points": 0
              }
    if found >= num_matches:
        p_test['points'] += points
    else:
        p_test['pass'] = False
    return p_test


def extract_move_steps(p_json):
    """
    Extracts the steps inside the block.
    Will match the all integers.
    :param p_json:  - json of the block you are looking at
    :return: all matches, as a list of integers
    """
    import re

    regex = r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'(\d+)']]}"
    matches = re.findall(regex, str(p_json), re.X | re.M | re.S)
    if matches:
        return matches
    else:
        return []


def extract_turn_degrees(p_json):
    """
    Extracts the turn degrees inside the block.
    Will match the all integers integer.
    :param p_json:  - json of the block you are looking at
    :return: all matches, as a list of integers
    """
    import re

    regex = r"{'opcode':\s+'motion_turn(right|left)',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'(\d+)']]}"
    matches = re.findall(regex, str(p_json), re.X | re.M | re.S)
    if matches:
        return matches
    else:
        return []


def count_sprites(p_json):
    """
    Finds the number of sprites that are NOT background
    :param p_json:  - json of all code
    :return: all matches, as a list of integers
    """
    num_sprites = 0
    for target in p_json['targets']:
        if target['isStage'] is True:
            pass
        else:
            num_sprites += 1
    return num_sprites


def count_stage_changes(p_json):
    """
    Finds the number of times backdrop changes happen (does not work for repeats)
    :param p_json:  - json of all code
    :return: all matches, as a list of integers
    """
    import re
    for target in p_json['targets']:
        if target['isStage'] is True:
            matches = len(re.findall(r'(looks_switchcostumeto|looks_nextbackdrop)', str(p_json), re.X | re.M | re.S))
    return matches


def every_sprite_green_flag(p_json, p_points):
    """
    Verifies that every sprite has a green flag.
    :param p_json:  - json of all code
    :param p_points:  - points this is worth(int)
    :return: test dictionary
    """
    p_test = {"name": "Checking that every sprite has a green flag (" + str(p_points) + " points)<br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Every sprite has a green flag.  The green flag "
                              "will help you always start at the same place.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Every sprite does not have a green flag.  "
                              "The green flag will help you always start at the same place. <br>",
              "points": 0
              }
    for target in p_json['targets']:
        if target['isStage'] is True:
            pass
        else:
            if match_string(r'event_whenflagclicked', target)['pass'] is False:
                p_test['pass'] = False
                p_test['fail_message'] += 'This sprite does not have a green flag: ' + target['name'] + '<br>'
    if p_test['pass']:
        p_test['points'] += p_points
    return p_test


def every_sprite_broadcast_and_receive(p_json, p_points):
    """
    Verifies that every sprite has at least one broadcast and one receive.
    :param p_json:  - json of all code
    :param p_points:  - points this is worth(int)
    :return: test dictionary
    """
    p_test = {"name": "Checking that every sprite has a least one broadcast and one receive"
                      " (" + str(p_points) + " points)<br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Every sprite has at least one broadcast and one receive.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Not every sprite has a broadcast and receive.<br>"
                              "You should use broadcasts and receives instead of waits.  Broadcasts and receives will "
                              "work more reliably if you change your code around.<br>",
              "points": 0
              }
    for target in p_json['targets']:
        if target['isStage'] is True:
            pass
        else:
            if match_string(r'event_broadcast', target)['pass'] is False or \
                    match_string(r'event_whenbroadcastreceived', target)['pass'] is False:
                p_test['pass'] = False
                p_test['fail_message'] += 'This sprite does not have a broadcast AND a receive: ' + \
                                          target['name'] + '<br>'
    if p_test['pass']:
        p_test['points'] += p_points
    return p_test
