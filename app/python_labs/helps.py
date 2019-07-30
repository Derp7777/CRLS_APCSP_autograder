def helps(p_filename, p_points):
    """
    Function figures out how many points to give for helps.
    :param p_filename: name of python file with code to grade
    :param p_points: points to give if there is a help
    :return: a dictionary containing the test info
    """
    import delegator

    # Check for help comment
    cmd = 'grep "#" ' + p_filename + ' | grep -i help | grep -vi wu|grep -vi martinez |grep -vi atwood|  wc -l  '
    c = delegator.run(cmd)
    help_comments = int(c.out)
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
                                   "This translates to " + str(p_points) + " points deduction.<br>"
                                   "Your help can NOT be from teachers Atwood, Wu, or Martinez",
                   'points': 0
                   }
    if help_comments == 0:
        p_test_help['pass'] = False
    else:
        p_test_help['points'] += p_points
    return p_test_help
