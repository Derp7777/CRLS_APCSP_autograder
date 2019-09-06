import math

class brickLayer(object):
    def __init__(self, x, y, direction, *, pendown=True, draw_targets={}, variables={}):
        self.x = x
        self.y = y
        self.direction = math.radians(direction)
        self.draw_targets = draw_targets
        self.pendown = pendown
        self.move_history = [[self.x, self.y]]
        self.variables = variables
        self.say_history = ''

    def move(self, amount):
        print("start of move selfx {} selfy {} hist {}".format(self.x, self.y, self.move_history))

        orig_x = self.x
        orig_y = self.y
        amount = int(amount)
        self.y += round(math.cos(self.direction) * amount)
        self.x += round(math.sin(self.direction) * amount)
        print("end move selfx {} selfy {} hist {}".format(self.x, self.y, self.move_history))
        self.move_history.append([self.x, self.y])
        if self.pendown is True:

            if ((orig_x, orig_y), (self.x, self.y)) in self.draw_targets.keys():
                self.draw_targets[((orig_x, orig_y), (self.x, self.y))] = 0
                return True
            elif ((self.x, self.y), (orig_x, orig_y)) in self.draw_targets.keys():
                self.draw_targets[((self.x, self.y), (orig_x, orig_y))] = 0
                return True
            else:
                return False


    def turn(self, amount):
        self.direction += amount


def eval_boolean(p_boolean, p_sprite):
    """
    evaluates p_boolean given from scratch json, after simplifying
    :param p_boolean: the statement to evaluate
    :param p_sprite: sprite object(we will use the sprite variables)
    :return: True or False
    """
    import re

    print("aaa inside eval_boolean.  p_boolean {}".format(p_boolean))

    p_boolean = re.sub(",", '', p_boolean)
    p_boolean = re.sub('=', '==', p_boolean)
    p_boolean = sub_variables(p_boolean, p_sprite)
    print("aaa inside eval, after variable subs {}".format(p_boolean))
    words = p_boolean.split()
    p_boolean = ''
    print("aaa inside words {}".format(words))
    # got a blank?
    if len(words) == 2:
        if words[0] == '==' or words[0] == '>' or words[0] == '<':
            words.insert(0,"' '")
        else:
            words.append("' '")
    print("aaa inside wordsafter space check {}".format(words))

    for word in words:
        if word != '==' and word != '>' and word != '<':
            if re.search(r"[^a-zA-Z]", word):
                p_boolean += " " + word + " "  # numbers only
            else:
                p_boolean += "'" + word + "' "
        else:
            p_boolean += ' ' + word + ' '  # pass through ==, >, or <
    print("aaa inside   eval boolean{}".format(p_boolean))
    ret_val = eval(p_boolean)
    print(ret_val)
    return ret_val


def sub_variables(p_words, p_sprite):
    """
    Sub in variables to expressions
    :param p_words: words (such as VARIABLES_x is this)
    :param p_sprite: contains p_sprite.variables, which is the dictionary conversion of variables to values
    :return:
    """
    import re
    p_words = re.sub("'", '', p_words)
    p_words = re.sub(r"\[", '', p_words)
    p_words = re.sub("]", '', p_words)
    print('aaa in sub_variables, before subbing {}'.format(p_words))
    if re.search("VARIABLE_", p_words):
        for key in sorted(p_sprite.variables, key=len, reverse=True):
            #print("aaa key for subbing vars {}".format(key))
            match_string = r'VARIABLE_' + key
            match = re.search(match_string, p_words, re.X | re.M | re.S)
            if match:
                p_words = re.sub(match_string, str(p_sprite.variables[key]), p_words)
            # p_words = re.sub(sub_this, str(p_sprite.variables[variable_name]), p_words)
            words = p_words
            # print("aaa words after first sub {}".format(p_words))
    if re.search("sensing_answer", p_words):
        print('ccc sensing answer')
        if 'sensing_answer' not in p_sprite.variables.keys():
            raise Exception("Code has a sensing answer, but test does not. <br>"
                            "Students: Remove the question if you do'nt need it and do it a different way.<br>"
                            "Teacher: Create a sensing_answer variable in the sprite object.<br>")
        sensing_answers = True
        while sensing_answers:
            match_string = 'sensing_answer'
            # print("ccc p_words {}".format(p_words))
            match = re.search(match_string, p_words, re.X | re.M | re.S)
            if match:
                answer = p_sprite.variables['current_answer']
                p_words = re.sub(match_string, answer, p_words, 1)
            else:
                sensing_answers = False
    print("aaa after all variable substitutios {}".format(p_words))
    return p_words


def do_sprite(p_sprite, moves, success):
    """
    This function does the sprite movements
    :param p_sprite: The sprite object
    :param moves: moves sprite will try (list, looks like scripts in main code)
    :param success: What it returns  If false then exit right away
    :return: True/False depending on if crash or maximum fly exceeded.
    """
    import re
    import random
    if success is False:
        print("ccc exiting, success if false")
        return False
    print("aaa beginning of do sprite.  here are all  moves {} \n".format(moves))
    for i, move in enumerate(moves):
        print("next move is this {}\n".format(move))
        if isinstance(move, list):
            ret_val = do_sprite(p_sprite, moves[i], success)
            if ret_val is False:
                success = False
                break
        else:
            print("ggg  at beggining of loop not a list.  move is this{}".format(move))
            if move == 'event_whenkeypressed':
                break
            if move == 'motion_movesteps':
                amount = sub_variables(str(moves[i+1]), p_sprite)
#                 if re.search("VARIABLE_", moves[i+1]):
#                     print("uuu moves[i+1] {}".format(moves[i+1]))
#                     match = re.search(r"VARIABLE_(.+)", moves[i+1], re.X | re.M | re.S)
#                     variable_name = match.group(1)
#                     print("uuu variable name {}".format(variable_name))
#                     print("uuu  p_sprite.variables[variable_name] {}".format(p_sprite.variables[variable_name]))
# #                    amount = re.sub(r"VARIABLE_.+'", str(p_sprite.variables[variable_name]),  moves[i+1],
#                     #                re.X | re.M | re.S)
#                     amount = int(p_sprite.variables[variable_name])
#                     print("uuu amountf {}".format(amount))
#                 else:
#                     amount = moves[i+1]
                ret_val = p_sprite.move(amount)
                if ret_val is False:
                    print("RET VAL IS FALSE")
                    success = False
                break
            elif move == 'motion_turnleft':
                degrees = float(moves[i+1])
                degrees = -math.radians(degrees)
                p_sprite.turn(degrees)
                break
            elif move == 'motion_changeyby':
                dy = int(moves[i + 1])
                if p_sprite.pendown is True:
                    orig_x = p_sprite.x
                    orig_y = p_sprite.y
                p_sprite.y += dy
                if p_sprite.pendown is True:
                    if ((orig_x, orig_y), (p_sprite.x, p_sprite.y)) in p_sprite.draw_targets.keys():
                        p_sprite.draw_targets[((orig_x, orig_y), (p_sprite.x, p_sprite.y))] = 0
                        return True
                    elif ((p_sprite.x, p_sprite.y), (orig_x, orig_y)) in p_sprite.draw_targets.keys():
                        p_sprite.draw_targets[((p_sprite.x, p_sprite.y), (orig_x, orig_y))] = 0
                        return True
                    else:
                        return False
                break
            elif move == 'motion_changexby':
                dx = int(moves[i + 1])
                if p_sprite.pendown is True:
                    orig_x = p_sprite.x
                    orig_y = p_sprite.y
                p_sprite.x += dx
                if p_sprite.pendown is True:
                    if ((orig_x, orig_y), (p_sprite.x, p_sprite.y)) in p_sprite.draw_targets.keys():
                        p_sprite.draw_targets[((orig_x, orig_y), (p_sprite.x, p_sprite.y))] = 0
                        return True
                    elif ((p_sprite.x, p_sprite.y), (orig_x, orig_y)) in p_sprite.draw_targets.keys():
                        p_sprite.draw_targets[((p_sprite.x, p_sprite.y), (orig_x, orig_y))] = 0
                        return True
                    else:
                        return False
                break
            elif move == 'motion_setx':
                x = int(moves[i + 1])
                if p_sprite.pendown is True:
                    orig_x = p_sprite.x
                    orig_y = p_sprite.y
                p_sprite.x = x
                if p_sprite.pendown is True:
                    if ((orig_x, orig_y), (p_sprite.x, p_sprite.y)) in p_sprite.draw_targets.keys():
                        p_sprite.draw_targets[((orig_x, orig_y), (p_sprite.x, p_sprite.y))] = 0
                        return True
                    elif ((p_sprite.x, p_sprite.y), (orig_x, orig_y)) in p_sprite.draw_targets.keys():
                        p_sprite.draw_targets[((p_sprite.x, p_sprite.y), (orig_x, orig_y))] = 0
                        return True
                    else:
                        return False
                break
            elif move == 'data_setvariableto':
                print("ccc beginning of set variable to.   variable: {} value: {}".format(moves[i+1], moves[i+2]))
                key = moves[i + 1]
                value = moves[i + 2]
                if isinstance(value, list):
                    if str(value) == "['sensing_answer']":
                        value = p_sprite.variables['current_answer']
                    else:
                        value = do_sprite(p_sprite, value, success)
                value = str(value)
                value = sub_variables(value, p_sprite)
                p_sprite.variables[key] = value
                print('ccc variables after data_setvariableto after data set {}  '.format(p_sprite.variables))

                break
            elif move == 'data_changevariableby':
                variable_plus_variable = moves[1]
                print("aaa change variable.  Moves {} say_history {}".format(moves[2], p_sprite.say_history))
                delta_value = moves[2]
                if isinstance(moves[2], list):
                    ret_val = do_sprite(p_sprite, moves[2], success)
                    delta_value = ret_val
                else:
                    delta_value = moves[2]
                if re.search("\d \. \d", str(delta_value), re.X | re.M | re.S):
                    delta_value = float(delta_value)
                else:
                    delta_value = int(delta_value)
                variable = re.sub('VARIABLE_', '', variable_plus_variable)
                if variable in p_sprite.variables.keys():
                    if re.search("\d \. \d", str(p_sprite.variables[variable]), re.X | re.M | re.S):
                        p_sprite.variables[variable] = float(p_sprite.variables[variable])
                    else:
                        p_sprite.variables[variable] = int(p_sprite.variables[variable])
                    p_sprite.variables[variable] += delta_value
                else:
                    raise Exception("Tried to edit variable {}, but that variable does not exist.<br>".format(variable))
                print("changevariable by worked? {}".format(p_sprite.variables))
                break
            elif move == 'data_lengthoflist':
                list_name = moves[i + 1]
                list_length = len(p_sprite.variables[list_name])
                print("fff returning this for length of list {}".format(list_length))
                return list_length
            elif move == 'data_itemoflist':
                index = moves[i + 1]
                list_name = moves[i + 2]
                print("fff returning this for index {} list name {}".format(index, list_name))
                if isinstance(index, list):
                    index = do_sprite(p_sprite, index, success)
                index = sub_variables(str(index), p_sprite)
                print("iiu index {}".format(index))
                index = int(index)
                # print("fff index {}".format(index))
                if index - 1 < 0:
                    raise Exception("Index was 0 or lower (too low of number.\n"
                                    "  Did you try to 'say' 0th item of list or something like that?)")
                try:
                    item = p_sprite.variables[list_name][index - 1]
                except IndexError:
                    raise Exception("Index was out of range of list.  This means you are picking an item that is longer"
                                    " than the list.\n"
                                    "For example, you might be trying to pick item 10 of a 3 item list.\n"
                                    "Check the part of your code where it says 'item XXXX of LISTNAME' and probably "
                                    "the XXXX part is wrong.<br>"
                                    "ALTERNATIVELY, the code mostly works and it looks like it works in Scratch,"
                                    "but the counter goes too high at the very end or is too low at beginning.  \n"
                                    "We recommend to follow this template:\n"
                                    "1. Outside loop, set the counter to where you want it to start (1 if beginning of "
                                    "list)\n"
                                    "2. Inside loop, do your thing (for example say item of list) \n"
                                    "3. Change counter variable by 1 (or more, if you are skipping items in list).\n\n"
                                    "Another possibility is that you are hard coding your counter somewhere"
                                    "and it works for certain size lists but not small lists. ")
                return item
            elif move == 'data_deletealloflist':
                list_name = moves[i + 1]
                print("jjj data_deletealloflist")
                p_sprite.variables[list_name] = []

                break
            elif move == 'data_addtolist':
                item = moves[i + 1]
                list_name = moves[i + 2]
                print("jjj data-add_to_list")

                print("fff radding thisthis for item {} list name {}".format(item, list_name))
                if isinstance(item, list):
                    item = do_sprite(p_sprite, item, success)

                print("jjj item is this {}".format(item))
                item = sub_variables(str(item), p_sprite)
                p_sprite.variables[list_name].append(item)

                break
            elif move == 'data_deleteoflist':
                item = moves[i + 1]
                list_name = moves[i + 2]
                print("jjj datadelete_list")

                print("fff radding thisthis for item {} list name {}".format(item, list_name))
                if isinstance(item, list):
                    item = do_sprite(p_sprite, item, success)

                print("jjj item is this {}".format(item))
                item = int(sub_variables(str(item), p_sprite))
                p_sprite.variables[list_name].pop(item - 1)

                break
            if move == 'operator_random':
                if isinstance(moves[2], list) is False:
                    if abs(float(moves[1]) - round(float(moves[1]))) < .001 and \
                            abs(float(moves[2]) - round(float(moves[2]))) < .001:
                        rand_number = random.randint(int(moves[1]), int(moves[2]))
                    else:
                        rand_number = random.uniform(float(moves[1]), float(moves[2]))
                    print("returning this  rand num {}".format(rand_number))
                else:
                    upper_bound = do_sprite(p_sprite, moves[2], success)
                    print("ccc lower {} upper_bound{}".format(moves[1], upper_bound))

                    if abs(float(moves[1]) - round(float(moves[1]))) < .001 and \
                            abs(float(upper_bound) - round(float(upper_bound))) < .001:
                        rand_number = random.randint(int(moves[1]), int(upper_bound))
                    else:
                        rand_number = random.uniform(float(moves[1]), float(upper_bound))
                    print("returning this  for randnumber {}".format(rand_number))
                return rand_number
            elif move == 'operator_subtract':
                if isinstance(moves[1], list):
                    num1 = do_sprite(p_sprite, moves[1], success)
                else:
                    num1 = moves[1]
                if isinstance(moves[2], list):
                    num2 = do_sprite(p_sprite, moves[2], success)
                else:
                    num2 = moves[2]
                num1 = sub_variables(str(num1), p_sprite)
                num2 = sub_variables(str(num2), p_sprite)
                try:
                    temp = float(num1)
                except ValueError:
                    raise Exception("First number of subtraction can't be converted to int.  Number is: {}"
                                    .format(num1))
                try:
                    temp = float(num2)
                except ValueError:
                    raise Exception("Second number of subtraction can't be converted to int.  Number is: {}"
                                    .format(num2))
                tol = 0.01
                if abs(round(float(num1)) - float(num1)) < tol:
                    num1 = int(num1)
                else:
                    num1 = float(num1)
                if abs(round(float(num2)) - float(num2)) < tol:
                    num2 = int(num2)
                else:
                    num2 = float(num2)
                evaluated = num1 - num2
                print("jjj ran operator_subtract and got this {}".format(evaluated))
                return evaluated
            elif move == 'operator_equals':
                print("operator_equals moves {}".format(moves))
                if isinstance(moves[1], list):
                    num1 = do_sprite(p_sprite, moves[1], success)
                else:
                    num1 = moves[1]
                if isinstance(moves[2], list):
                    num2 = do_sprite(p_sprite, moves[2], success)
                else:
                    num2 = moves[2]
                print("operator_equals pre sub num1 {} num2 {}".format(num1, num2))
                num1 = sub_variables(str(num1), p_sprite)
                num2 = sub_variables(str(num2), p_sprite)
                print("operator_equals post sub num1 {} num2 {}".format(num1, num2))
                #
                # try:
                #     temp = float(num1)
                # except ValueError:
                #     raise Exception("First number of subtraction can't be converted to int.  Number is: {}"
                #                     .format(num1))
                # try:
                #     temp = float(num2)
                # except ValueError:
                #     raise Exception("Second number of subtraction can't be converted to int.  Number is: {}"
                #                     .format(num2))
                # tol = 0.01
                # if abs(round(float(num1)) - float(num1)) < tol:
                #     num1 = int(num1)
                # else:
                #     num1 = float(num1)
                # if abs(round(float(num2)) - float(num2)) < tol:
                #     num2 = int(num2)
                # else:
                #     num2 = float(num2)
                evaluated = num1 == num2
                print("jjj ran operator_equals and got this {}".format(evaluated))
                return evaluated
            elif move == 'operator_gt':
                print("operator_gt moves {}".format(moves))
                if isinstance(moves[1], list):
                    num1 = do_sprite(p_sprite, moves[1], success)
                else:
                    num1 = moves[1]
                if isinstance(moves[2], list):
                    num2 = do_sprite(p_sprite, moves[2], success)
                else:
                    num2 = moves[2]
                #print("operator_gt pre sub num1 {} num2 {}".format(num1, num2))
                num1 = sub_variables(str(num1), p_sprite)
                num2 = sub_variables(str(num2), p_sprite)
                #print("operator_gt post sub num1 {} num2 {}".format(num1, num2))

                try:
                    temp = float(num1)
                except ValueError:
                    raise Exception("First number of subtraction can't be converted to int.  Number is: {}"
                                    .format(num1))
                try:
                    temp = float(num2)
                except ValueError:
                    raise Exception("Second number of subtraction can't be converted to int.  Number is: {}"
                                    .format(num2))
                tol = 0.01
                if abs(round(float(num1)) - float(num1)) < tol:
                    num1 = int(num1)
                else:
                    num1 = float(num1)
                if abs(round(float(num2)) - float(num2)) < tol:
                    num2 = int(num2)
                else:
                    num2 = float(num2)
                evaluated = num1 > num2
                print("jjj ran operator_gt and got this {}".format(evaluated))
                return evaluated
            elif move == 'operator_lt':
                print("operator_lt moves {}".format(moves))
                if isinstance(moves[1], list):
                    num1 = do_sprite(p_sprite, moves[1], success)
                else:
                    num1 = moves[1]
                if isinstance(moves[2], list):
                    num2 = do_sprite(p_sprite, moves[2], success)
                else:
                    num2 = moves[2]
                print("operator_lt pre sub num1 {} num2 {}".format(num1, num2))
                num1 = sub_variables(str(num1), p_sprite)
                num2 = sub_variables(str(num2), p_sprite)
                print("operator_lt post sub num1 {} num2 {}".format(num1, num2))

                try:
                    temp = float(num1)
                except ValueError:
                    raise Exception("First number of subtraction can't be converted to int.  Number is: {}"
                                    .format(num1))
                try:
                    temp = float(num2)
                except ValueError:
                    raise Exception("Second number of subtraction can't be converted to int.  Number is: {}"
                                    .format(num2))
                tol = 0.01
                if abs(round(float(num1)) - float(num1)) < tol:
                    num1 = int(num1)
                else:
                    num1 = float(num1)
                if abs(round(float(num2)) - float(num2)) < tol:
                    num2 = int(num2)
                else:
                    num2 = float(num2)
                evaluated = num1 < num2
                print("jjj ran operator_lt and got this {}".format(evaluated))
                return evaluated
            elif move == 'operator_and':
                print("operator_and moves {}".format(moves))
                if isinstance(moves[1], list):
                    num1 = do_sprite(p_sprite, moves[1], success)
                else:
                    num1 = moves[1]
                if isinstance(moves[2], list):
                    num2 = do_sprite(p_sprite, moves[2], success)
                else:
                    num2 = moves[2]
                print("operator_and pre sub num1 {} num2 {}".format(num1, num2))
                if not isinstance(num1, bool):
                    num1 = sub_variables(str(num1), p_sprite)

                if not isinstance(num2, bool):
                    num2 = sub_variables(str(num2), p_sprite)
                print("operator_and post sub num1 {} num2 {}".format(num1, num2))

                # try:
                #     temp = float(num1)
                # except ValueError:
                #     raise Exception("First number of subtraction can't be converted to int.  Number is: {}"
                #                     .format(num1))
                # try:
                #     temp = float(num2)
                # except ValueError:
                #     raise Exception("Second number of subtraction can't be converted to int.  Number is: {}"
                #                     .format(num2))
                # tol = 0.01
                # if abs(round(float(num1)) - float(num1)) < tol:
                #     num1 = int(num1)
                # else:
                #     num1 = float(num1)
                # if abs(round(float(num2)) - float(num2)) < tol:
                #     num2 = int(num2)
                # else:
                #     num2 = float(num2)
                evaluated = num1 and num2
                print("jjj ran operator_and and got this {}".format(evaluated))
                return evaluated
            elif move == 'operator_or':
                print("operator_or moves {}".format(moves))
                if isinstance(moves[1], list):
                    num1 = do_sprite(p_sprite, moves[1], success)
                else:
                    num1 = moves[1]
                if isinstance(moves[2], list):
                    num2 = do_sprite(p_sprite, moves[2], success)
                else:
                    num2 = moves[2]
                print("operator_or pre sub num1 {} num2 {} {} {}".format(num1, num2, type(num1), type(num2)))
                if not isinstance(num1, bool):
                    num1 = sub_variables(str(num1), p_sprite)
                if not isinstance(num2, bool):
                    num2 = sub_variables(str(num2), p_sprite)
                print("operator_or post sub num1 {} num2 {} {} {}".format(num1, num2, type(num1), type(num2)))

                # try:
                #     temp = float(num1)
                # except ValueError:
                #     raise Exception("First number of subtraction can't be converted to int.  Number is: {}"
                #                     .format(num1))
                # try:
                #     temp = float(num2)
                # except ValueError:
                #     raise Exception("Second number of subtraction can't be converted to int.  Number is: {}"
                #                     .format(num2))
                # tol = 0.01
                # if abs(round(float(num1)) - float(num1)) < tol:
                #     num1 = int(num1)
                # else:
                #     num1 = float(num1)
                # if abs(round(float(num2)) - float(num2)) < tol:
                #     num2 = int(num2)
                # else:
                #     num2 = float(num2)

                evaluated = num1 or num2
                # evaluated = bool(evaluated)

                print("jjj ran operator_or and got this {} {}".format(evaluated, type(evaluated)))
                return evaluated
            elif move == 'operator_mod':
                if isinstance(moves[1], list):
                    num1 = do_sprite(p_sprite, moves[1], success)
                else:
                    num1 = moves[1]
                if isinstance(moves[2], list):
                    num2 = do_sprite(p_sprite, moves[2], success)
                else:
                    num2 = moves[2]
                num1 = sub_variables(str(num1), p_sprite)
                num2 = sub_variables(str(num2), p_sprite)
                try:
                    temp = float(num1)
                except ValueError:
                    raise Exception("First number of mod can't be converted to float.  Number is: {}"
                                    .format(num1))
                try:
                    temp = float(num2)
                except ValueError:
                    raise Exception("Second number of mod can't be converted to int.  Number is: {}"
                                    .format(num2))
                tol = 0.01
                if abs(round(float(num1)) - float(num1)) < tol:
                    num1 = int(num1)
                else:
                    num1 = float(num1)
                if abs(round(float(num2)) - float(num2)) < tol:
                    num2 = int(num2)
                else:
                    num2 = float(num2)
                print("aaa mod numbers are this num1 {} num2 {}".format(num1, num2))
                evaluated = num1 % num2
                print("jjj ran operator_mod and got this {}".format(evaluated))
                return evaluated
            elif move == 'operator_divide':
                if isinstance(moves[1], list):
                    num1 = do_sprite(p_sprite, moves[1], success)
                else:
                    num1 = moves[1]
                if isinstance(moves[2], list):
                    num2 = do_sprite(p_sprite, moves[2], success)
                else:
                    num2 = moves[2]
                num1 = sub_variables(str(num1), p_sprite)
                num2 = sub_variables(str(num2), p_sprite)

                print("this is what I got num1 {} num2 {}".format(num1, num2))
                try:
                    temp = float(num1)
                except ValueError:
                    raise Exception("First number of subtraction can't be converted to int.  Number is: {}"
                                    .format(num1))
                try:
                    temp = float(num2)
                except ValueError:
                    raise Exception("Second number of subtraction can't be converted to int.  Number is: {}"
                                    .format(num2))
                tol = 0.01
                if abs(round(float(num1)) - float(num1)) < tol:
                    num1 = int(num1)
                else:
                    num1 = float(num1)
                if abs(round(float(num2)) - float(num2)) < tol:
                    num2 = int(num2)
                else:
                    num2 = float(num2)
                evaluated = num1 / num2
                print("jjj ran operator_divide and got this {}".format(evaluated))
                return evaluated
            elif move == 'operator_multiply':
                if isinstance(moves[1], list):
                    num1 = do_sprite(p_sprite, moves[1], success)
                else:
                    num1 = moves[1]
                if isinstance(moves[2], list):
                    num2 = do_sprite(p_sprite, moves[2], success)
                else:
                    num2 = moves[2]
                num1 = sub_variables(str(num1), p_sprite)
                num2 = sub_variables(str(num2), p_sprite)

                try:
                    temp = float(num1)
                except ValueError:
                    raise Exception("First number of subtraction can't be converted to int.  Number is: {}"
                                    .format(num1))
                try:
                    temp = float(num2)
                except ValueError:
                    raise Exception("Second number of subtraction can't be converted to int.  Number is: {}"
                                    .format(num2))
                tol = 0.01
                if abs(round(float(num1)) - float(num1)) < tol:
                    num1 = int(num1)
                else:
                    num1 = float(num1)
                if abs(round(float(num2)) - float(num2)) < tol:
                    num2 = int(num2)
                else:
                    num2 = float(num2)
                evaluated = num1 * num2
                print("jjj ran operator_multiply and got this {}".format(evaluated))
                return evaluated

            elif move == 'operator_length':
                if isinstance(moves[1], list):
                    operator_string = do_sprite(p_sprite, moves[1], success)
                else:
                    operator_string = moves[1]
                operator_string = sub_variables(str(operator_string), p_sprite )
                print("iii operator_length l string is {} length is {}".format(operator_string, len(operator_string)))
                return len(operator_string)
            elif move == 'operator_letter_of':
                print("tried operator letter of")
                if isinstance(moves[1], list):
                    number = do_sprite(p_sprite, moves[1], success)
                else:
                    number = moves[1]
                print("aaa number {}".format(number))
                number = str(number)
                number = sub_variables(number, p_sprite)
                try:
                    number = int(number)
                except ValueError:
                    raise Exception("Your number for operator_letter_of isn't an integer?  Got this: {}".
                                    format(moves[1]))
                if isinstance(moves[2], list):
                    operator_string = do_sprite(p_sprite, moves[2], success)
                else:
                    operator_string = moves[2]
                operator_string = sub_variables(str(operator_string), p_sprite)
                if number - 1 < 0 or number > len(operator_string):
                    raise Exception("Tried to get letter more or less than word. Number is: {} word is : {}".
                                    format(number, operator_string))
                return operator_string[number - 1].lower()
            elif move == 'operator_add':
                if isinstance(moves[1], list):
                    num1 = do_sprite(p_sprite, moves[1], success)
                else:
                    num1 = moves[1]
                if isinstance(moves[2], list):
                    num2 = do_sprite(p_sprite, moves[2], success)
                else:
                    num2 = moves[2]
                num1 = sub_variables(str(num1), p_sprite)
                num2 = sub_variables(str(num2), p_sprite)

                try:
                    temp = float(num1)
                except ValueError:
                    raise Exception("First number of addition can't be converted to int.  Number is: {}"
                                    .format(num1))
                try:
                    temp = float(num2)
                except ValueError:
                    raise Exception("Second number of addition can't be converted to int.  Number is: {}"
                                    .format(num2))
                tol = 0.01
                if abs(round(float(num1)) - float(num1)) < tol:
                    num1 = int(num1)
                else:
                    num1 = float(num1)
                if abs(round(float(num2)) - float(num2)) < tol:
                    num2 = int(num2)
                else:
                    num2 = float(num2)
                evaluated = num1 + num2
                return evaluated
            elif move == 'pen_penUp':
                p_sprite.pendown = False
            elif move == 'pen_penDown':
                p_sprite.pendown = True

            elif move == 'motion_turnright':
                degrees = float(moves[i+1])
                degrees = math.radians(degrees)
                p_sprite.turn(degrees)
                break    
            elif move == 'looks_sayforsecs':
                print("looks_say. beginning entire list " + str(moves))
                print("looks say i is this {}".format(i))
                say_this = moves[i+1]

                print("what is saying?  Type?  {}".format(type(moves[i+1])))
                if isinstance(say_this, list):
                    ret_val = do_sprite(p_sprite, say_this, success)
                    print('ggg say this {}'.format(ret_val))
                    words_pre_sub = ret_val
                else:
                    words_pre_sub = str(moves[i+1])
                print("looks_say.  beginning efore subbing words" + str(words_pre_sub))
                words = words_pre_sub
                if isinstance(words_pre_sub, str):
                    words_pre_sub = re.sub("'", '', words_pre_sub)
                    words_pre_sub = re.sub(r"\[", '', words_pre_sub)
                    words_pre_sub = re.sub("]", '', words_pre_sub)
                    print('aaa presub words {}'.format(words_pre_sub))
                    if re.search("VARIABLE_", words_pre_sub) :
                        for key in sorted(p_sprite.variables, key=len, reverse=True):
                            # print("aaa key for subbing vars {}".format(key))
                            match_string = r'VARIABLE_' + key
                            match = re.search(match_string, words_pre_sub, re.X | re.M | re.S)
                            if match:
                                words_pre_sub = re.sub(match_string, str(p_sprite.variables[key]), words_pre_sub)
                            # words_pre_sub = re.sub(sub_this, str(p_sprite.variables[variable_name]), words_pre_sub)
                            words = words_pre_sub
                            print("aaa words after first sub {}".format(words_pre_sub))
                    # match = re.search(r"VARIABLE_(.+) \s", words_pre_sub, re.X | re.M | re.S)
                        # if match:
                        #     variable_name = match.group(1)
                        # match = re.search(r"VARIABLE_(.+?)'", words_pre_sub, re.X | re.M | re.S)
                        # if match:
                        #     variable_name = match.group(1)
                        # sub_this = r'VARIABLE_' + variable_name
                        # print("fff subthis {}".format(sub_this))
                        # words_pre_sub = re.sub(sub_this, str(p_sprite.variables[variable_name]), words_pre_sub)
                        # words = words_pre_sub
                    else:
                        words = words_pre_sub
                p_sprite.say_history += str(words) + "\n"
                print("pppo {}".format(p_sprite.say_history))
                break
            elif move == 'sensing_answer':
                return 'sensing_answer'
            elif move == 'sensing_askandwait':
                p_sprite.variables['current_answer'] = p_sprite.variables['sensing_answer'].pop(0)
                print("ooo current answer is this {}".format(p_sprite.variables['current_answer']))
            elif move == 'join':
                string1 = moves[i+1]
                if isinstance(string1, list):
                    ret_val1 = do_sprite(p_sprite, string1, success)
                    string1 = ret_val1
                string2 = moves[i+2]
                if isinstance(string2, list):
                    ret_val2 = do_sprite(p_sprite, string2, success)
                    string2 = ret_val2
                print("uuu join string1 {} string2 {} and both {}".format(string1, string2, string1 + string2))

                return string1 + string2
            elif move == 'control_if_else':
                print("ooo found a control if_else moves{}  i{}".format(moves, i))
                operator = moves[i + 1]
                operator_result = do_sprite(p_sprite, operator, success)
                # operator_result = bool(operator_result)
                print("aaa in control_if_else, result of operator {} and type {} ".format(operator_result,
                                                                                   type(operator_result)))
                # print("pieces of operator left {} middle  {} rigth {} ".format(operator[0], operator[1], operator[2]))
                # if isinstance(operator[0], list):
                #     left = str(do_sprite(p_sprite, operator[0], success))
                # else:
                #     left = str(operator[0])
                # if isinstance(operator[2], list):
                #     right = str(do_sprite(p_sprite, operator[2], success))
                # else:
                #     right = str(operator[2])
                # middle = do_sprite(p_sprite, operator[1], success)
                # all_list = [left, middle, right]
                # print("inside control if/else This is the operator {} all_list {}".format(operator, all_list))
                # condition = eval_boolean(str(all_list), p_sprite)
                # if condition:
                #     ret_val = do_sprite(p_sprite, moves[2], success)
                # else:
                #     ret_val = do_sprite(p_sprite, moves[3], success)
                print("two sets of moves moves2 {} moves 3 {}".format(moves[2], moves[3]))

                if operator_result:
                    print("aaa operator_result is true")
                    ret_val = do_sprite(p_sprite, moves[2], success)
                else:
                    print("aaa operator_result is false aaa{}aaa".format(operator_result))

                    ret_val = do_sprite(p_sprite, moves[3], success)
                break
            elif move == 'control_if':
                print("ooo control_if moves{}  i{}".format(moves, i))
                operator = moves[i + 1]
                operator_result = do_sprite(p_sprite, operator, success)
                print("aaa in control_if, result of operator {} ".format(operator_result))
                #operator_result = bool(operator_result)

                if operator_result:
                    ret_val = do_sprite(p_sprite, moves[2], success)
                break
            # if isinstance(operator[0], list):
            #         left = str(do_sprite(p_sprite, operator[0], success))
            #     else:
            #         left = str(operator[0])
            #     if isinstance(operator[2], list):
            #         right = str(do_sprite(p_sprite, operator[2], success))
            #     else:
            #         right = str(operator[2])
            #     middle = operator[1]
            #     all_list = [left, middle, right]
            #     print("This is the operator {}".format(all_list))
            #     condition = eval_boolean(str(all_list), p_sprite)
            #     if condition:
            #         ret_val = do_sprite(p_sprite, moves[2], success)
            #     break
            elif move == 'control_repeat':
                times = int(moves[i + 1])
                for _ in range(times):
                    print("ooo repeat time {_}")
                    ret_val = do_sprite(p_sprite, moves[2], success)
                    if ret_val is False:
                        success = False
                        break
                break
            elif move == 'control_repeat_until':
#                condition = moves[1]
                operator = moves[i + 1]
                print("ffff in repeat until operator {}".format(operator))
                operator_result = do_sprite(p_sprite, operator, success)

 #               new_condition = []
 #                for x in condition:
 #                    if isinstance(x, list):
 #                        ret_val = do_sprite(p_sprite, x, success)
 #                        new_condition.append(ret_val)
 #                    else:
 #                        new_condition.append(x)
 #                print('oooo new condition {}  {}'.format(new_condition, type(new_condition)))
 #                new_condition = str(new_condition)
 #                true_false = eval_boolean(new_condition, p_sprite)
 #                print("ooo condition {}".format(true_false))
                wu_counter = 1
                while operator_result is False:
                    print("repeat until move is this {}".format(moves[2]))
                    print("variables are this {}".format(p_sprite.variables))
                    print("ppp what is say hist".format(p_sprite.say_history))

                    ret_val = do_sprite(p_sprite, moves[2], success)
                    print("finished a loop variables {}".format(p_sprite.variables))
                    print("ppp what is say hist".format(p_sprite.say_history))
                    operator_result = do_sprite(p_sprite, operator, success)
                    #true_false = eval_boolean(new_condition, p_sprite)
                    print("ppp wu counter {}".format(wu_counter))
                    wu_counter += 1
                    if wu_counter > 1000:
                        break
                break
            elif re.search('VARIABLE_', move):
                return move
            elif move == '=':
                return move
            else:
                print("xxx this move did not get done {}".format(move))
    return success


def press_zero(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch import match_string

    p_test = {"name": "Checking that there is a script that has 'when 0 key is pressed' along with a "
                      "pen down, goto -160 -180, clear, and point 90. (" + str(p_points) + " points)<br>",
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
    test_goto = match_string(r"\['event_whenkeypressed', \s* '0'] .+ \['motion_gotoxy', \s '-160', \s '-180'],",
                             p_scripts)
    if test_goto['pass'] is False:
        p_test['fail_message'] += "Did not find a when 0 pressed followed by goto -160 -180.<br>"
    test_color = match_string(r"\['event_whenkeypressed', \s* '0'] .+ \['pen_setPenColorToColor'",
                              p_scripts)
    if test_color['pass'] is False:
        p_test['fail_message'] += "Did not find a when 0 pressed followed by changing of pen color.<br>"
    if test_pendown['pass'] and test_clear['pass'] and test_point['pass'] and test_goto['pass'] and test_color['pass']:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def press_one(p_scripts, p_points):
    from app.scratch_labs.scratch import match_string

    p_test = {"name": "Checking that there is a script that has 'when 1 key is pressed' and that this "
                      "script draws a single brick, assuming 0 is pressed first "
                      "(" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Script that has 'when 1 key is pressed' draws a single brick"
                              " (assuming 0 is pressed first).<br>"
                              "Script also has a repeat with the correct number of times.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Script that has 'when 1 key is pressed does NOT draw a single brick"
                              " (assuming 0 is pressed first)<br>"
                              "OR, script does not have a repeat with correct number of times.<br>"
                              "OR, script draws too many lines.<br>"
                              "OR, a combination of all three.<br>"
                              "Checker assumes you pressed 0 first, so you start in bottom left corner.<br><br>",
              "points": 0
              }
    t_list = (
        ((-160, -180), (-120, -180)), ((-120, -180), (-120, -160)), ((-120, -160), (-160, -160)), ((-160, -180),
                                                                                                   (-160, -160))
    )

    target_dict = {}
    for target in t_list:
        if target not in target_dict.keys():
            target_dict[target] = 1
    sprite = brickLayer(-160, -180, 90, draw_targets=target_dict)
    success = False
    for key in p_scripts:
        script = p_scripts[key]
        if script[0] == ['event_whenkeypressed', '1']:
            success = do_sprite(sprite, script, True)
            if success:
                break

    find_repeat = match_string(r"\['event_whenkeypressed', \s* '1'], .+ \['control_repeat', \s '2'", p_scripts)
    if find_repeat['pass'] is False:
        p_test['fail_message'] += "Did not find a repeat with the correct number of times in the script. <br>"
    if success is False:
        p_test['fail_message'] += 'Drew too many lines.<br>'
    if 1 in sprite.draw_targets.values():
        p_test['fail_message'] += 'Did not draw enough lines.<br>'
    if success is False or 1 in target_dict.values():
        p_test['fail_message'] += 'Key: Start location, end location, whether or not this line was ' \
                                  'not drawn (1 = not drawn, 0 = drawn).<br>' \
                                  'Line status:<br>'
        for key in target_dict:
            p_test['fail_message'] += str(key) + ": " + str(target_dict[key]) + "<br>"
    if success and find_repeat['pass'] and 1 not in target_dict.values():
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def press_two(p_scripts, p_points):
    from app.scratch_labs.scratch import match_string

    p_test = {"name": "Checking that there is a script that has 'when 2 key is pressed' and that this "
                      "script draws a two bricks, assuming 0 is pressed first "
                      "(" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Script that has 'when 2 key is pressed' draws two bricks"
                              " (assuming 0 is pressed first).<br>"
                              "Script also has a repeat with the correct number of times.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Script that has 'when 2 key is pressed does NOT draw two bricks"
                              " (assuming 0 is pressed first)<br>"
                              "OR, script does not have a repeat with correct number of times.<br>"
                              "OR, script draws too many lines.<br>"
                              "OR, a combination of all three.<br>"
                              "Checker assumes you pressed 0 first, so you start in bottom left corner.<br><br>",
              "points": 0
              }
    target_list = (
        ((-160, -180), (-120, -180)), ((-120, -180), (-120, -160)), ((-120, -160), (-160, -160)), ((-160, -180),
                                                                                                   (-160, -160)),
        ((-120, -180), (-80, -180)), ((-80, -180), (-80, -160)), ((-80, -160), (-120, -160)), ((-120, -180),
                                                                                               (-120, -160)))
    target_dict = {}
    for target in target_list:
        if target not in target_dict.keys():
            target_dict[target] = 1
    sprite = brickLayer(-160, -180, 90, draw_targets=target_dict)
    success = False
    for key in p_scripts:
        script = p_scripts[key]
        if script[0] == ['event_whenkeypressed', '2']:
            success = do_sprite(sprite, script, True)
            print("success? {} ".format(success))
            if success:
                break
    # print("ggg sprite.x {} sprite.y {} dir {} targets {}".format(sprite.x, sprite.y, sprite.direction,
    #                                                              sprite.draw_targets))
    find_repeat = match_string(r"\['event_whenkeypressed', \s* '2'], .+ \['control_repeat', \s '2'", p_scripts)
    if find_repeat['pass'] is False:
        p_test['fail_message'] += "Did not find a repeat with the correct number of times in the script. <br>"
    if success is False:
        p_test['fail_message'] += 'Drew too many lines.<br>'
    if 1 in sprite.draw_targets.values():
        p_test['fail_message'] += 'Did not draw enough lines.<br>'
    if success is False or 1 in sprite.draw_targets.values():
        p_test['fail_message'] += 'Key: Start location, end location, whether or not this line was ' \
                                  'not drawn (1 = not drawn, 0 = drawn).<br>' \
                                  'Line status:<br>'
        for key in target_dict:
            p_test['fail_message'] += str(key) + ": " + str(target_dict[key]) + "<br>"
    if success and find_repeat['pass'] and 1 not in sprite.draw_targets.values():
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def press_three(p_scripts, p_points):
    from app.scratch_labs.scratch import match_string

    p_test = {"name": "Checking that there is a script that has 'when 3 key is pressed' and that this "
                      "script draws 8 bricks, assuming 0 is pressed first "
                      "(" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Script that has 'when 3 key is pressed' draws 8 bricks"
                              " (assuming 0 is pressed first).<br>"
                              "Script also has a repeat with the correct number of times.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Script that has 'when 3 key is pressed does NOT draw 8 bricks"
                              " (assuming 0 is pressed first)<br>"
                              "OR, script does not have a repeat with correct number of times.<br>"
                              "OR, script draws too many lines.<br>"
                              "OR, a combination of all three.<br>"
                              "Checker assumes you pressed 0 first, so you start in bottom left corner.<br><br>",
              "points": 0
              }
    target_list = (
        ((-160, -180), (-120, -180)), ((-120, -180), (-120, -160)), ((-120, -160), (-160, -160)), ((-160, -180),
                                                                                                   (-160, -160)),
        ((-120, -180), (-80, -180)), ((-80, -180), (-80, -160)), ((-80, -160), (-120, -160)), ((-120, -180),
                                                                                               (-120, -160)),
        ((-80, -180), (-40, -180)), ((-40, -180), (-40, -160)), ((-40, -160), (-80, -160)), ((-80, -180),
                                                                                             (-80, -160)),
        ((-40, -180), (0, -180)), ((0, -180), (0, -160)), ((0, -160), (-40, -160)), ((-40, -180),
                                                                                     (-40, -160)),
        ((0, -180), (40, -180)), ((40, -180), (40, -160)), ((40, -160), (0, -160)), ((0, -180), (0, -160)),
        ((40, -180), (80, -180)), ((80, -180), (80, -160)), ((80, -160), (40, -160)), ((40, -180), (40, -160)),
        ((80, -180), (120, -180)), ((120, -180), (120, -160)), ((120, -160), (80, -160)), ((80, -180), (80, -160)),
        ((120, -180), (160, -180)), ((160, -180), (160, -160)), ((160, -160), (120, -160)), ((120, -180), (120, -160)))

    target_dict = {}
    for target in target_list:
        if target not in target_dict.keys():
            target_dict[target] = 1
    print(target_dict)
    sprite = brickLayer(-160, -180, 90, draw_targets=target_dict)
    success = False
    for key in p_scripts:
        script = p_scripts[key]
        if script[0] == ['event_whenkeypressed', '3']:
            print("here we go 3")
            success = do_sprite(sprite, script, True)
            print("success? {} ".format(success))
            if success:
                break
    # print("ggg sprite.x {} sprite.y {} dir {} targets {}".format(sprite.x, sprite.y, sprite.direction,
    #                                                              sprite.draw_targets))
    find_repeat_1 = match_string(r"\['event_whenkeypressed', \s* '3'], .+ \['control_repeat', \s '2'", p_scripts)
    find_repeat_2 = match_string(r"\['event_whenkeypressed', \s* '3'], .+ \['control_repeat', \s '8'", p_scripts)
    if find_repeat_1['pass'] is False or find_repeat_2['pass'] is False:
        p_test['fail_message'] += "Did not find two repeat with the correct number of times in the script. <br>"
    if success is False:
        p_test['fail_message'] += 'Drew too many lines.<br>'
    if 1 in sprite.draw_targets.values():
        p_test['fail_message'] += 'Did not draw enough lines.<br>'
    if success is False or 1 in sprite.draw_targets.values():
        p_test['fail_message'] += 'Key: Start location, end location, whether or not this line was ' \
                                  'not drawn (1 = not drawn, 0 = drawn).<br>' \
                                  'Line status:<br>'
        for key in target_dict:
            p_test['fail_message'] += str(key) + ": " + str(target_dict[key]) + "<br>"
    if success and find_repeat_1['pass'] and find_repeat_2['pass'] and 1 not in sprite.draw_targets.values():
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def press_four(p_scripts, p_points):
    from app.scratch_labs.scratch import match_string

    p_test = {"name": "Checking that there is a script that has 'when 4 key is pressed' and that this "
                      "script draws an entire brick road, assuming 0 is pressed first "
                      "(" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Script that has 'when 4 key is pressed' draws a road of bricks"
                              " (assuming 0 is pressed first).<br>"
                              "Script also has a repeat with the correct number of times.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Script that has 'when 4 key is pressed does NOT draw an entire road of bricks"
                              " (assuming 0 is pressed first)<br>"
                              "OR, script does not have a repeat with correct number of times.<br>"
                              "OR, script draws too many lines.<br>"
                              "OR, a combination of all three.<br>"
                              "Checker assumes you pressed 0 first, so you start in bottom left corner.<br><br>",
              "points": 0
              }
    t_list = (((-160, -180), (-120, -180)), ((-120, -180), (-120, -160)), ((-120, -160), (-160, -160)),
              ((-160, -160), (-160, -180)), ((-120, -180), (-80, -180)), ((-80, -180), (-80, -160)),
              ((-80, -160), (-120, -160)), ((-120, -160), (-120, -180)), ((-80, -180), (-40, -180)),
              ((-40, -180), (-40, -160)), ((-40, -160), (-80, -160)), ((-80, -160), (-80, -180)),
              ((-40, -180), (0, -180)), ((0, -180), (0, -160)), ((0, -160), (-40, -160)),
              ((-40, -160), (-40, -180)), ((0, -180), (40, -180)), ((40, -180), (40, -160)),
              ((40, -160), (0, -160)), ((0, -160), (0, -180)), ((40, -180), (80, -180)),
              ((80, -180), (80, -160)), ((80, -160), (40, -160)), ((40, -160), (40, -180)),
              ((80, -180), (120, -180)), ((120, -180), (120, -160)), ((120, -160), (80, -160)),
              ((80, -160), (80, -180)), ((120, -180), (160, -180)), ((160, -180), (160, -160)),
              ((160, -160), (120, -160)), ((120, -160), (120, -180)), ((-140, -160), (-100, -160)),
              ((-100, -160), (-100, -140)), ((-100, -140), (-140, -140)), ((-140, -140), (-140, -160)),
              ((-100, -160), (-60, -160)), ((-60, -160), (-60, -140)), ((-60, -140), (-100, -140)),
              ((-100, -140), (-100, -160)), ((-60, -160), (-20, -160)), ((-20, -160), (-20, -140)),
              ((-20, -140), (-60, -140)), ((-60, -140), (-60, -160)), ((-20, -160), (20, -160)),
              ((20, -160), (20, -140)), ((20, -140), (-20, -140)), ((-20, -140), (-20, -160)),
              ((20, -160), (60, -160)), ((60, -160), (60, -140)), ((60, -140), (20, -140)),
              ((20, -140), (20, -160)), ((60, -160), (100, -160)), ((100, -160), (100, -140)),
              ((100, -140), (60, -140)), ((60, -140), (60, -160)), ((100, -160), (140, -160)),
              ((140, -160), (140, -140)), ((140, -140), (100, -140)), ((100, -140), (100, -160)),
              ((140, -160), (180, -160)), ((180, -160), (180, -140)), ((180, -140), (140, -140)),
              ((140, -140), (140, -160)), ((-160, -140), (-120, -140)), ((-120, -140), (-120, -120)),
              ((-120, -120), (-160, -120)), ((-160, -120), (-160, -140)), ((-120, -140), (-80, -140)),
              ((-80, -140), (-80, -120)), ((-80, -120), (-120, -120)), ((-120, -120), (-120, -140)),
              ((-80, -140), (-40, -140)), ((-40, -140), (-40, -120)), ((-40, -120), (-80, -120)),
              ((-80, -120), (-80, -140)), ((-40, -140), (0, -140)), ((0, -140), (0, -120)),
              ((0, -120), (-40, -120)), ((-40, -120), (-40, -140)), ((0, -140), (40, -140)),
              ((40, -140), (40, -120)), ((40, -120), (0, -120)), ((0, -120), (0, -140)),
              ((40, -140), (80, -140)), ((80, -140), (80, -120)), ((80, -120), (40, -120)),
              ((40, -120), (40, -140)), ((80, -140), (120, -140)), ((120, -140), (120, -120)),
              ((120, -120), (80, -120)), ((80, -120), (80, -140)), ((120, -140), (160, -140)),
              ((160, -140), (160, -120)), ((160, -120), (120, -120)), ((120, -120), (120, -140)),
              ((-140, -120), (-100, -120)), ((-100, -120), (-100, -100)), ((-100, -100), (-140, -100)),
              ((-140, -100), (-140, -120)), ((-100, -120), (-60, -120)), ((-60, -120), (-60, -100)),
              ((-60, -100), (-100, -100)), ((-100, -100), (-100, -120)), ((-60, -120), (-20, -120)),
              ((-20, -120), (-20, -100)), ((-20, -100), (-60, -100)), ((-60, -100), (-60, -120)),
              ((-20, -120), (20, -120)), ((20, -120), (20, -100)), ((20, -100), (-20, -100)),
              ((-20, -100), (-20, -120)), ((20, -120), (60, -120)), ((60, -120), (60, -100)),
              ((60, -100), (20, -100)), ((20, -100), (20, -120)), ((60, -120), (100, -120)),
              ((100, -120), (100, -100)), ((100, -100), (60, -100)), ((60, -100), (60, -120)),
              ((100, -120), (140, -120)), ((140, -120), (140, -100)), ((140, -100), (100, -100)),
              ((100, -100), (100, -120)), ((140, -120), (180, -120)), ((180, -120), (180, -100)),
              ((180, -100), (140, -100)), ((140, -100), (140, -120)), ((-160, -100), (-120, -100)),
              ((-120, -100), (-120, -80)), ((-120, -80), (-160, -80)), ((-160, -80), (-160, -100)),
              ((-120, -100), (-80, -100)), ((-80, -100), (-80, -80)), ((-80, -80), (-120, -80)),
              ((-120, -80), (-120, -100)), ((-80, -100), (-40, -100)), ((-40, -100), (-40, -80)),
              ((-40, -80), (-80, -80)), ((-80, -80), (-80, -100)), ((-40, -100), (0, -100)),
              ((0, -100), (0, -80)), ((0, -80), (-40, -80)), ((-40, -80), (-40, -100)),
              ((0, -100), (40, -100)), ((40, -100), (40, -80)), ((40, -80), (0, -80)), ((0, -80), (0, -100)),
              ((40, -100), (80, -100)), ((80, -100), (80, -80)), ((80, -80), (40, -80)), ((40, -80), (40, -100)),
              ((80, -100), (120, -100)), ((120, -100), (120, -80)), ((120, -80), (80, -80)), ((80, -80), (80, -100)),
              ((120, -100), (160, -100)), ((160, -100), (160, -80)), ((160, -80), (120, -80)),
              ((120, -80), (120, -100)), ((-140, -80), (-100, -80)), ((-100, -80), (-100, -60)),
              ((-100, -60), (-140, -60)), ((-140, -60), (-140, -80)), ((-100, -80), (-60, -80)),
              ((-60, -80), (-60, -60)), ((-60, -60), (-100, -60)), ((-100, -60), (-100, -80)),
              ((-60, -80), (-20, -80)), ((-20, -80), (-20, -60)), ((-20, -60), (-60, -60)), ((-60, -60), (-60, -80)),
              ((-20, -80), (20, -80)), ((20, -80), (20, -60)), ((20, -60), (-20, -60)), ((-20, -60), (-20, -80)),
              ((20, -80), (60, -80)), ((60, -80), (60, -60)), ((60, -60), (20, -60)), ((20, -60), (20, -80)),
              ((60, -80), (100, -80)), ((100, -80), (100, -60)), ((100, -60), (60, -60)), ((60, -60), (60, -80)),
              ((100, -80), (140, -80)), ((140, -80), (140, -60)), ((140, -60), (100, -60)), ((100, -60), (100, -80)),
              ((140, -80), (180, -80)), ((180, -80), (180, -60)), ((180, -60), (140, -60)), ((140, -60), (140, -80)),
              ((-160, -60), (-120, -60)), ((-120, -60), (-120, -40)), ((-120, -40), (-160, -40)),
              ((-160, -40), (-160, -60)), ((-120, -60), (-80, -60)), ((-80, -60), (-80, -40)),
              ((-80, -40), (-120, -40)), ((-120, -40), (-120, -60)), ((-80, -60), (-40, -60)),
              ((-40, -60), (-40, -40)), ((-40, -40), (-80, -40)), ((-80, -40), (-80, -60)),
              ((-40, -60), (0, -60)), ((0, -60), (0, -40)), ((0, -40), (-40, -40)), ((-40, -40), (-40, -60)),
              ((0, -60), (40, -60)), ((40, -60), (40, -40)), ((40, -40), (0, -40)), ((0, -40), (0, -60)),
              ((40, -60), (80, -60)), ((80, -60), (80, -40)), ((80, -40), (40, -40)), ((40, -40), (40, -60)),
              ((80, -60), (120, -60)), ((120, -60), (120, -40)), ((120, -40), (80, -40)), ((80, -40), (80, -60)),
              ((120, -60), (160, -60)), ((160, -60), (160, -40)), ((160, -40), (120, -40)), ((120, -40), (120, -60)),
              ((-140, -40), (-100, -40)), ((-100, -40), (-100, -20)), ((-100, -20), (-140, -20)),
              ((-140, -20), (-140, -40)), ((-100, -40), (-60, -40)), ((-60, -40), (-60, -20)),
              ((-60, -20), (-100, -20)), ((-100, -20), (-100, -40)), ((-60, -40), (-20, -40)),
              ((-20, -40), (-20, -20)), ((-20, -20), (-60, -20)), ((-60, -20), (-60, -40)),
              ((-20, -40), (20, -40)), ((20, -40), (20, -20)), ((20, -20), (-20, -20)), ((-20, -20), (-20, -40)),
              ((20, -40), (60, -40)), ((60, -40), (60, -20)), ((60, -20), (20, -20)),
              ((20, -20), (20, -40)), ((60, -40), (100, -40)), ((100, -40), (100, -20)),
              ((100, -20), (60, -20)), ((60, -20), (60, -40)), ((100, -40), (140, -40)),
              ((140, -40), (140, -20)), ((140, -20), (100, -20)), ((100, -20), (100, -40)),
              ((140, -40), (180, -40)), ((180, -40), (180, -20)), ((180, -20), (140, -20)),
              ((140, -20), (140, -40)), ((-160, -20), (-120, -20)), ((-120, -20), (-120, 0)),
              ((-120, 0), (-160, 0)), ((-160, 0), (-160, -20)), ((-120, -20), (-80, -20)),
              ((-80, -20), (-80, 0)), ((-80, 0), (-120, 0)), ((-120, 0), (-120, -20)),
              ((-80, -20), (-40, -20)), ((-40, -20), (-40, 0)), ((-40, 0), (-80, 0)),
              ((-80, 0), (-80, -20)), ((-40, -20), (0, -20)), ((0, -20), (0, 0)), ((0, 0), (-40, 0)),
              ((-40, 0), (-40, -20)), ((0, -20), (40, -20)), ((40, -20), (40, 0)), ((40, 0), (0, 0)),
              ((0, 0), (0, -20)), ((40, -20), (80, -20)), ((80, -20), (80, 0)), ((80, 0), (40, 0)),
              ((40, 0), (40, -20)), ((80, -20), (120, -20)), ((120, -20), (120, 0)), ((120, 0), (80, 0)),
              ((80, 0), (80, -20)), ((120, -20), (160, -20)), ((160, -20), (160, 0)), ((160, 0), (120, 0)),
              ((120, 0), (120, -20)), ((-140, 0), (-100, 0)), ((-100, 0), (-100, 20)), ((-100, 20), (-140, 20)),
              ((-140, 20), (-140, 0)), ((-100, 0), (-60, 0)), ((-60, 0), (-60, 20)), ((-60, 20), (-100, 20)),
              ((-100, 20), (-100, 0)), ((-60, 0), (-20, 0)), ((-20, 0), (-20, 20)), ((-20, 20), (-60, 20)),
              ((-60, 20), (-60, 0)), ((-20, 0), (20, 0)), ((20, 0), (20, 20)), ((20, 20), (-20, 20)),
              ((-20, 20), (-20, 0)), ((20, 0), (60, 0)), ((60, 0), (60, 20)), ((60, 20), (20, 20)),
              ((20, 20), (20, 0)), ((60, 0), (100, 0)), ((100, 0), (100, 20)), ((100, 20), (60, 20)),
              ((60, 20), (60, 0)), ((100, 0), (140, 0)), ((140, 0), (140, 20)), ((140, 20), (100, 20)),
              ((100, 20), (100, 0)), ((140, 0), (180, 0)), ((180, 0), (180, 20)), ((180, 20), (140, 20)),
              ((140, 20), (140, 0)), ((-160, 20), (-120, 20)), ((-120, 20), (-120, 40)), ((-120, 40), (-160, 40)),
              ((-160, 40), (-160, 20)), ((-120, 20), (-80, 20)), ((-80, 20), (-80, 40)), ((-80, 40), (-120, 40)),
              ((-120, 40), (-120, 20)), ((-80, 20), (-40, 20)), ((-40, 20), (-40, 40)), ((-40, 40), (-80, 40)),
              ((-80, 40), (-80, 20)), ((-40, 20), (0, 20)), ((0, 20), (0, 40)), ((0, 40), (-40, 40)),
              ((-40, 40), (-40, 20)), ((0, 20), (40, 20)), ((40, 20), (40, 40)), ((40, 40), (0, 40)),
              ((0, 40), (0, 20)), ((40, 20), (80, 20)), ((80, 20), (80, 40)), ((80, 40), (40, 40)),
              ((40, 40), (40, 20)), ((80, 20), (120, 20)), ((120, 20), (120, 40)), ((120, 40), (80, 40)),
              ((80, 40), (80, 20)), ((120, 20), (160, 20)), ((160, 20), (160, 40)), ((160, 40), (120, 40)),
              ((120, 40), (120, 20)), ((-140, 40), (-100, 40)), ((-100, 40), (-100, 60)), ((-100, 60), (-140, 60)),
              ((-140, 60), (-140, 40)), ((-100, 40), (-60, 40)), ((-60, 40), (-60, 60)), ((-60, 60), (-100, 60)),
              ((-100, 60), (-100, 40)), ((-60, 40), (-20, 40)), ((-20, 40), (-20, 60)), ((-20, 60), (-60, 60)),
              ((-60, 60), (-60, 40)), ((-20, 40), (20, 40)), ((20, 40), (20, 60)), ((20, 60), (-20, 60)),
              ((-20, 60), (-20, 40)), ((20, 40), (60, 40)), ((60, 40), (60, 60)), ((60, 60), (20, 60)),
              ((20, 60), (20, 40)), ((60, 40), (100, 40)), ((100, 40), (100, 60)), ((100, 60), (60, 60)),
              ((60, 60), (60, 40)), ((100, 40), (140, 40)), ((140, 40), (140, 60)), ((140, 60), (100, 60)),
              ((100, 60), (100, 40)), ((140, 40), (180, 40)), ((180, 40), (180, 60)), ((180, 60), (140, 60)),
              ((140, 60), (140, 40)), ((-160, 60), (-120, 60)), ((-120, 60), (-120, 80)), ((-120, 80), (-160, 80)),
              ((-160, 80), (-160, 60)), ((-120, 60), (-80, 60)), ((-80, 60), (-80, 80)), ((-80, 80), (-120, 80)),
              ((-120, 80), (-120, 60)), ((-80, 60), (-40, 60)), ((-40, 60), (-40, 80)), ((-40, 80), (-80, 80)),
              ((-80, 80), (-80, 60)), ((-40, 60), (0, 60)), ((0, 60), (0, 80)), ((0, 80), (-40, 80)),
              ((-40, 80), (-40, 60)), ((0, 60), (40, 60)), ((40, 60), (40, 80)), ((40, 80), (0, 80)),
              ((0, 80), (0, 60)), ((40, 60), (80, 60)), ((80, 60), (80, 80)), ((80, 80), (40, 80)),
              ((40, 80), (40, 60)), ((80, 60), (120, 60)), ((120, 60), (120, 80)), ((120, 80), (80, 80)),
              ((80, 80), (80, 60)), ((120, 60), (160, 60)), ((160, 60), (160, 80)), ((160, 80), (120, 80)),
              ((120, 80), (120, 60)), ((-140, 80), (-100, 80)), ((-100, 80), (-100, 100)), ((-100, 100), (-140, 100)),
              ((-140, 100), (-140, 80)), ((-100, 80), (-60, 80)), ((-60, 80), (-60, 100)), ((-60, 100), (-100, 100)),
              ((-100, 100), (-100, 80)), ((-60, 80), (-20, 80)), ((-20, 80), (-20, 100)), ((-20, 100), (-60, 100)),
              ((-60, 100), (-60, 80)), ((-20, 80), (20, 80)), ((20, 80), (20, 100)), ((20, 100), (-20, 100)),
              ((-20, 100), (-20, 80)), ((20, 80), (60, 80)), ((60, 80), (60, 100)), ((60, 100), (20, 100)),
              ((20, 100), (20, 80)), ((60, 80), (100, 80)), ((100, 80), (100, 100)), ((100, 100), (60, 100)),
              ((60, 100), (60, 80)), ((100, 80), (140, 80)), ((140, 80), (140, 100)), ((140, 100), (100, 100)),
              ((100, 100), (100, 80)), ((140, 80), (180, 80)), ((180, 80), (180, 100)), ((180, 100), (140, 100)),
              ((140, 100), (140, 80)), ((-160, 100), (-120, 100)), ((-120, 100), (-120, 120)),
              ((-120, 120), (-160, 120)), ((-160, 120), (-160, 100)), ((-120, 100), (-80, 100)),
              ((-80, 100), (-80, 120)), ((-80, 120), (-120, 120)), ((-120, 120), (-120, 100)),
              ((-80, 100), (-40, 100)), ((-40, 100), (-40, 120)), ((-40, 120), (-80, 120)),
              ((-80, 120), (-80, 100)), ((-40, 100), (0, 100)), ((0, 100), (0, 120)),
              ((0, 120), (-40, 120)), ((-40, 120), (-40, 100)), ((0, 100), (40, 100)), ((40, 100), (40, 120)),
              ((40, 120), (0, 120)), ((0, 120), (0, 100)), ((40, 100), (80, 100)), ((80, 100), (80, 120)),
              ((80, 120), (40, 120)), ((40, 120), (40, 100)), ((80, 100), (120, 100)), ((120, 100), (120, 120)),
              ((120, 120), (80, 120)), ((80, 120), (80, 100)), ((120, 100), (160, 100)), ((160, 100), (160, 120)),
              ((160, 120), (120, 120)), ((120, 120), (120, 100)), ((-140, 120), (-100, 120)),
              ((-100, 120), (-100, 140)), ((-100, 140), (-140, 140)), ((-140, 140), (-140, 120)),
              ((-100, 120), (-60, 120)), ((-60, 120), (-60, 140)), ((-60, 140), (-100, 140)),
              ((-100, 140), (-100, 120)), ((-60, 120), (-20, 120)), ((-20, 120), (-20, 140)),
              ((-20, 140), (-60, 140)), ((-60, 140), (-60, 120)), ((-20, 120), (20, 120)), ((20, 120), (20, 140)),
              ((20, 140), (-20, 140)), ((-20, 140), (-20, 120)), ((20, 120), (60, 120)), ((60, 120), (60, 140)),
              ((60, 140), (20, 140)), ((20, 140), (20, 120)), ((60, 120), (100, 120)), ((100, 120), (100, 140)),
              ((100, 140), (60, 140)), ((60, 140), (60, 120)), ((100, 120), (140, 120)), ((140, 120), (140, 140)),
              ((140, 140), (100, 140)), ((100, 140), (100, 120)), ((140, 120), (180, 120)), ((180, 120), (180, 140)),
              ((180, 140), (140, 140)), ((140, 140), (140, 120)), ((-160, 140), (-120, 140)),
              ((-120, 140), (-120, 160)), ((-120, 160), (-160, 160)), ((-160, 160), (-160, 140)),
              ((-120, 140), (-80, 140)), ((-80, 140), (-80, 160)), ((-80, 160), (-120, 160)),
              ((-120, 160), (-120, 140)), ((-80, 140), (-40, 140)), ((-40, 140), (-40, 160)),
              ((-40, 160), (-80, 160)), ((-80, 160), (-80, 140)), ((-40, 140), (0, 140)),
              ((0, 140), (0, 160)), ((0, 160), (-40, 160)), ((-40, 160), (-40, 140)), ((0, 140), (40, 140)),
              ((40, 140), (40, 160)), ((40, 160), (0, 160)), ((0, 160), (0, 140)), ((40, 140), (80, 140)),
              ((80, 140), (80, 160)), ((80, 160), (40, 160)), ((40, 160), (40, 140)), ((80, 140), (120, 140)),
              ((120, 140), (120, 160)), ((120, 160), (80, 160)), ((80, 160), (80, 140)), ((120, 140), (160, 140)),
              ((160, 140), (160, 160)), ((160, 160), (120, 160)), ((120, 160), (120, 140)), ((-140, 160), (-100, 160)),
              ((-100, 160), (-100, 180)), ((-100, 180), (-140, 180)), ((-140, 180), (-140, 160)),
              ((-100, 160), (-60, 160)), ((-60, 160), (-60, 180)), ((-60, 180), (-100, 180)),
              ((-100, 180), (-100, 160)), ((-60, 160), (-20, 160)), ((-20, 160), (-20, 180)),
              ((-20, 180), (-60, 180)), ((-60, 180), (-60, 160)), ((-20, 160), (20, 160)), ((20, 160), (20, 180)),
              ((20, 180), (-20, 180)), ((-20, 180), (-20, 160)), ((20, 160), (60, 160)), ((60, 160), (60, 180)),
              ((60, 180), (20, 180)), ((20, 180), (20, 160)), ((60, 160), (100, 160)), ((100, 160), (100, 180)),
              ((100, 180), (60, 180)), ((60, 180), (60, 160)), ((100, 160), (140, 160)), ((140, 160), (140, 180)),
              ((140, 180), (100, 180)), ((100, 180), (100, 160)), ((140, 160), (180, 160)), ((180, 160), (180, 180)),
              ((180, 180), (140, 180)), ((140, 180), (140, 160)))

    target_dict = {}
    for target in t_list:
        if target not in target_dict.keys():
            target_dict[target] = 1
    print(target_dict)
    sprite = brickLayer(-160, -180, 90, draw_targets=target_dict)
    success = False
    for key in p_scripts:
        script = p_scripts[key]
        if script[0] == ['event_whenkeypressed', '4']:
            print("aaa here we go")
            success = do_sprite(sprite, script, True)
            if success:
                break
    print("ggg sprite.x {} sprite.y {} dir {} targets {}".format(sprite.x, sprite.y, sprite.direction,
                                                                 sprite.draw_targets))
    find_repeat_1 = match_string(r"\['event_whenkeypressed', \s* '4'], .+ \['control_repeat', \s '2'", p_scripts)
    find_repeat_2 = match_string(r"\['event_whenkeypressed', \s* '4'], .+ \['control_repeat', \s '8'", p_scripts)
    if find_repeat_1['pass'] is False or find_repeat_2['pass'] is False:
        p_test['fail_message'] += "Did not find two repeat with the correct number of times in the script. <br>"
    if success is False:
        p_test['fail_message'] += 'Drew too many lines.<br>'
    if 1 in sprite.draw_targets.values():
        p_test['fail_message'] += 'Did not draw enough lines.<br>'
    if success is False or 1 in sprite.draw_targets.values():
        p_test['fail_message'] += 'Key: Start location, end location, whether or not this line was ' \
                                  'not drawn (1 = not drawn, 0 = drawn).<br>' \
                                  'Line status:<br>'
        counter = 0
        for key in target_dict:
            p_test['fail_message'] += str(key) + ": " + str(target_dict[key]) + "<br>"
            counter += 1
            if counter % 8 == 0:
                p_test['fail_message'] += 'New row <br>'
    if success and find_repeat_1['pass'] and find_repeat_2['pass'] and 1 not in sprite.draw_targets.values():
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test