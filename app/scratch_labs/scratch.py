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
                    else:  # Do repeat blocks
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
        # print("KEY!!")
        # print(scripts[key])
    return scripts


#
# abc = [{'opcode': 'event_whenkeypressed', 'inputs': {}, 'fields': {'KEY_OPTION': ['2', None]}},
#        {'opcode': 'control_repeat', 'inputs': {'TIMES': [1, [6, '4']], 'SUBSTACK': [2, 'OXRKfvlR06`]@|XXen9}',
#                                                                                     [
#                                                                                         {'opcode': 'motion_movesteps', 'inputs': {'STEPS': [1, [4, '100']]}, 'fields': {}},
#                                                                                         {'opcode': 'motion_turnright', 'inputs': {'DEGREES': [1, [4, '90']]}, 'fields': {}},
#                                                                                         {'opcode': 'looks_say', 'inputs': {'MESSAGE': [1, [10, 'Hello!']]}, 'fields': {}},
#                                                                                         {'opcode': 'looks_think', 'inputs': {'MESSAGE': [1, [10, 'Hmm...']]}, 'fields': {}}
#                                                                                     ]
#                                                                                     ]
#                                                },
#         'fields': {}
#         },
#        {'opcode': 'looks_changesizeby', 'inputs': {'CHANGE': [1, [4, '10']]}, 'fields': {}},
#        {'opcode': 'looks_say', 'inputs': {'MESSAGE': [1, [10, 'Hello!']]}, 'fields': {}}]
#
# def = [{'opcode': 'event_whenkeypressed', 'inputs': {}, 'fields': {'KEY_OPTION': ['3', None]}},
#        {'opcode': 'control_repeat', 'inputs': {'TIMES': [1, [6, '2']], 'SUBSTACK': [2, 'p0Tz(va{*U$l$FsD/0ai',
#                                                                                     [{'opcode': 'control_repeat', 'inputs': {'TIMES': [1, [6, '2']], 'SUBSTACK': [2, '+Teeb|F1KHh7}3DM%6RO',
#                                                                                                                                                                   [{'opcode': 'motion_movesteps', 'inputs': {'STEPS': [1, [4, '100']]}, 'fields': {}},
#                                                                                                                                                                    {'opcode': 'motion_turnright', 'inputs': {'DEGREES': [1, [4, '90']]}, 'fields': {}}]]
#                                                                                                                              }, 'fields': {}},
#                                                                                      {'opcode': 'looks_changesizeby', 'inputs': {'CHANGE': [1, [4, '10']]}, 'fields': {}},
#                                                                                      {'opcode': 'looks_say', 'inputs': {'MESSAGE': [1, [10, 'Hello!']]}, 'fields': {}}]]}, 'fields': {}},
#        {'opcode': 'looks_changesizeby', 'inputs': {'CHANGE': [1, [4, '10']]}, 'fields': {}},
#        {'opcode': 'looks_say', 'inputs': {'MESSAGE': [1, [10, 'Hello!']]}, 'fields': {}}]
