# Inputs: p_filename, filename to search for help.
#         p_points, number of points this is worth.
# Output: dictionary of test_help


def helps(p_filename, p_points):
    import delegator

    # Check for help comment
    cmd = 'grep "#" ' + p_filename + ' | grep help | wc -l  '
    c = delegator.run(cmd)
    help_comments = int(c.out)
    p_test_help = {"name": "Testing that you got a help and documented it as a comment (" + str(p_points) + " points)",
                   "pass": True,
                   "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                                   "Be sure your comment is meaningful, otherwise this can be overturned "
                                   "on review.",
                   "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                                   " how somebody helped you with your code.  <br>"
                                   "This must be a MEANINGFUL help.<br>"
                                   "For example 'Luis helped by testing that input abc gave output def as expected'"
                                   "will score.  <br>"
                                   "Helps such as 'Joe helped test my code' will probably be overturned on review.<br>"
                                   "This translates to " + str(p_points) + " points deduction.<br>",
                   }
    if help_comments == 0:
        p_test_help['pass'] = False
    return p_test_help
