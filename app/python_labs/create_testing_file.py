# Inputs: p_filename, filename with python in it
# This module creates a testing file to run unit tests


def create_testing_file(p_filename):
    import delegator
    import sys
    import os
    import re

    from app.python_labs import YEAR

    var_dir = ''
    if sys.platform == 'darwin':
        var_dir = '/Users/dimmyfinster/PycharmProjects/CRLS_APCSP_autograder/var'
        # This is Eric's home computer
    else:
        var_dir = '/home/ewu/CRLS_APCSP_autograder/var'
    if os.path.isdir(var_dir) is False:
        raise Exception("Cannot find the var dir")

    p_functions_filename = p_filename.replace('.py', '.functions.py')

    p_var_filename = re.sub('/tmp/', '', p_filename)
    p_var_filename = re.sub(YEAR + '_', '', p_var_filename)
    p_var_filename = re.sub('.py', '.test.py', p_var_filename)
    p_var_filename = re.sub('.+_', '', p_var_filename)
    cmd = ' cat ' + var_dir + "/" +  p_functions_filename + " " + p_var_filename + "  > /tmp/" + p_var_filename
    c = delegator.run(cmd)
    if c.err:
        flash("There was a problem creating the python test file")
