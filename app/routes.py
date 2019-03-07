from flask import render_template, url_for, request, redirect, flash

from app import app
from app.forms import UploadForm
from werkzeug.utils import secure_filename
import os


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Please select a file')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        if not allowed_file(file.filename):
            flash('This type of file not allowed.  Only files ending in .py.'
                  '  In particular, Google doc and text files are not allowed.'
                  'You have to turn in a Python file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash(file.filename + ' uploaded')
            if request.form['lab'] == '1.040':
                return redirect(url_for('feedback_1040', filename=filename))
            elif request.form['lab'] == '1.060':
                return redirect(url_for('feedback_1060', filename=filename))
            elif request.form['lab'] == '2.020':
                return redirect(url_for('feedback_2020', filename=filename))
            elif request.form['lab'] == '2.032a':
                return redirect(url_for('feedback_2032a', filename=filename))
            elif request.form['lab'] == '2.032b':
                return redirect(url_for('feedback_2032b', filename=filename))
            elif request.form['lab'] == '2.040':
                return redirect(url_for('feedback_2040', filename=filename))
            elif request.form['lab'] == '2.050a':
                return redirect(url_for('feedback_2050a', filename=filename))
            elif request.form['lab'] == '2.050b':
                return redirect(url_for('feedback_2050b', filename=filename))
            elif request.form['lab'] == '3.011':
                return redirect(url_for('feedback_3011', filename=filename))
            elif request.form['lab'] == '3.020':
                return redirect(url_for('feedback_3020', filename=filename))
            elif request.form['lab'] == '3.026':
                return redirect(url_for('feedback_3026', filename=filename))
            elif request.form['lab'] == '4.011':
                return redirect(url_for('feedback_4011', filename=filename))
            elif request.form['lab'] == '4.021':
                return redirect(url_for('feedback_4021', filename=filename))
            elif request.form['lab'] == '4.022':
                return redirect(url_for('feedback_4022', filename=filename))
            elif request.form['lab'] == '4.025':
                return redirect(url_for('feedback_4025', filename=filename))
            elif request.form['lab'] == '6.011':
                return redirect(url_for('feedback_6011', filename=filename))
            elif request.form['lab'] == '6.021':
                return redirect(url_for('feedback_6021', filename=filename))
            elif request.form['lab'] == '6.031':
                return redirect(url_for('feedback_6031', filename=filename))

            
            
            
    form = UploadForm()
    user = {'username': 'CRLS Scholar!!!'}
    return render_template('index.html', title='Home', user=user, form=form)


@app.route('/feedback_1040')
def feedback_1040():
    import re
    import subprocess
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 34.5, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2019', filename)
    find_lab = re.search('1.040', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2019_luismartinez_1.04.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2019_luismartinez_1.040.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)

        # Check for part 1 asks 3 questions
        cmd = 'grep "input" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        inputs = int(c.out)
        test_inputs_1 = {"name": "Testing for at genie asking at least 3 questions (first part of lab) ( 5 points )",
                         "pass": True,
                         "pass_message": "Pass!  Genie asks at least 3 questions (first part of lab)",
                         "fail_message": "Fail.  Code does not have at least 3 inputs (first part of lab).<br>"
                                         "The Genie needs to ask for 3 wishes for the first part"
                                         "Please fix error and resubmit (other tests not run). <br>",
                         }
        if inputs < 3:
            test_inputs_1['pass'] = False
            tests.append(test_inputs_1)
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            score_info['score'] += 5
            tests.append(test_inputs_1)

            # Check that things are in correct order (a, b, c)
            filename_output = filename + '.out'
            cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/1.040.in > ' \
                  + filename_output
            c = delegator.run(cmd)
            if c.err:
                flash('bad! You have an error somewhere in running program correct order 1.040')
                flash(c.err)
            with open(filename_output, 'r') as myfile:
                outfile_data = myfile.read()

            search_object = re.search(r".+ "
                                      r"a1 "
                                      r".+ "
                                      r"a2 "
                                      r".+ "
                                      r"a3 "
                                      r".+ ",
                                      outfile_data, re.X | re.M | re.S)
            test_order_1 = {"name": "Testing that Genie answers in correct order for part 1 (5 points)",
                            "pass": True,
                            "pass_message": "Pass!  Genie appears to answer your wishes in correct order",
                            "fail_message": "Fail.  Double check that the Genie is answering in correct order. <br>"
                                            "Genie needs to reply back with the 3 wishes you asked for in a particular order. <br>"
                                            "Note: you must have a comma, period, space, or something between wishes."
                                            "Review the sample run if this isn't clear. <br>"
                            }
            if not search_object or c.err:
                test_order_1['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_order_1)

            # Check for part 2 asks 3 more questions, 6 total
            cmd = 'grep "input" ' + filename + ' | wc -l  '
            c = delegator.run(cmd)
            inputs = int(c.out)
            test_inputs_2 = {"name": "Testing for at genie asking at least 6 questions (first + second part of lab) "
                                     "(5 points)",
                             "pass": True,
                             "pass_message": "Pass!  Genie asks at least 6 questions (first + second part of lab)",
                             "fail_message": "Fail. Code does not have at least 6 inputs (first + second part of lab)."
                                             "<br>"
                                             "The Genie needs to ask for 3 wishes for the first part and 3 for the second part",
                             }
            if inputs < 6:
                test_inputs_2['pass'] = False
                tests.append(test_inputs_2)
            else:
                score_info['score'] += 5
                tests.append(test_inputs_2)

            # Check for asing variable questions
            process_grep1 = subprocess.Popen(['/bin/grep', "input([\"']", filename], stdout=subprocess.PIPE)
            process_wc = subprocess.Popen(['wc', '-l'], stdin=process_grep1.stdout, stdout=subprocess.PIPE)
            process_grep1.wait()
            process_grep1.stdout.close()
            output_string = str(process_wc.communicate()[0])
            match_object = re.search(r"([0-9]+)", output_string)
            inputs_variable = int(match_object.group())
            test_input_variable = {"name": "Testing for use of variable to sub for repeated strings in asking questions"
                                           "(5 points)",
                                   "pass": True,
                                   "pass_message": "Pass!  Genie appears to have stuck repeated strings into variables,"
                                                   " per instructions AND there are at least 6 inputs",
                                   "fail_message": "Fail.  There are over 3 inputs with single or double quotations. "
                                                   "<br>"
                                                   "Please recheck the instructions about putting repeated strings into variables. "
                                                   "This translates to -10 points deduction.<br>",
                                   }
            if inputs_variable > 4:
                test_input_variable['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_input_variable)

            # Check that things are in correct order (a, b, c, then b, c, a)

            cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/1.040.in > ' \
                  + filename_output
            c = delegator.run(cmd)

            search_object = re.search(r".+ "
                                      r"a1 "
                                      r".+ "
                                      r"a2 "
                                      r".+ "
                                      r"a3 "
                                      r".+ "
                                      r"b2 "
                                      r".+ "
                                      r"b3 "
                                      r".+ "
                                      r"b1",
                                      outfile_data, re.X | re.M | re.S)
            test_order_2 = {"name": "Testing that Genie answers in correct order for part 1 and part 2 (5 points)",
                            "pass": True,
                            "pass_message": "Pass!  Genie appears to answer your wishes in correct order for part 1 "
                                            "and part 2",
                            "fail_message": "Fail.  Double check that the Genie is answering in correct order for both "
                                            "part 1 and part 2. <br>"
                                            "wish1, wish2, and wish3 responses need to go in a particular order. <br>"
                                            "Note: you must have a comma, period, space, or something between wishes."
                                            "Review the instructions if this isn't clear. <br>"
                            }
            if not search_object or c.err:
                test_order_2['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_order_2)

            # Find number of PEP8 errors
            #cmd2 = '/home/ewu/CRLS_APCSP_autograder/venv1/bin/pycodestyle --max-line-length=120 ' + filename + ' | wc -l  '
            #c = delegator.run(cmd2)
            #flash(c.out)
            
            cmd = '/home/ewu/CRLS_APCSP_autograder/venv1/bin/pycodestyle --max-line-length=120 ' + filename + ' | wc -l  '
            c = delegator.run(cmd)
            if c.err:
                flash(c.err)
            side_errors = int(c.out)
            test_pep8 = {"name": "Testing for PEP8 warnings and errors (7 points)",
                         "pass": True,
                         "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                         "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                                                                          "This translates to -" + str(
                             side_errors) + " point(s) deduction.<br>"
                         }
            if side_errors != 0:
                test_pep8['pass'] = False
            score_info['score'] += max(0, int(7) - side_errors)
            tests.append(test_pep8)

            # Check for help comment
            cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
            c = delegator.run(cmd)
            help_comments = int(c.out)
            test_help = {"name": "Testing that you got a help and documented it as a comment (2.5 points)",
                         "pass": True,
                         "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                                         "Be sure your comment is meaningful, otherwise this can be overturned on review.",
                         "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                                         " how somebody helped you with your code.  <br>"
                                         "If you didn't have any problems, then ask somebody to check that your code"
                                         " gives correct outputs, given an input.<br>"
                                         "This translates to -5 points deduction.<br>",
                         }
            if help_comments == 0:
                test_help['pass'] = False
            else:
                score_info['score'] += 2.5
            tests.append(test_help)

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_1060')
def feedback_1060():
    import re
    import subprocess
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 59, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2019', filename)
    find_lab = re.search('1.060', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2019_luismartinez_1.06.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2019_luismartinez_1.060.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)

        # Check that asks at least 5 questions
        cmd = 'grep "input" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        inputs = int(c.out)
        test_inputs_1 = {"name": "Testing for at least 5 input questions (5 points)",
                         "pass": True,
                         "pass_message": "Pass!  Asks at least 5 inputs questions",
                         "fail_message": "Fail.  Code does not have at least 5 input questions.<br>"
                                         "The program needs to ask for 5 inputs of parts of speech"
                                         "Please fix error and resubmit (other tests not run). <br>",
                         }
        if inputs < 5:
            test_inputs_1['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_inputs_1)

        # Check that inputs are named after part of speech
        cmd = 'grep -E "verb|noun|adjective|adverb|preposition" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        parts_of_speech = int(c.out)
        test_parts_of_speech = {"name": "Testing that variables named after parts of speech (5 points)",
                                "pass": True,
                                "pass_message": "Pass!  Code asks at least 5 parts of speech in code",
                                "fail_message": "Fail.  Variables should be named after parts of speech. "
                                                "(noun, verb1, adjective, noun3, adverb10, etc...)<br>"
                                                "The program needs to ask for 5 inputs of parts of speech.<br>"
                                                "Please fix error and resubmit (other tests not run). <br>",
                                }

        if parts_of_speech < 5:
            test_parts_of_speech['pass'] = False
            tests.append(test_parts_of_speech)
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            score_info['score'] += 5
            tests.append(test_parts_of_speech)

            # Check for at least 1 print statement
            cmd = 'grep "print" ' + filename + ' | wc -l  '
            c = delegator.run(cmd)
            prints = int(c.out)
            test_one_print = {"name": "Testing for at least 1 print statement (5 points)",
                              "pass": True,
                              "pass_message": "Pass!  Asks at least 1 print statement.",
                              "fail_message": "Fail.  Code does not have at least 1 print statement.<br>"
                                              "The program needs to have print statements"
                              }
            if prints < 1:
                test_one_print['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_one_print)

            # Check for less than 3 print statement
            test_three_print = {"name": "Testing for  less than 3 print statements (5 points)",
                                "pass": True,
                                "pass_message": "Pass!  Fewer than 3 print statements.",
                                "fail_message": "Fail.  Code has more than 3 print statements.<br>"
                                                "The program should have max 3 prints"
                                }
            if prints > 3:
                test_three_print['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_three_print)

            # Check that things are in correct order.  First 5 inputs show up in output)
            filename_output = filename + '.out'
            cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/1.060.in > ' \
                  + filename_output
            c = delegator.run(cmd)
            if c.err:
                flash('bad! You have an error somewhere in running program first 5 inputs show up')
            with open(filename_output, 'r') as myfile:
                outfile_data = myfile.read()

            search_object_1 = re.search(r"a1", outfile_data, re.X | re.M | re.S)
            search_object_2 = re.search(r"a2", outfile_data, re.X | re.M | re.S)
            search_object_3 = re.search(r"a3", outfile_data, re.X | re.M | re.S)
            search_object_4 = re.search(r"b1", outfile_data, re.X | re.M | re.S)
            search_object_5 = re.search(r"b2", outfile_data, re.X | re.M | re.S)

            test_show_5 = {"name": "Testing that first 5 inputs show up in the output printout (5 points)",
                           "pass": True,
                           "pass_message": "Pass!  First 5 inputs show up in the output printout",
                           "fail_message": "Fail.  Check that first 5 inputs show up in the output printout.<br>"
                                           "For example, if you typed in noun1, verb1, noun2, verb2, and adjective<br>"
                                           "noun1, verb1, noun2, verb2, and adjective should all appear in the prinout."
                                           "<br> ",
                           }
            if search_object_1 and search_object_2 and search_object_3 and search_object_4 and search_object_5:
                score_info['score'] += 15
            else:
                test_show_5['pass'] = False
            tests.append(test_show_5)

            # Check for 3 punctuations
            filename_output = filename + '.out'
            cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/1.060.in > ' \
                  + filename_output
            c = delegator.run(cmd)
            if c.err:
                flash('bad! You have an error somewhere in running program check 3 punctuations')
            with open(filename_output, 'r') as myfile:
                outfile_data = myfile.read()

            num_periods = outfile_data.count('.')
            num_questions = outfile_data.count('?')
            num_exclamations = outfile_data.count('!')
            num_punctuations = num_periods + num_questions + num_exclamations
            test_puncts = {"name": "Testing that there are at least 3 punctuations (5 points)",
                           "pass": True,
                           "pass_message": "Pass!  There are at least 3 punctuations.",
                           "fail_message": "Fail.  Check that there are at least 3 punctuations.<br>"
                                           "Looking for at least 3 periods, questions marks, or exclamations "
                                           "<br> ",
                           }
            if num_punctuations < 3:
                test_puncts['pass'] = False
            else:
                score_info['score'] += 5

            tests.append(test_puncts)

            # Find number of PEP8 errors
            #cmd2 = '/home/ewu/CRLS_APCSP_autograder/venv1/bin/pycodestyle --max-line-length=120 ' + filename
            #c = delegator.run(cmd2)
            #flash(c.out)
            

            
            cmd = '/home/ewu/CRLS_APCSP_autograder/venv1/bin/pycodestyle --max-line-length=120 ' + filename + ' | wc -l  '
            c = delegator.run(cmd)
            #flash(c.out)
            
            side_errors = int(c.out)
            test_pep8 = {"name": "Testing for PEP8 warnings and errors (14 points)",
                         "pass": True,
                         "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                         "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                                                                          "This translates to -" + str(
                             side_errors) + " point(s) deduction.<br>"
                         }
            if c.err:
                flash(c.err)
            if side_errors != 0:
                test_pep8['pass'] = False
            score_info['score'] += max(0, int(14) - side_errors)
            tests.append(test_pep8)

            # Check for help comment
            cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
            c = delegator.run(cmd)
            help_comments = int(c.out)
            test_help = {"name": "Testing that you got a help and documented it as a comment (5 points)",
                         "pass": True,
                         "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                                         "Be sure your comment is meaningful, otherwise this can be "
                                         "overturned on review.",
                         "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                                         " how somebody helped you with your code.  <br>"
                                         "If you didn't have any problems, then ask somebody to check that your code"
                                         " gives correct outputs, given an input.<br>"
                                         "This translates to -5 points deduction.<br>",
                         }
            if help_comments == 0:
                test_help['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_help)

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_2020')
def feedback_2020():
    import re
    import subprocess
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 55, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2019', filename)
    find_lab = re.search('2.020', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2019_luismartinez_1.06.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2019_luismartinez_2.020.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)

        # Check that input1 is good (input / 2)
        filename_output = filename + '.out'
        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.020-1.in > ' + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check input1')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()
        flash(outfile_data)
        search_object = re.search(r"49.5", outfile_data, re.X | re.M | re.S)
        test_output_1 = {"name": "Testing that the number divides by 2 correctly and prints it out (15 points)",
                         "pass": True,
                         "pass_message": "Pass!  The number divides by 2 correctly and prints it out.",
                         "fail_message": "Fail.  Check that the number divides by 2 correctly and prints it out.<br>"
                                         "For example, if you input 5, it should output 2.5.<br>."
                                         "Note, the program looks at the FIRST thing that is printed.  If you think your<br>"
                                         "program should pass, remove any extra prints in the program.<br>"
                                         "<br> ",
                         }
        if search_object:
            score_info['score'] += 15
        else:
            test_output_1['pass'] = False
        tests.append(test_output_1)

        # Check input2 is good (int(input / 2))
        search_object = re.search(r"49$", outfile_data, re.X | re.M | re.S)
        test_output_2 = {"name": "Testing that the number divides by 2 correctly and prints it out INTEGER (15 points)",
                         "pass": True,
                         "pass_message": "Pass!  The number divides by 2 correctly and prints it out.",
                         "fail_message": "Fail.  Check that the number divides by 2 correctly and prints it "
                                         "out INTEGER.<br>"
                                         "For example, if you input 5, it should output 2 <br>"
                                         "<br> "
                                         "Note, the program looks at the SECOND thing that is printed.  If you think your<br>"
                                         "program should pass, remove any extra prints in the program.<br>"
,
                         
                         }
        if not search_object:
            test_output_2['pass'] = False
            tests.append(test_output_2)
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            tests.append(test_output_2)
            score_info['score'] += 15

        # check input3 is good (input / 2) AND (int(input/2)) for 3.5 number
        filename_output = filename + '2.out'
        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.020-2.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check input2')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object1 = re.search(r"49.75", outfile_data, re.X | re.M | re.S)
        search_object2 = re.search(r"49", outfile_data, re.X | re.M | re.S)

        test_output_3 = {"name": "Testing that it works for float numbers (6 points)",
                         "pass": True,
                         "pass_message": "Pass!  It works for float numbers",
                         "fail_message": "Fail.  Check that it works for float numbers.<br>"
                                         "For example, if you typed in 3.5, it should output 1.75 and 1"
                                         "<br> ",
                         }
        if search_object1:
            flash("yes")
        if search_object2:
            flash("yes2")
        if search_object1 and search_object2:
            score_info['score'] += 6
        else:
            test_output_3['pass'] = False
        tests.append(test_output_3)

        # Find number of PEP8 errors
        cmd = '/home/ewu/CRLS_APCSP_autograder/venv1/bin/pycodestyle --max-line-length=120  --ignore=E305,E226 ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        side_errors = int(c.out)
        test_pep8 = {"name": "Testing for PEP8 warnings and errors (14 points)",
                     "pass": True,
                     "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                     "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                                                                      "This translates to -" +
                                     str(side_errors) + " point(s) deduction.<br>"
                     }
        if side_errors != 0:
            test_pep8['pass'] = False
        score_info['score'] += max(0, int(14) - side_errors)
        tests.append(test_pep8)

        # Check for help comment
        cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
        c = delegator.run(cmd)
        help_comments = int(c.out)
        test_help = {"name": "Testing that you got a help and documented it as a comment (5 points)",
                     "pass": True,
                     "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                                     "Be sure your comment is meaningful, otherwise this can be "
                                     "overturned on review.",
                     "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                                     " how somebody helped you with your code.  <br>"
                                     "If you didn't have any problems, then ask somebody to check that your code"
                                     " gives correct outputs, given an input.<br>"
                                     "This translates to -5 points deduction.<br>",
                     }
        if help_comments == 0:
            test_help['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_help)

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_2032a')
def feedback_2032a():
    import re
    import subprocess
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 22.5, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2019', filename)
    find_lab = re.search('2.032a', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2019_luismartinez_2.032a.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2019_luismartinez_2.032a.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)

        # Check for ifs
        cmd = 'grep "if" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        ifs = int(c.out)

        test_ifs = {"name": "Checking for zero if statements (5 points)",
                    "pass": True,
                    "pass_message": "Pass!  Zero if statements",
                    "fail_message": "Fail.  Code should not have any if statements.<br>"
                                    "For example, print(1==1) NOT if (1 == 1): print('True') <br>"
                                    "Review instructions or ask teacher for more details<br> ",
                    }
        if ifs == 0:
            score_info['score'] += 5
        else:
            test_ifs['pass'] = False
        tests.append(test_ifs)

        # test all 8 cases
        filename_output = filename + '.out'
        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032a-1.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-1')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()
        eight_cases_score = 0

        search_object = re.search(r"False", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032a-2.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-2')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"False", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032a-3.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-3')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"True", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032a-4.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-4')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"False", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032a-5.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-5')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"False", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032a-6.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-6')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"False", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032a-7.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-7')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"False", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032a-8.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-8')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"False", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        test_eight_tests = {"name": "Testing that all 8 test cases work (8 points)",
                            "pass": True,
                            "pass_message": "Pass!  All 8 test cases work",
                            "fail_message": "Fail.  Check your 8 test cases.<br>"
                                            "Please review the table that is after the 2.032a program run "
                                            "in your assignment <br> "
                                            "As part of this assignment, you should have populated that table.<br>"
                                            "You should test your code with the data from this table.<br>"
                                            "You need to figure out which ones, we do not tell you",
                            }

        if eight_cases_score != 8:
            test_eight_tests['pass'] = False
        if c.err:
            test_eight_tests['pass'] = False
            eight_cases_score = 0 
        score_info['score'] += eight_cases_score
        tests.append(test_eight_tests)

        # Find number of PEP8 errors
        cmd = '/home/ewu/CRLS_APCSP_autograder/venv1/bin/pycodestyle --max-line-length=120 ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        side_errors = int(c.out)
        test_pep8 = {"name": "Testing for PEP8 warnings and errors (7 points)",
                     "pass": True,
                     "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                     "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                                                                      "This translates to -" + str(
                         side_errors) + " point(s) deduction.<br>"
                     }
        if side_errors != 0:
            test_pep8['pass'] = False
        score_info['score'] += max(0, int(7) - side_errors)
        tests.append(test_pep8)

        # Check for help comment
        cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
        c = delegator.run(cmd)
        help_comments = int(c.out)
        test_help = {"name": "Testing that you got a help and documented it as a comment (2.5 points)",
                     "pass": True,
                     "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                                     "Be sure your comment is meaningful, otherwise this can be "
                                     "overturned on review.",
                     "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                                     " how somebody helped you with your code.  <br>"
                                     "If you didn't have any problems, then ask somebody to check that your code"
                                     " gives correct outputs, given an input.<br>"
                                     "This translates to -5 points deduction.<br>",
                     }
        if help_comments == 0:
            test_help['pass'] = False
        else:
            score_info['score'] += 2.5
        tests.append(test_help)

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_2032b')
def feedback_2032b():
    import re
    import subprocess
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 22.5, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2019', filename)
    find_lab = re.search('2.032b', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2019_luismartinez_2.032b.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2019_luismartinez_2.032b.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)

        # Check for ifs
        cmd = 'grep "if" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        ifs = int(c.out)

        test_ifs = {"name": "Checking for zero if statements (5 points)",
                    "pass": True,
                    "pass_message": "Pass!  Zero if statements",
                    "fail_message": "Fail.  Code should not have any if statements.<br>"
                                    "For example, print(1==1) NOT if (1 == 1): print('True') <br>"
                                    "Review instructions or ask teacher for more details<br> ",
                    }
        if ifs == 0:
            score_info['score'] += 5
        else:
            test_ifs['pass'] = False
        tests.append(test_ifs)

        # test all 8 cases
        filename_output = filename + '.out'
        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032b-1.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-1')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()
        eight_cases_score = 0

        search_object = re.search(r"True", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032b-2.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-2')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"False", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032b-3.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-3')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"True", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032b-4.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-4')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"False", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032b-5.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-5')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"True", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032b-6.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-6')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"False", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032b-7.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-7')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"False", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032b-8.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-8')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"False", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        test_eight_tests = {"name": "Testing that all 8 test cases work (8 points)",
                            "pass": True,
                            "pass_message": "Pass!  All 8 test cases work",
                            "fail_message": "Fail.  Check your 8 test cases.<br>"
                                            "Please review the table that is after the 2.032b program run "
                                            "in your assignment <br> "
                                            "As part of this assignment, you should have populated that table.<br>"
                                            "You should test your code with the data from this table.<br>"
                                            "You need to figure out which ones, we do not tell you",
                            }

        if eight_cases_score != 8:
            test_eight_tests['pass'] = False
        if c.err:
            test_eight_tests['pass'] = False
            eight_cases_score = 0 

        score_info['score'] += eight_cases_score
        tests.append(test_eight_tests)

        # Find number of PEP8 errors
        cmd = '/home/ewu/CRLS_APCSP_autograder/venv1/bin/pycodestyle --max-line-length=120 ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        side_errors = int(c.out)
        test_pep8 = {"name": "Testing for PEP8 warnings and errors (7 points)",
                     "pass": True,
                     "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                     "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                                                                      "This translates to -" + str(
                         side_errors) + " point(s) deduction.<br>"
                     }
        if side_errors != 0:
            test_pep8['pass'] = False
        score_info['score'] += max(0, int(7) - side_errors)
        tests.append(test_pep8)

        # Check for help comment
        cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
        c = delegator.run(cmd)
        help_comments = int(c.out)
        test_help = {"name": "Testing that you got a help and documented it as a comment (2.5 points)",
                     "pass": True,
                     "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                                     "Be sure your comment is meaningful, otherwise this can be "
                                     "overturned on review.",
                     "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                                     " how somebody helped you with your code.  <br>"
                                     "If you didn't have any problems, then ask somebody to check that your code"
                                     " gives correct outputs, given an input.<br>"
                                     "This translates to -5 points deduction.<br>",
                     }
        if help_comments == 0:
            test_help['pass'] = False
        else:
            score_info['score'] += 2.5
        tests.append(test_help)

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_2040')
def feedback_2040():
    import re
    import subprocess
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 46, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2019', filename)
    find_lab = re.search('2.040', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2019_luismartinez_2.040.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2019_luismartinez_2.040.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)

        # Check for equals, aka variable assignment
        cmd = 'grep "=" ' + filename + ' | grep -v "==" | wc -l  '
        c = delegator.run(cmd)
        equals = int(c.out)

        test_variables = {"name": "Checking for variables, need > 4 (5 points)",
                          "pass": True,
                          "pass_message": "Pass!  At least 4 equals signs assigning variables",
                          "fail_message": "Fail.  Code should assign at least 4 prizes.<br>"
                                          "For example, prize1 = 'brand new car' prize2 =..etc.. <br>"
                                          "Review instructions or ask teacher for more details<br> ",
                          }
        if equals > 4:
            score_info['score'] += 5
        else:
            test_variables['pass'] = False
        tests.append(test_variables)

        # test input
        cmd = 'grep "input" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        inputs = int(c.out)

        test_inputs = {"name": "Checking for asking use question (5 points)",
                       "pass": True,
                       "pass_message": "Pass!  At least 4 equals signs assigning variables",
                       "fail_message": "Fail. Code should ask user for a door to choose.<br>"
                       }
        if inputs >= 1:
            score_info['score'] += 5
        else:
            test_inputs['pass'] = False
        tests.append(test_inputs)

        # test if
        cmd = 'grep "if" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        ifs = int(c.out)

        test_ifs = {"name": "Checking for at least one if(5 points)",
                    "pass": True,
                    "pass_message": "Pass!  At least 1 if in code",
                    "fail_message": "Fail. Code should use an if to help decide what to print <br>"
                                    " depending on what door was chosen"
                    }
        if ifs >= 1:
            score_info['score'] += 5
        else:
            test_ifs['pass'] = False
        tests.append(test_ifs)

        # test else
        cmd = 'grep "^else" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        elses = int(c.out)

        test_elses = {"name": "Checking for at least one else at beginning of line(5 points)",
                      "pass": True,
                      "pass_message": "Pass!  At least one else in code at beginning of line",
                      "fail_message": "Fail. Code should use an else in case user doesn't pick door 1-4"
                      }
        if elses >= 1:
            score_info['score'] += 6
        else:
            test_elses['pass'] = False
        tests.append(test_elses)

        # test elif
        cmd = 'grep "elif" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        elifs = int(c.out)

        test_elifs = {"name": "Checking for at least 3 elifs (6 points)",
                      "pass": True,
                      "pass_message": "Pass!  At least 3 elifs in code",
                      "fail_message": "Fail. Review the presentation for why we use elif vs if.  This question will be "
                                      "on <br> your lab understanding Google form for sure."
                      }
        if elifs >= 3:
            score_info['score'] += 6
        else:
            test_elifs['pass'] = False
        tests.append(test_elifs)



        # Find number of PEP8 errors
        cmd = '/home/ewu/CRLS_APCSP_autograder/venv1/bin/pycodestyle --max-line-length=120 ' + filename + ' | wc -l '
        c = delegator.run(cmd)
        side_errors = int(c.out)
        test_pep8 = {"name": "Testing for PEP8 warnings and errors (14 points)",
                     "pass": True,
                     "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                     "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                     "This translates to -" + str(
                         side_errors) + " point(s) deduction.<br>"
        }
        if side_errors != 0:
            test_pep8['pass'] = False
        score_info['score'] += max(0, int(14) - side_errors)
        tests.append(test_pep8)
            

        # Check for help comment
        cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
        c = delegator.run(cmd)
        help_comments = int(c.out)
        test_help = {"name": "Testing that you got a help and documented it as a comment (5 points)",
                     "pass": True,
                     "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                                     "Be sure your comment is meaningful, otherwise this can be "
                                     "overturned on review.",
                     "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                                     " how somebody helped you with your code.  <br>"
                                     "If you didn't have any problems, then ask somebody to check that your code"
                                     " gives correct outputs, given an input.<br>"
                                     "This translates to -5 points deduction.<br>",
                     }
        if help_comments == 0:
            test_help['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_help)

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)



@app.route('/feedback_2050a')
def feedback_2050a():
    import re
    import subprocess
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 15.5, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2019', filename)
    find_lab = re.search('2.050a', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2019_luismartinez_2.050a.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2019_luismartinez_2.050a.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)

        # test for a list
        with open(filename, 'r') as myfile:
            filename_data = myfile.read()

        search_object = re.search(r".+ = .* \[ .* \]", filename_data, re.X | re.M | re.S)

        test_list = {"name": "Testing that there is something looking like a list",
                     "pass": True,
                     "pass_message": "Pass! Submitted file looks like it has a list",
                     "fail_message": "Submitted file does not look like it has a list.",
                     }

        if not search_object:
            test_list['pass'] = False
        else:
            score_info['score'] += 3
        tests.append(test_list)


        # Check for uinput 
        cmd = 'grep "input" ' + filename + '  | wc -l  '
        c = delegator.run(cmd)
        inputs = int(c.out)
        test_input = {"name": "Testing that you ask the user for an input (3 points)",
                     "pass": True,
                     "pass_message": "Pass (for now).  You have ask the user for an input.  <br>",
                     "fail_message": "Fail.  You need to ask the user for an input<br>"
                                     "This translates to -3 points deduction.<br>",
                     }
        if inputs == 0:
            test_input['pass'] = False
        else:
            score_info['score'] += 3
        tests.append(test_input)

        # Find number of PEP8 errors
        cmd = '/home/ewu/CRLS_APCSP_autograder/venv1/bin/pycodestyle --max-line-length=120 ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        side_errors = int(c.out)
        test_pep8 = {"name": "Testing for PEP8 warnings and errors (7 points)",
                     "pass": True,
                     "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                     "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                                                                      "This translates to -" + str(
                         side_errors) + " point(s) deduction.<br>"
                     }
        if side_errors != 0:
            test_pep8['pass'] = False
        score_info['score'] += max(0, int(7) - side_errors)
        tests.append(test_pep8)


        # Check for help comment
        cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
        c = delegator.run(cmd)
        help_comments = int(c.out)
        test_help = {"name": "Testing that you got a help and documented it as a comment (2.5 points)",
                     "pass": True,
                     "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                                     "Be sure your comment is meaningful, otherwise this can be "
                                     "overturned on review.",
                     "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                                     " how somebody helped you with your code.  <br>"
                                     "If you didn't have any problems, then ask somebody to check that your code"
                                     " gives correct outputs, given an input.<br>"
                                     "This translates to -5 points deduction.<br>",
                     }
        if help_comments == 0:
            test_help['pass'] = False
        else:
            score_info['score'] += 2.5
        tests.append(test_help)

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_2050b')
def feedback_2050b():
    import re
    import subprocess
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 14.5, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2019', filename)
    find_lab = re.search('2.050b', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2019_luismartinez_2.050b.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2019_luismartinez_2.050b.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)

        # test for a 2 lists
        with open(filename, 'r') as myfile:
            filename_data = myfile.read()

        search_object = re.search(r".+ = .* \[ .* \] (.|\n)*  .+ = .* \[ .* \]  ", filename_data, re.X | re.M | re.S)

        test_twolist = {"name": "Testing that there is something looking like a 2 lists",
                        "pass": True,
                        "pass_message": "Pass! Submitted file looks like it has 2 lists",
                        "fail_message": "Submitted file does not look like it has 2 lists.",
        }

        if not search_object:
            test_twolist['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_twolist)

        # Find number of PEP8 errors
        cmd = '/home/ewu/CRLS_APCSP_autograder/venv1/bin/pycodestyle  --ignore=E305,E226  --max-line-length=120 ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        side_errors = int(c.out)
        test_pep8 = {"name": "Testing for PEP8 warnings and errors (7 points)",
                     "pass": True,
                     "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                     "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                                                                      "This translates to -" + str(
                         side_errors) + " point(s) deduction.<br>"
                     }
        if side_errors != 0:
            test_pep8['pass'] = False
        score_info['score'] += max(0, int(7) - side_errors)
        tests.append(test_pep8)

        # Check for help comment
        cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
        c = delegator.run(cmd)
        help_comments = int(c.out)
        test_help = {"name": "Testing that you got a help and documented it as a comment (2.5 points)",
                     "pass": True,
                     "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                                     "Be sure your comment is meaningful, otherwise this can be "
                                     "overturned on review.",
                     "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                                     " how somebody helped you with your code.  <br>"
                                     "If you didn't have any problems, then ask somebody to check that your code"
                                     " gives correct outputs, given an input.<br>"
                                     "This translates to -5 points deduction.<br>",
                     }
        if help_comments == 0:
            test_help['pass'] = False
        else:
            score_info['score'] += 2.5
        tests.append(test_help)

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


    
@app.route('/feedback_3011')
def feedback_3011():
    import re
    import subprocess
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 54, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2019', filename)
    find_lab = re.search('3.011', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2019_luismartinez_3.011.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2019_luismartinez_3.011.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)

        # test for a list
        with open(filename, 'r') as myfile:
            filename_data = myfile.read()

        search_object = re.search(r".+ = .* \[ .* \]", filename_data, re.X | re.M | re.S)

        test_list = {"name": "Testing that there is something looking like a list",
                     "pass": True,
                     "pass_message": "Pass! Submitted file looks like it has a list",
                     "fail_message": "Submitted file does not look like it has a list.",
                     }

        if not search_object:
            test_list['pass'] = False
        else:
            score_info['score'] += 10
        tests.append(test_list)

        # test for 4+ items list
        search_object = re.search(r".+ = .* \[ .* , .* , .* , .* , .* \]", filename_data, re.X | re.M | re.S)

        test_four_item_list = {"name": "Testing that there is something looking like a 4+ items in list",
                               "pass": True,
                               "pass_message": "Pass! Submitted file looks like it has 4+ items in list",
                               "fail_message": "Submitted file does not look like it has 4+ items in list.",
        }

        if not search_object:
            test_four_item_list['pass'] = False
        else:
            score_info['score'] += 10
        tests.append(test_four_item_list)

        # Check for any print
        cmd = 'grep "print" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        prints = int(c.out)
        test_print = {"name": "Testing for a print of any type (5 points)",
                      "pass": True,
                      "pass_message": "Pass (for now).  You have a print statment.  <br>",
                      "fail_message": "Fail.  You do not have a print of any sort <br>",
                      }
        if prints == 0:
            test_print['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_print)

        # Check for any input
        cmd = 'grep "input" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        inputs = int(c.out)
        test_input = {"name": "Testing for an input of any type (5 points)",
                      "pass": True,
                      "pass_message": "Pass (for now).  You have an input statment.  <br>",
                      "fail_message": "Fail.  You do not have an input of any sort <br>",
                      }
        if inputs == 0:
            test_input['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_input)

        # Check for any random at all
        cmd = 'grep "random" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        randoms = int(c.out)
        test_random = {"name": "Testing for an random of any type (5 points)",
                     "pass": True,
                     "pass_message": "Pass (for now).  You have an random statment.  <br>",
                     "fail_message": "Fail.  You do not have an random of any sort <br>",
                     }
        if randoms == 0:
            test_random['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_random)

        # Find number of PEP8 errors
        cmd = '/home/ewu/CRLS_APCSP_autograder/venv1/bin/pycodestyle  --ignore=E305,E226  --max-line-length=120 ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        side_errors = int(c.out)
        test_pep8 = {"name": "Testing for PEP8 warnings and errors (7 points)",
                     "pass": True,
                     "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                     "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                                                                      "This translates to -" + str(
                         side_errors) + " point(s) deduction.<br>"
                     }
        if side_errors != 0:
            test_pep8['pass'] = False
        score_info['score'] += max(0, int(14) - side_errors)
        tests.append(test_pep8)


        # Check for help comment
        cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
        c = delegator.run(cmd)
        help_comments = int(c.out)
        test_help = {"name": "Testing that you got a help and documented it as a comment (2.5 points)",
                     "pass": True,
                     "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                                     "Be sure your comment is meaningful, otherwise this can be "
                                     "overturned on review.",
                     "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                                     " how somebody helped you with your code.  <br>"
                                     "If you didn't have any problems, then ask somebody to check that your code"
                                     " gives correct outputs, given an input.<br>"
                                     "This translates to -5 points deduction.<br>",
                     }
        if help_comments == 0:
            test_help['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_help)

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)



def extract_functions(orig_file):
    import re
    outfile_name = orig_file.replace('.py', '.functions.py')
    outfile = open(outfile_name, 'w')
    with open(orig_file) as infile:
        line = True
        while line:
            print("starting over looking for function")
            print('reading this ' + str(line))
            line = infile.readline()
            start_def = re.search("^(def) \s+ .+ " , line,  re.X | re.M | re.S)
            if start_def:
                print("entering function!")
                print('writing this' + str(line))
                outfile.write(line)
                print("reading this" + str(line))
                #                   line = infile.readline()
                #                   inside_function = re.search("^\s+ .+ " , line,  re.X | re.M | re.S)
                inside_function = True
                while inside_function:
                    print('reading this ' + str(line))
                    line = infile.readline()
                    inside_function = re.search("^(\s+ | \# ) .+ " , line,  re.X | re.M | re.S)
                    if inside_function:
                        print("writing this inside function " + str(line))
                        outfile.write(line)
                outfile.write(line)
                
def extract_single_function(orig_file, function):
    import re
    function_file = orig_file.replace('.py', '.functions.py')
    extracted_function = ''
    with open(function_file) as infile:
        line = True
        while line:
            print("looking for this function : " + function)
            line = infile.readline()
            start_def = re.search("^(def) \s+ " + function , line,  re.X | re.M | re.S)
            if start_def:
                print("entering function!")
                print('writing this' + str(line))
                extracted_function += line
                print("reading this" + str(line))
                inside_function = True
                while inside_function:
                    print('reading this ' + str(line))
                    line = infile.readline()
                    inside_function = re.search("^(\s+ | \# ) .+ " , line,  re.X | re.M | re.S)
                    if inside_function:
                        print("writing this inside function " + str(line))
                        extracted_function += line
                extracted_function += line
    return extracted_function
                  
    # with open(orig_file) as infile:
    #        line = True
    #        while line:
    #            print("starting over looking for function")
    #            line = infile.readline()
    #            print(line)
    #            start_def = re.search("^(def) \s+ .+ " , line,  re.X | re.M | re.S)
    #            if start_def:
    #                outfile.write(line)
    #                print("this function!")
    #                line = infile.readline()
    #                print(line)
    #                inside_function = re.search("^\s+ .+ " , line,  re.X | re.M | re.S)
    #                while inside_function:
    #                    line = infile.readline()
    #                    outfile.write(line)
    #                    print("inside function " + line)
    #                    inside_function = re.search("^\s+ .+ " , line,  re.X | re.M | re.S)
                                                                                                                                                                               
#   
    
#    with open(orig_file) as infile:
#        for line in infile.readlines():
#            print(line)
#            start_def = re.match("^(def) \s+ .+ " , line,  re.X | re.M | re.S)
#            outfile.write(line)
#            if start_def:
#                 keep_line = re.match("^\s+ .+ " , line,  re.X | re.M | re.S)
#                 if keep_line:
#                     outfile.write(line)


#            keep_line = re.match("^([^a-z] | def ) \s+ .+ " , line,  re.X | re.M | re.S)
#            if keep_line:
#                print("keep this line: " + line)
#                outfile.write(line)
                


@app.route('/feedback_3020')
def feedback_3020():
    import re
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 61, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2019', filename)
    find_lab = re.search('3.020', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2019_luismartinez_3.020.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2019_luismartinez_3.020.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)

        # Check for function birthday_song
        cmd = 'grep "def birthday_song(" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        birthday_song = int(c.out)
        test_birthday_song = {"name": "Testing that birthday song function exists (4 points)",
                              "pass": True,
                              "pass_message": "Pass.  birthday_song function exists.  <br>",
                              "fail_message": "Fail.  birthday_song function isn't in the code. <br>"
                                              "It may be spelled incorrectly.  The function needs to be named "
                                              "birthday_song, exactly."
                                              "Fix code and resubmit. <br>",
        }
        if birthday_song == 0:
            test_birthday_song['pass'] = False
        else:
            score_info['score'] += 4
        tests.append(test_birthday_song)

        # Only continue if you have a birthday_song_function
        if test_birthday_song['pass']:
            # Check that function is called once
            test_birthday_song_run = {"name": "Testing that birthday song function is called at least once (4 points)",
                                      "pass": False,
                                      "pass_message": "Pass.  birthday_song function is called.  <br>",
                                      "fail_message": "Fail.  birthday_song function isn't called in the code. <br>"
            }
            with open(filename) as infile:
                for line in infile.readlines():
                    found = re.match("(?<!def\s)birthday_song" , line,  re.X | re.M | re.S)
                    if found:
                        test_birthday_song_run['pass'] = True
            infile.close()
            if test_birthday_song_run['pass']:
                score_info['score'] += 4
            tests.append(test_birthday_song_run)

            # test that output of any sort with happy birthday

            # extract functions and create python test file
            extract_functions(filename)
            functions_filename = filename.replace('.py', '.functions.py')
            cmd = ' cat ' + functions_filename + \
                  ' /home/ewu/CRLS_APCSP_autograder/var/3.020.test.py > /tmp/3.020.test.py'
            c = delegator.run(cmd)
            if c.err:
                flash("There was a problem creating the python test file")


            # test to see happy birthday output spits out 'birthday'
            cmd = 'python3 /tmp/3.020.test.py testAutograde.test_happy_birthday 2>&1 |grep -i fail |wc -l'
            c = delegator.run(cmd)
            failures = int(c.out)
            test_birthday_song_birthday =  {"name": "Testing that birthday song function is "
                                                    "prints 'birthday' (4 points)",
                                            "pass": True,
                                            "pass_message": "Pass.  birthday_song function prints 'birthday'.  <br>",
                                            "fail_message": "Fail.  birthday_song function doesn't print 'birthday'."
                                                            " <br>"
            }
            if failures > 0:
                test_birthday_song_birthday['pass'] = False
            else:
                score_info['score'] += 4
            tests.append(test_birthday_song_birthday)

            # test to see happy birthday output spits out argument
            cmd = 'python3 /tmp/3.020.test.py testAutograde.test_happy_birthday_output 2>&1 |grep -i fail |wc -l'
            c = delegator.run(cmd)
            failures = int(c.out)
            test_birthday_song_argument = {"name": "Testing that birthday song function is "
                                                   "prints the argument (5 points)",
                                           "pass": True,
                                           "pass_message": "Pass.  birthday_song function prints the argument.  <br>",
                                           "fail_message": "Fail.  birthday_song function doesn't print argument. <br>"
                                                           "For example, if you call birthday_song('Martinez'), the"
                                                           "function should print out 'Martinez' somewhere in there<br>"
                                           }
            if failures > 0:
                test_birthday_song_argument['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_birthday_song_argument)

            # Check for function pick_card
            cmd = 'grep "def pick_card(" ' + filename + ' | wc -l  '
            c = delegator.run(cmd)
            pick_card = int(c.out)
            test_pick_card = {"name": "Testing that pick_card function exists (4 points)",
                                  "pass": True,
                                  "pass_message": "Pass.  pick_card function exists.  <br>",
                                  "fail_message": "Fail.  pick_card function isn't in the code. <br>"
                                  "It may be spelled incorrectly.  The function needs to be named "
                                  "pick_card, exactly."
                                  "Fix code and resubmit. <br>",
            }
            if pick_card == 0:
                test_pick_card['pass'] = False
            else:
                score_info['score'] += 4
            tests.append(test_pick_card)

            # test for 4+ items list named cards
#            search_object = re.search(r"cards \s* = \s* \[ .* , .* , .* , .*\]", filename, re.X | re.M | re.S)

            with open(filename, 'r') as myfile:
                filename_data = myfile.read()

            search_object = re.search(r"\s* cards \s* = \s* \[ .* , .* , .* \]", filename_data, re.X | re.M | re.S)
            test_cards_list = {"name": "Testing that there is a list named cards with 4+ items (2 points)",
                                   "pass": True,
                                   "pass_message": "Pass! Submitted file looks like it has a list named "
                                                   "cards with 4+ items",
                                   "fail_message": "Submitted file does not look like it has a list named "
                                                   "'cards' with 4+ items. <br>"
                                                   "The list must be named exactly 'cards'",
            }
            
            if not search_object:
                test_cards_list['pass'] = False
            else:
                score_info['score'] += 2
            tests.append(test_cards_list)

            # test for 4+ items list named suits
            search_object = re.search(r"\s* suits \s* = .* \[ .* , .* , .* , .* \]", filename_data, re.X | re.M | re.S)
            
            test_suits_list = {"name": "Testing that there is a list named suits with 4+ items (2 points)",
                                   "pass": True,
                                   "pass_message": "Pass! Submitted file looks like it has a list named suits with 4+ items",
                                   "fail_message": "Submitted file does not look like it has a list named 'suits' with 4 items. <br>"
                                                   "The list must be named exactly 'suits'",
            }
            
            if not search_object:
                test_suits_list['pass'] = False
            else:
                score_info['score'] += 2
            tests.append(test_suits_list)

            # test to see pick_card output spits out 1 'of'
            cmd = 'python3 /tmp/3.020.test.py testAutograde.test_pick_card_output 2>&1 |grep -i fail |wc -l'
            c = delegator.run(cmd)
            failures = int(c.out)
            test_pick_card_function =  {"name": "Testing that pick_card_output function gives 1 card ",
                                            "pass": True,
                                            "pass_message": "Pass.  pick_card function prints 'of' once "
                                                            "(assume this means prints 1 card).  <br>",
                                            "fail_message": "Fail.  pick_card function doesn't 'of' once. "
                                                            "Expecting to see '1 of hearts' or something like that.<br>"
                                                            "Function should print just ONE card. <br>"
            }
            if failures > 0:
                test_pick_card_function['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_pick_card_function)


            # Check that pick_card function is called once
            test_pick_card_run = {"name": "Testing that pick_card function is called at least once (4 points)",
                                  "pass": False,
                                  "pass_message": "Pass.  pick_card function is called.  <br>",
                                  "fail_message": "Fail.  pick_card function isn't called in the code. <br>"
                                  "If this fails, but you think it should not, try to do this: <br>"
                                  "pick_card()<br>"
                                  "(do it at the beginning of the line instead in a loop)",
                               
            }
            with open(filename) as infile:
                for line in infile.readlines():
                    found = re.match("(?<!def\s)pick_card" , line,  re.X | re.M | re.S)
                    if found:
                        test_pick_card_run['pass'] = True
            infile.close()
            if test_pick_card_run['pass']:
                score_info['score'] += 4
            tests.append(test_pick_card_run)

            
            # test 2 funs and verify they are different
            filename_output1 = filename + '.out1'
            filename_output2 = filename + '.out2'

            cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/3.020.in > ' \
                  + filename_output1
            c = delegator.run(cmd)
            if c.err:
                flash('bad! You have an error somewhere in running program check 3.020.in')
            cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/3.020.in > ' \
                  + filename_output2
            c = delegator.run(cmd)
            if c.err:
                flash('bad! You have an error somewhere in running program check 3.020.in')

            cmd = 'diff ' + filename_output1 + ' ' + filename_output2 + ' | wc -l'
            c = delegator.run(cmd)
            different_lines = int(c.out)
            test_pick_cards_different_outputs =  {"name": "Testing that pick_card shows random behavior when code is run (4 points) ",
                                                  "pass": True,
                                                  "pass_message": "Pass. pick_card shows random behavior when code is run. <br>",
                                                  "fail_message": "Fail. pick_card doesn't show random behavior. <br>"
                                                                  "Be sure that you are calling pick_card.<br>"
                                                                  "Be sure that pick_card uses random numbers.",
            }
            if different_lines == 0:
                test_pick_cards_different_outputs['pass'] = False
            else:
                score_info['score'] += 4
            tests.append(test_pick_cards_different_outputs)

            # check that pick_card prints out 10 cards (looks for 'of' 10x)
            test_run_ten_cards = {
                "name": "Testing that program draws 10 cards (4 points) ",
                "pass": True,
                "pass_message": "Pass. program draws 10 cards. <br>",
                "fail_message": "Fail. program doesn't draw 10 cards. <br>"
                                "looking for something like this: <br>"
                                "2 of hearts <br>"
                                "3 of spades <br>"
                                "K of diamonds <br>"
                                "9 of clubs <br>"
                                "etc... for 10 cards.  card OF suit<br>",
                }

            num_ofs = 0
            with open(filename_output2) as infile:
                for line in infile.readlines():
                    found = re.search(r"of", line,  re.X | re.M | re.S)
                    if found:
                        num_ofs += 1
            infile.close()
            flash(num_ofs)
            if num_ofs <= 9:
                test_run_ten_cards['pass'] = False
            else:
                score_info['score'] += 4
            tests.append(test_run_ten_cards)

            # Find number of PEP8 errors
            cmd = '/home/ewu/CRLS_APCSP_autograder/venv1/bin/pycodestyle  --ignore=E305,E226 --max-line-length=120 ' + filename + ' | wc -l  '
            c = delegator.run(cmd)
            side_errors = int(c.out)
            test_pep8 = {"name": "Testing for PEP8 warnings and errors (14 points)",
                         "pass": True,
                         "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                         "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                                                                          "This translates to -" + str(
                             side_errors) + " point(s) deduction.<br>"
                         }
            if side_errors != 0:
                test_pep8['pass'] = False
            score_info['score'] += max(0, int(14) - side_errors)
            tests.append(test_pep8)


            # Check for help comment
            cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
            c = delegator.run(cmd)
            help_comments = int(c.out)
            test_help = {"name": "Testing that you got a help and documented it as a comment (5 points)",
                         "pass": True,
                         "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                                         "Be sure your comment is meaningful, otherwise this can be "
                                         "overturned on review.",
                         "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                                         " how somebody helped you with your code.  <br>"
                                         "If you didn't have any problems, then ask somebody to check that your code"
                                         " gives correct outputs, given an input.<br>"
                                         "This translates to -5 points deduction.<br>",
                         }
            if help_comments == 0:
                test_help['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_help)

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)

            # found = re.match("(?<!def\s)birthday_song" , line,  re.X | re.M | re.S)
            # if found:
            #     test_birthday_song_run['pass'] = True
            #     infile.close()
            #
            #
            #
            #
            # # Check for function pick_card
            # cmd = 'grep "def pick_card(" ' + filename + ' | wc -l  '
            # c = delegator.run(cmd)
            # pick_card = int(c.out)
            # test_pick_card = {"name": "Testing that birthday song function exists (4 points)",
            #                   "pass": True,
            #                   "pass_message": "Pass.  pick_card function exists.  <br>",
            #                   "fail_message": "Fail.  pick_card function isn't in the code.  <br>",
            # }
            # if pick_card == 0:
            #     test_pick_card['pass'] = False
            # else:
            #     score_info['score'] += 4
            #     tests.append(test_pick_card)
            #
            #
        else:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)










    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_3026')
def feedback_3026():
    import re
    import subprocess
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 44.5, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2019', filename)
    find_lab = re.search('3.026', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2019_luismartinez_3.026.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2019_luismartinez_3.026.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)

        # Check for function return_min
        cmd = 'grep "def return_min(" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        return_min = int(c.out)
        test_return_min = {"name": "Testing that return_min function exists (5 points)",
                              "pass": True,
                              "pass_message": "Pass.  return_min function exists.  <br>",
                              "fail_message": "Fail.  return_min function isn't in the code. <br>"
                                              "It may be spelled incorrectly.  The function needs to be named "
                                              "return_min, exactly."
                                              "Fix code and resubmit. <br>",
        }
        if return_min == 0:
            test_return_min['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_return_min)

        # Only continue if you have a return_min_function
        if test_return_min['pass']:
            # Check that function is called once
            test_return_min_run = {"name": "Testing that return_min function is called at least once (5 points)",
                                   "pass": False,
                                   "pass_message": "Pass.  return_min function is called.  <br>",
                                   "fail_message": "Fail.  return_min function isn't called in the code. <br>"
            }
            with open(filename) as infile:
                for line in infile.readlines():
                    found = re.search("(?<!def\s)return_min" , line,  re.X | re.M | re.S)
                    if found:
                        test_return_min_run['pass'] = True
            infile.close()
            if test_return_min_run['pass']:
                score_info['score'] += 5
            tests.append(test_return_min_run)

            # test that there is a 'return' anywhere in the code
            test_return = {"name": "Testing that there is a 'return' in the code (5 points)",
                           "pass": False,
                           "pass_message": "Pass.  'return <something>' in the code.  <br>",
                           "fail_message": "Fail.  'return <something> is nowhere to be round in the code. <br>"
                           " Be sure that your function return_min returns the value of the minimum item at the "
                                           "end.<br>",
            }

            with open(filename) as infile:
                for line in infile.readlines():
                    found = re.search("return \s .+" , line,  re.X | re.M | re.S)
                    if found:
                        test_return['pass'] = True
            infile.close()
            if test_return['pass']:
                score_info['score'] += 5
            tests.append(test_return)
            
            # extract functions and create python test file
            extract_functions(filename)
            functions_filename = filename.replace('.py', '.functions.py')
            cmd = ' cat ' + functions_filename + \
                  ' /home/ewu/CRLS_APCSP_autograder/var/3.026.test.py > /tmp/3.026.test.py'
            c = delegator.run(cmd)
            if c.err:
                flash("There was a problem creating the python test file")


            # test1 for return_min
            cmd = 'python3 /tmp/3.026.test.py testAutograde.test_return_min_1 2>&1 |grep -i fail |wc -l'
            c = delegator.run(cmd)
            failures = int(c.out)
            test_return_min_1 =  {"name": "Testing calling return_min with list [-1, 3, 5, 99] returns -1",
                                  "pass": True,
                                  "pass_message": "Pass. Calling return_min with list [-1, 3, 5, 99] returns -1.  <br>",
                                  "fail_message": "Fail.   Calling return_min with list [-1, 3, 5, 99] doesn't return -1."
                                                            " You should test your return_min to see what it returns <br>"
            }
            if failures > 0:
                test_return_min_1['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_return_min_1)


            # test2 for return_min
            cmd = 'python3 /tmp/3.026.test.py testAutograde.test_return_min_2 2>&1 |grep -i fail |wc -l'
            c = delegator.run(cmd)
            failures = int(c.out)
            test_return_min_2 =  {"name": "Testing calling return_min with list [-1, 3, 5, -99] returns -99",
                                  "pass": True,
                                  "pass_message": "Pass. Calling return_min with list [-1, 3, 5, -99] returns -99.  <br>",
                                  "fail_message": "Fail.   Calling return_min with list [-1, 3, 5, -99] doesn't return -99."
                                                            " You should test your return_min to see what it returns <br>"
            }
            if failures > 0:
                test_return_min_2['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_return_min_2)


            # test3 for return_min
            cmd = 'python3 /tmp/3.026.test.py testAutograde.test_return_min_3 2>&1 |grep -i fail |wc -l'
            c = delegator.run(cmd)
            failures = int(c.out)
            test_return_min_3 =  {"name": "Testing calling return_min with list [5] returns 5",
                                  "pass": True,
                                  "pass_message": "Pass. Calling return_min with list [5] returns 5.  <br>",
                                  "fail_message": "Fail.   Calling return_min with list [5] doesn't return 5."
                                                            " You should test your return_min to see what it returns <br>"
            }
            if failures > 0:
                test_return_min_3['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_return_min_3)


            # test4 for return_min
            cmd = 'python3 /tmp/3.026.test.py testAutograde.test_return_min_4 2>&1 |grep -i fail |wc -l'
            c = delegator.run(cmd)
            failures = int(c.out)
            test_return_min_4 =  {"name": "Testing calling return_min with list "
                                          "[5, 4, 99, -11, 44, -241, -444, -999, 888, -2] returns -444",
                                  "pass": True,
                                  "pass_message": "Pass. Calling return_min with list "
                                                  "[5, 4, 99, -11, 44, -241, -444, -999, 888, -2] returns -444.  <br>",
                                  "fail_message": "Fail.   Calling return_min with list list "
                                                  "[5, 4, 99, -11, 44, -241, -444, -999, 888, -2] doesn't return -444."
                                                  " You should test your return_min to see what it returns <br>"
            }
            if failures > 0:
                test_return_min_4['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_return_min_4)
            
            # Find number of PEP8 errors
            cmd = '/home/ewu/CRLS_APCSP_autograder/venv1/bin/pycodestyle --ignore=E305,E226 --max-line-length=120 ' + filename + ' | wc -l  '
            c = delegator.run(cmd)
            side_errors = int(c.out)
            test_pep8 = {"name": "Testing for PEP8 warnings and errors (7 points)",
                         "pass": True,
                         "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                         "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                                                                          "This translates to -" + str(
                             side_errors) + " point(s) deduction.<br>"
                         }
            if side_errors != 0:
                test_pep8['pass'] = False
            score_info['score'] += max(0, int(7) - side_errors)
            tests.append(test_pep8)

            # Check for help comment
            cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
            c = delegator.run(cmd)
            help_comments = int(c.out)
            test_help = {"name": "Testing that you got a help and documented it as a comment (2.5 points)",
                         "pass": True,
                         "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                                         "Be sure your comment is meaningful, otherwise this can be "
                                         "overturned on review.",
                         "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                                         " how somebody helped you with your code.  <br>"
                                         "If you didn't have any problems, then ask somebody to check that your code"
                                         " gives correct outputs, given an input.<br>"
                                         "This translates to -2.5 points deduction.<br>",
                         }
            if help_comments == 0:
                test_help['pass'] = False
            else:
                score_info['score'] += 2.5
            tests.append(test_help)

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)

        else:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_4011')
def feedback_4011():
    import re
    import subprocess
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 69, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2019', filename)
    find_lab = re.search('4.011', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2019_luismartinez_4.011.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2019_luismartinez_4.011.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)

        # Check for function could_it_be_a_martian_word
        cmd = 'grep "def could_it_be_a_martian_word([[a-zA-Z]\+[^,]*)" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        function_name = int(c.out)
        test_function_name = {"name": "Testing that could_it_be_a_martian_word function exists with one input parameter (5 points)",
                              "pass": True,
                              "pass_message": "Pass.   could_it_be_a_martian_word function exists with one input parameter  <br>",
                              "fail_message": "Fail.   could_it_be_a_martian_word function exists with one input parameter isn't in the code. <br>"
                              "It may be spelled incorrectly.  The function needs to be named exactly correctly<br>"
                              "The function needs exactly one input parameter. <br>"
                              "Fix code and resubmit. <br>",
        }
        if function_name == 0:
            test_function_name['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_function_name)

        # Only continue if you have a function_name correct
        if test_function_name['pass']:

            # Check for a loop of some sort (for or while)
            cmd = 'grep -E "for|while"  ' + filename + ' | wc -l  '
            c = delegator.run(cmd)
            loop = int(c.out)
            test_loop = {"name": "Testing that program has a loop. (5 points)",
                         "pass": True,
                         "pass_message": "Pass.  Testing that program has a loop.  <br>",
                         "fail_message": "Fail.  Testing that program has a loop (assume a while or for means you have a loop) <br>"
                         "The program needs a while or a for. <br>"
                         "Fix code and resubmit. <br>",
            }
            if loop == 0:
                test_loop['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_loop)

            # Check for 3 ifs on different lines
            cmd = 'grep "if" ' + filename + ' | wc -l  '
            c = delegator.run(cmd)
            ifs = int(c.out)
            test_ifs = {"name": "Testing that program is efficient. (5 points)",
                        "pass": True,
                        "pass_message": "Pass.  Testing that program is efficient.  <br>",
                        "fail_message": "Fail.  Testing that program is efficient<br>"
                        
                        "Are you using an if/if/if/if or if/elif/elif/elif? <br>"
                        "Check HW11.  Using if/elif/elif can get really big code with a lot of conditions <br>",
            }
            if ifs >= 3:
                test_ifs['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_ifs)


            # Check that function is called 3x
            test_function_run = {"name": "Testing that could_it_be_a_martian_word function is called at least once (10 points)",
                                 "pass": False,
                                 "pass_message": "Pass.  could_it_be_a_martian_word function is called at least once <br>",
                                 "fail_message": "Fail.  could_it_be_a_martian_word function is not called at least once  <br>"
            }
            count = 1
            with open(filename) as infile:
                for line in infile.readlines():
                    found = re.search("(?<!def\s)could_it_be_a_martian_word" , line,  re.X | re.M | re.S)
                    if found:
                        count += 1
            infile.close()
            if count >= 2:
                test_function_run['pass'] = True
                score_info['score'] += 5
            tests.append(test_function_run)

            # extract functions and create python test file
            extract_functions(filename)
            functions_filename = filename.replace('.py', '.functions.py')
            cmd = ' cat ' + functions_filename + \
                  ' /home/ewu/CRLS_APCSP_autograder/var/4.011.test.py > /tmp/4.011.test.py'
            c = delegator.run(cmd)
            if c.err:
                flash("There was a problem creating the python test file")


            # test1 for could_it_be_a_martian_word
            cmd = 'python3 /tmp/4.011.test.py testAutograde.test_could_it_be_a_martian_word_1 2>&1 |grep -i fail |wc -l'
            c = delegator.run(cmd)
            failures = int(c.out)
            test_could_it_be_a_martian_word_1 =  {"name": "Testing calling could_it_be_a_martian_word with 'bcdefgijnpqrstuvwxyz' returns []",
                                                  "pass": True,
                                                  "pass_message": "Pass. Calling could_it_be_a_martian_word 'bcdefgijnpqrstuvwxyz' returns [].  <br>",
                                                  "fail_message": "Fail.   Calling could_it_be_a_martian_word  'bcdefgijnpqrstuvwxyz' doesn't return []."
                                                  " You should test your could_it_be_a_martian_word to see what it returns <br>"
            }
            if failures > 0:
                test_could_it_be_a_martian_word_1['pass'] = False
            else:
                score_info['score'] += 10
            tests.append(test_could_it_be_a_martian_word_1)


            # test2 for could_it_be_a_martian_word
            cmd = 'python3 /tmp/4.011.test.py testAutograde.test_could_it_be_a_martian_word_2 2>&1 |grep -i fail |wc -l'
            c = delegator.run(cmd)
            failures = int(c.out)
            test_could_it_be_a_martian_word_2 =  {"name": "Testing calling could_it_be_a_martian_word with string 'ba' returns ['a']",
                                                  "pass": True,
                                                  "pass_message": "Pass. Calling could_it_be_a_martian_word with string ba returns ['a'].  <br>",
                                                  "fail_message": "Fail.   Calling could_it_be_a_martian_word with string ba returns ['a']."
                                                  " You should test your could_it_be_a_martian_word to see what it returns <br>"
            }
            if failures > 0:
                test_could_it_be_a_martian_word_2['pass'] = False
            else:
                score_info['score'] += 10
            tests.append(test_could_it_be_a_martian_word_2)


            # test3 for could_it_be_a_martian_word
            cmd = 'python3 /tmp/4.011.test.py testAutograde.test_could_it_be_a_martian_word_3 2>&1 |grep -i fail |wc -l'
            c = delegator.run(cmd)
            failures = int(c.out)
            test_could_it_be_a_martian_word_3 = {"name": "Testing calling could_it_be_a_martian_word with string "
                                                          "'baa' returns ['a']",
                                                  "pass": True,
                                                  "pass_message": "Pass. Calling could_it_be_a_martian_word with string"
                                                                  " 'baa' returns ['a'].  <br>",
                                                  "fail_message": "Fail.   Calling could_it_be_a_martian_word with "
                                                                  "string 'baa' doesn't return ['a']."
                                                  " You should test your could_it_be_a_martian_word to see what it "
                                                                  "returns <br>"
            }
            if failures > 0:
                test_could_it_be_a_martian_word_3['pass'] = False
            else:
                score_info['score'] += 10
            tests.append(test_could_it_be_a_martian_word_3)


            
            # Find number of PEP8 errors
            cmd = '/home/ewu/CRLS_APCSP_autograder/venv1/bin/pycodestyle --ignore=E305,E226 --max-line-length=120 ' + filename + ' | wc -l  '
            c = delegator.run(cmd)
            side_errors = int(c.out)
            test_pep8 = {"name": "Testing for PEP8 warnings and errors (14 points)",
                         "pass": True,
                         "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                         "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                                                                          "This translates to -" + str(
                             side_errors) + " point(s) deduction.<br>"
                         }
            if side_errors != 0:
                test_pep8['pass'] = False
            score_info['score'] += max(0, int(14) - side_errors)
            tests.append(test_pep8)


            # Check for help comment
            cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
            c = delegator.run(cmd)
            help_comments = int(c.out)
            test_help = {"name": "Testing that you got a help and documented it as a comment (5 points)",
                         "pass": True,
                         "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                                         "Be sure your comment is meaningful, otherwise this can be "
                                         "overturned on review.",
                         "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                                         " how somebody helped you with your code.  <br>"
                                         "If you didn't have any problems, then ask somebody to check that your code"
                                         " gives correct outputs, given an input.<br>"
                                         "This translates to -2.5 points deduction.<br>",
                         }
            if help_comments == 0:
                test_help['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_help)

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)

        else:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_4021')
def feedback_4021():
    import re
    import subprocess
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 34.5, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2019', filename)
    find_lab = re.search('4.021', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2019_luismartinez_4.021.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2019_luismartinez_4.021.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)

        # Check for function return_min
        cmd = 'grep "^def the_rock_says([a-zA-Z_]\+[^,])" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)

        the_rock_says = int(c.out)
        cmd = 'grep "the_rock_says([a-zA-Z_]\+[^,])" ' + filename + '   '
        c = delegator.run(cmd)
        if c.err:
            flash("Grepping for the_rock_says failed")
        test_the_rock_says = {"name": "Testing that the_rock_says function exists with one input argument (5 points)",
                              "pass": True,
                              "pass_message": "Pass.   the_rock_says function exists with one input argument  <br>",
                              "fail_message": "Fail.   the_rock_says function exists with one input argument. <br>"
                                              "It may be spelled incorrectly.  The function needs to be named "
                                              "the_rock_says, exactly. <br>"
                                              "You may not have one input argument.  You need one.<br>"
                                              "Fix code and resubmit. <br>",
        }
        if the_rock_says == 0:
            test_the_rock_says['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_the_rock_says)

        # Only continue if you have a the_rock_says function
        if test_the_rock_says['pass']:
            # Check that function is called 3x
            test_the_rock_says_run = {"name": "Testing that the_rock_says function is called at least once (5 points)",
                                          "pass": False,
                                          "pass_message": "Pass.  the_rock_says function is called.  <br>",
                                          "fail_message": "Fail.  the_rock_says function isn't called in the code. <br>"
            }
            with open(filename) as infile:
                for line in infile.readlines():
                    found = re.search("(?<!def\s)the_rock_says" , line,  re.X | re.M | re.S)
                    if found:
                        test_the_rock_says_run['pass'] = True
            infile.close()
            if test_the_rock_says_run['pass']:
                score_info['score'] += 5
            tests.append(test_the_rock_says_run)

            # extract functions and create python test file
            extract_functions(filename)
            functions_filename = filename.replace('.py', '.functions.py')
            cmd = ' cat ' + functions_filename + \
                  ' /home/ewu/CRLS_APCSP_autograder/var/4.021.test.py > /tmp/4.021.test.py'
            c = delegator.run(cmd)
            if c.err:
                flash("There was a problem creating the python test file")


            # test1 for the_rock_says
            cmd = 'python3 /tmp/4.021.test.py testAutograde.test_the_rock_says_1 2>&1 |grep -i fail |wc -l'
            c = delegator.run(cmd)
            failures = int(c.out)
            test_the_rock_says_1 = {"name": "Testing calling the_rock_says with list ['eggs', 'apple'] returns a list "
                                            "['The Rock says eggs', 'The Rock says apple']",
                                    "pass": True,
                                    "pass_message": "Pass. Calling the_rock_says with list ['eggs', 'apple'] returns a list"
                                                    " ['The Rock says eggs', 'The Rock says apple'] <br>",
                                    "fail_message": "Fail.   Calling the_rock_says with list ['eggs', 'apple'] doesn't return a list ['The Rock says eggs'"
                                    ",'The Rock says apple']."
                                    " You should test your the_rock_says function to see what it returns <br>"
                                    " If you think it is correct, check your capitalization. "
            }
            if failures > 0:
                test_the_rock_says_1['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_the_rock_says_1)


            # test2 for the_rock_says
            cmd = 'python3 /tmp/4.021.test.py testAutograde.test_the_rock_says_2 2>&1 |grep -i fail |wc -l'
            c = delegator.run(cmd)
            failures = int(c.out)
            test_the_rock_says_2 =  {"name": "Testing calling the_rock_says with list ['eggs', 'smell'] returns ['The Rock says eggs', 'Do you smell what The Rock is cooking']",
                                     "pass": True,
                                     "pass_message": "Pass. Calling the_rock_says with list ['eggs', 'smell'] returns ['The Rock says eggs', 'Do you smell what The Rock is cooking']",
                                     "fail_message": "Fail.  Calling the_rock_says with list ['eggs', 'smell'] doesn't return ['The Rock says eggs', 'Do you smell what The Rock is cooking']"
                                     " You should test your the_rock_says functionto see what it returns <br>"
                                     " If you think it is correct, check your capitalization",
            }
            if failures > 0:
                test_the_rock_says_2['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_the_rock_says_2)


            # test3 for the_rock_says
            cmd = 'python3 /tmp/4.021.test.py testAutograde.test_the_rock_says_3 2>&1 |grep -i fail |wc -l'
            c = delegator.run(cmd)
            failures = int(c.out)
            test_the_rock_says_3 =  {"name": "Testing calling the_rock_says with list ['smog', 'smells', 'smashmouth'] returns ['Do you smell what The Rock is cooking', 'Do you smellell what The Rock is cooking', 'Do you smellellellellellellell what The Rock is cooking']",
                                     "pass": True,
                                     "pass_message": "Pass. Calling the_rock_says with list ['smog', 'smells', 'smashmouth'] returns correct answer.  <br>",
                                     "fail_message": "Fail.   Calling the_rock_says with list ['smog', 'smells', 'smashmouth'] returns ['Do you smell what The Rock is cooking', 'Do you smellell what The Rock is cooking', 'Do you smellellellellellellell what The Rock is cooking']"
                                                            " You should test your the_rock_says to see what it returns <br>"
                                     " If you think it is correct, check your capitalization",

            }
            if failures > 0:
                test_the_rock_says_3['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_the_rock_says_3)

            # Find number of PEP8 errors
            cmd = '/home/ewu/CRLS_APCSP_autograder/venv1/bin/pycodestyle --ignore=E305,E226 --max-line-length=120 ' + filename + ' | wc -l  '
            c = delegator.run(cmd)
            side_errors = int(c.out)
            test_pep8 = {"name": "Testing for PEP8 warnings and errors (7 points)",
                         "pass": True,
                         "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                         "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                                                                          "This translates to -" + str(
                             side_errors) + " point(s) deduction.<br>"
                         }
            if side_errors != 0:
                test_pep8['pass'] = False
            score_info['score'] += max(0, int(7) - side_errors)
            tests.append(test_pep8)


            # Check for help comment
            cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
            c = delegator.run(cmd)
            help_comments = int(c.out)
            test_help = {"name": "Testing that you got a help and documented it as a comment (2.5 points)",
                         "pass": True,
                         "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                                         "Be sure your comment is meaningful, otherwise this can be "
                                         "overturned on review.",
                         "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                                         " how somebody helped you with your code.  <br>"
                                         "If you didn't have any problems, then ask somebody to check that your code"
                                         " gives correct outputs, given an input.<br>"
                                         "This translates to -2.5 points deduction.<br>",
                         }
            if help_comments == 0:
                test_help['pass'] = False
            else:
                score_info['score'] += 2.5
            tests.append(test_help)

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)

        else:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_4022')
def feedback_4022():
    import re
    import subprocess
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 34.5, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2019', filename)
    find_lab = re.search('4.022', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2019_luismartinez_4.022.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2019_luismartinez_4.022.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)

        # Check for function bad_lossy_compression
        cmd = 'grep "^def bad_lossy_compression([a-zA-Z_]\+[^,])" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)

        bad_lossy_compression = int(c.out)
        cmd = 'grep "bad_lossy_compression([a-zA-Z_]\+[^,])" ' + filename + '   '
        c = delegator.run(cmd)
        if c.err:
            flash("Grepping for bad_lossy_compression failed")
        test_bad_lossy_compression = {"name": "Testing that bad_lossy_compression function exists with one input argument (5 points)",
                              "pass": True,
                              "pass_message": "Pass.   bad_lossy_compression function exists with one input argument  <br>",
                              "fail_message": "Fail.   bad_lossy_compression function exists with one input argument. <br>"
                                              "It may be spelled incorrectly.  The function needs to be named "
                                              "bad_lossy_compression, exactly. <br>"
                                              "You may not have one input argument.  You need one.<br>"
                                              "Fix code and resubmit. <br>",
        }
        if bad_lossy_compression == 0:
            test_bad_lossy_compression['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_bad_lossy_compression)

        # Only continue if you have a bad_lossy_compression function
        if test_bad_lossy_compression['pass']:
            # Check that function is called 
            test_bad_lossy_compression_run = {"name": "Testing that bad_lossy_compression function is called at least once (5 points)",
                                          "pass": False,
                                          "pass_message": "Pass.  bad_lossy_compression function is called.  <br>",
                                          "fail_message": "Fail.  bad_lossy_compression function isn't called in the code. <br>"
            }
            with open(filename) as infile:
                for line in infile.readlines():
                    found = re.search("(?<!def\s)bad_lossy_compression" , line,  re.X | re.M | re.S)
                    if found:
                        test_bad_lossy_compression_run['pass'] = True
            infile.close()
            if test_bad_lossy_compression_run['pass']:
                score_info['score'] += 5
            tests.append(test_bad_lossy_compression_run)

            # extract functions and create python test file
            extract_functions(filename)
            functions_filename = filename.replace('.py', '.functions.py')
            cmd = ' cat ' + functions_filename + \
                  ' /home/ewu/CRLS_APCSP_autograder/var/4.022.test.py > /tmp/4.022.test.py'
            c = delegator.run(cmd)
            if c.err:
                flash("There was a problem creating the python test file")


            # test1 for bad_lossy_compression
            cmd = 'python3 /tmp/4.022.test.py testAutograde.test_bad_lossy_compression_1 2>&1 |grep -i fail |wc -l'
            c = delegator.run(cmd)
            failures = int(c.out)
            test_bad_lossy_compression_1 = {"name": "Testing calling bad_lossy_compression with 'The rain in spain falls mainly in the plain' returns  "
                                                    "'The ain n spin flls ainl in he pain'",
                                            "pass": True,
                                            "pass_message": "Pass. Calling bad_lossy_compression with  'The rain in spain falls mainly in the plain' returns  "
                                            "'The ain n spin flls ainl in he pain'<br>",
                                            "fail_message": "Fail.   Calling bad_lossy_compression with  'The rain in spain falls mainly in the plain' "
                                                            " doesn't return  'The ain n spin flls ainl in he pain'",
            }
            if failures > 0:
                test_bad_lossy_compression_1['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_bad_lossy_compression_1)


            # test2 for bad_lossy_compression
            cmd = 'python3 /tmp/4.022.test.py testAutograde.test_bad_lossy_compression_2 2>&1 |grep -i fail |wc -l'
            c = delegator.run(cmd)
            failures = int(c.out)
            test_bad_lossy_compression_2 =  {"name": "Testing calling bad_lossy_compression with 'I am sick and tired of these darned snakes on this darned plane' returns 'I a sik ad tredof hes danedsnaes n tis arnd pane'",
                                     "pass": True,
                                     "pass_message": "Pass. Calling bad_lossy_compression with 'I am sick and tired of these darned snakes on this darned plane' r\
eturns 'I a sik ad tredof hes danedsnaes n tis arnd pane'",
                                     "fail_message": "Fail.  Calling bad_lossy_compression with 'I am sick and tired of these darned snakes on this darned plane' doesn't  return 'I a sik ad tredof hes danedsnaes n tis arnd pane'"
                                     " You should test your bad_lossy_compression functionto see what it returns <br>"
                                     " If you think it is correct, check your capitalization",
            }
            if failures > 0:
                test_bad_lossy_compression_2['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_bad_lossy_compression_2)


            # test3 for bad_lossy_compression
            cmd = 'python3 /tmp/4.022.test.py testAutograde.test_bad_lossy_compression_3 2>&1 |grep -i fail |wc -l'
            c = delegator.run(cmd)
            failures = int(c.out)
            test_bad_lossy_compression_3 =  {"name": "Testing calling bad_lossy_compression with 'Madness?!?!?!?! THIS IS SPARTA!!!!' returns 'Madess!?!!?!THI ISSPATA!!!'",
                                     "pass": True,
                                     "pass_message": "Pass. Calling bad_lossy_compression with  'Madness?!?!?!?! THIS IS SPARTA!!!!' returns 'Madess!?!!?!THI ISSPA\
TA!!!'",
                                     "fail_message": "Fail.   Calling bad_lossy_compression with 'Madness?!?!?!?! THIS IS SPARTA!!!!' does not return 'Madess!?!!?!THI ISSPATA!!!'"
                                                            " You should test your bad_lossy_compression to see what it returns <br>"
                                     " If you think it is correct, check your capitalization",

            }
            if failures > 0:
                test_bad_lossy_compression_3['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_bad_lossy_compression_3)

            # Find number of PEP8 errors
            cmd = '/home/ewu/CRLS_APCSP_autograder/venv1/bin/pycodestyle --ignore=E305,E226 --max-line-length=120 ' + filename + ' | wc -l  '
            c = delegator.run(cmd)
            side_errors = int(c.out)
            test_pep8 = {"name": "Testing for PEP8 warnings and errors (7 points)",
                         "pass": True,
                         "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                         "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                                                                          "This translates to -" + str(
                             side_errors) + " point(s) deduction.<br>"
                         }
            if side_errors != 0:
                test_pep8['pass'] = False
            score_info['score'] += max(0, int(7) - side_errors)
            tests.append(test_pep8)


            # Check for help comment
            cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
            c = delegator.run(cmd)
            help_comments = int(c.out)
            test_help = {"name": "Testing that you got a help and documented it as a comment (2.5 points)",
                         "pass": True,
                         "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                                         "Be sure your comment is meaningful, otherwise this can be "
                                         "overturned on review.",
                         "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                                         " how somebody helped you with your code.  <br>"
                                         "If you didn't have any problems, then ask somebody to check that your code"
                                         " gives correct outputs, given an input.<br>"
                                         "This translates to -2.5 points deduction.<br>",
                         }
            if help_comments == 0:
                test_help['pass'] = False
            else:
                score_info['score'] += 2.5
            tests.append(test_help)

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)

        else:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)

    
@app.route('/feedback_4025')
def feedback_4025():
    import re
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 64, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2019', filename)
    find_lab = re.search('4.025', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2019_luismartinez_4.025.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2019_luismartinez_4.025.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)
            
        
        # extract functions and create python test file
        extract_functions(filename)
        functions_filename = filename.replace('.py', '.functions.py')
        cmd = ' cat ' + functions_filename + \
              ' /home/ewu/CRLS_APCSP_autograder/var/4.025.test.py > /tmp/4.025.test.py'
        c = delegator.run(cmd)
        if c.err:
            flash("There was a problem creating the python test file")


        # test1 for serena game
        cmd = 'python3 /tmp/4.025.test.py testAutograde.test_serena_1 2>&1 |grep -i fail |wc -l'
        c = delegator.run(cmd)
        failures = int(c.out)
        test_serena_1 = {"name": "Checking the game function. (10 points)",
                         "pass": True,
                         "pass_message": "Pass. Actual win percentages over 1000 tests match the predicted win percentages. ",
                         "fail_message": "Fail.  Actual win percentages over 1000 tests do NOT match the predicted win percentages.<br> "
                         " Check out your code and try again.",
        }
        if failures > 0:
            test_serena_1['pass'] = False
        else:
            score_info['score'] += 10
        tests.append(test_serena_1)
            
        # test2 for serena play_tournament prints tournmaent
        cmd = 'python3 /tmp/4.025.test.py testAutograde.test_serena_2 2>&1 |grep -i fail |wc -l'
        c = delegator.run(cmd)
        failures = int(c.out)
        test_serena_2 =  {"name": "Testing play_tournament function.  If I input 'Wimbledon', it should print 'Wimbledon' somewhere. (2.5 points)",
                          "pass": True,
                          "pass_message": "Pass.  If I input 'Wimbledon', it should print 'Wimbledon' somewhere."
                          "Note, this 'pass' is subject to manual review.",
                          "fail_message": "Fail.  If I input 'Wimbledon', it should print 'Wimbledon' somewhere.<br>"
                          "Please check the play_tournament function prints.<br>",
        }
        if failures > 0:
            test_serena_2['pass'] = False
        else:
            score_info['score'] += 2.5
        tests.append(test_serena_2)

        # test3 for serena play tournament prints win
        cmd = 'python3 /tmp/4.025.test.py testAutograde.test_serena_3 2>&1 |grep -i fail |wc -l'
        c = delegator.run(cmd)
        failures = int(c.out)
        test_serena_3 =  {"name": "Testing play_tournament function.  If I input a high enough winning percentage,  "
                          "it should print 'Win' somewhere (5 points)",
                          "pass": True,
                          "pass_message": "Pass.  If I input a high enough winning percentage, "
                          "it should print 'Win' somewhere.<br>"
                          "Note, this 'pass' is subject to manual review.",
                          "fail_message": "Fail.  If I input a high enough winning percentage, "
                          "it should print 'Win' somewhere<br>"
                          "Please check the play_tournament function prints.<br>",
        }
        if failures > 0:
            test_serena_3['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_serena_3)

        # Test that play_tournamnet has a loop
        test_play_tournament_loop =  {"name": "Testing play_tournament function.  Should have a loop somewhere. (2.5 points)",
                                      "pass": True,
                                      "pass_message": "Pass. play_tournament function has a loop somewhere. "
                                      "Note, this 'pass' is subject to manual review.",
                                      "fail_message": "Fail.   play_tournament function does not have loop somewhere."
                                      "It needs a loop to play multiple games in case of win",
        }
        play_tournament = extract_single_function(filename, 'play_tournament')
        match = re.search('(for|while)', play_tournament)
        if match:
            score_info['score'] += 2.5
        else:
            test_play_tournament_loop['pass'] = False            
        tests.append(test_play_tournament_loop)

        # test4 for serena data_analysis
        cmd = 'python3 /tmp/4.025.test.py testAutograde.test_serena_4 2>&1 |grep -i fail |wc -l'
        c = delegator.run(cmd)
        failures = int(c.out)
        test_serena_4 =  {"name": "Testing data_analysis function.(5 points) ",
                          "pass": True,
                          "pass_message": "Pass.  data_analysis prints correct numbers given an input. ",
                          "fail_message": "Fail.  data_analysis prints in correct numbers given an input.<br>"
                          "Input was list [25, 50, 75], and num_simulations = 100<br>"
                          "Please check the data_analysis function prints correct values.<br>",
        }
        if failures > 0:
            test_serena_4['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_serena_4)

        
        # full run, percentage is 1.0
        filename_output = filename + '.out'
        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/4.025-1.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running Serena Williams program')
        cmd = "grep '%' " + filename_output + ' | grep -i Wimbledon  '
        c = delegator.run(cmd)
        line = c.out
        test_win_all = {"name": "Testing that Wimbledon win % is correct, given win% of 1.0 (10 points)",
                        "pass": True,
                        "pass_message": "Pass!  Wimbledon win % is correct, givyen win% of 1.0.",
                        "fail_message": "Fail.   Wimbledon win % is NOT correct, given win% of 1.0.<br>"
                        "Looking for the word 'Wimbledon' and a '%'.  Looks for the percent of times times she wins.<br>"
                        "check your run to verify that the output is correct and she wins the correct % of times, <br>"
                        "given a win % of 1.0.  Assumes the characters '%' and 'Wimbledon' do not show up anywhere else in output."
                        "<br> ",
        }
        match = re.search('([.0-9]*)%', line)
        if match:
            percent = float(match.group(1))       
            if percent > 101.0 or percent < 99.0: 
                test_win_all['pass'] = False            
            else:
                score_info['score'] += 10
        else:
            test_win_all['pass'] = False            
        tests.append(test_win_all)

        # full run, percentage is .75
        filename_output = filename + '.out2'
        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/4.025-2.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running Serena Williams program' + cmd)
        cmd = "grep '%' " + filename_output + ' | grep -i Wimbledon  '
        c = delegator.run(cmd)
        line = c.out
        test_win_some = {"name": "Testing that Wimbledon win % is correct, given win% of 0.75 (10 points)",
                         "pass": True,
                         "pass_message": "Pass!  Wimbledon win % is correct, given win% of 0.75.",
                         "fail_message": "Fail.   Wimbledon win % is NOT correct, given win% of 0.75.<br>"
                         "Looking for the word 'Wimbledon' and a '%'.  Looks for the percent of times times she wins.<br>"
                         "check your run to verify that the output is correct and she wins the correct % of times, <br>"
                         "given a win % of 1.0.  Assumes the characters '%' and 'Wimbledon' do not show up anywhere else in output."
                         "<br> ",
        }
        match = re.search('([.0-9]*)%', line)
        if match:
            percent = float(match.group(1))
            if percent > 14.5 or percent < 12.5: 
                test_win_some['pass'] = False            
            else:
                score_info['score'] += 10
        else:
            test_win_some['pass'] = False            
        tests.append(test_win_some)

        # Find number of PEP8 errors
        cmd = '/home/ewu/CRLS_APCSP_autograder/venv1/bin/pycodestyle --ignore=E305,E226,W504 --max-line-length=120 ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        side_errors = int(c.out)
        test_pep8 = {"name": "Testing for PEP8 warnings and errors (14 points)",
                     "pass": True,
                     "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                     "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                     "This translates to -" + str(
                             side_errors) + " point(s) deduction.<br>"
        }
        if side_errors != 0:
            test_pep8['pass'] = False
        score_info['score'] += max(0, int(14) - side_errors)
        tests.append(test_pep8)
            
            
        # Check for help comment
        cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
        c = delegator.run(cmd)
        help_comments = int(c.out)
        test_help = {"name": "Testing that you got a help and documented it as a comment (5 points)",
                     "pass": True,
                     "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                     "Be sure your comment is meaningful, otherwise this can be "
                     "overturned on review.",
                     "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                     " how somebody helped you with your code.  <br>"
                     "If you didn't have any problems, then ask somebody to check that your code"
                     " gives correct outputs, given an input.<br>"
                     "This translates to -5.0 points deduction.<br>",
        }
        if help_comments == 0:
            test_help['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_help)
        
        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)    
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)

@app.route('/feedback_6_011')
def feedback_6011():
    import re
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 69, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2019', filename)
    find_lab = re.search('6.011', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2019_luismartinez_6.011.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2019_luismartinez_6.011.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)
            
        # Test for dictionary with 3+ items
        with open(filename, 'r', encoding='utf8') as myfile:
            filename_data = myfile.read()
            
        search_object = re.search(r"{ .+ : .+ , .+ : .+ , .+ : .+ }", filename_data, re.X | re.M | re.S)
        test_dictionary = {"name": "Testing that there is a dictionary with 3+ key/value pairs(10 points)",
                           "pass": True,
                           "pass_message": "Pass! "
                                           "Submitted file looks like it has a dictionary with 3+ key/value pairs. ",
                           "fail_message": "Fail. Submitted file does not look like it has a dictionary with 3+ "
                                           "key/value pairs. ",
        }
        
        if not search_object:
            test_dictionary['pass'] = False
        else:
            score_info['score'] += 10
        tests.append(test_dictionary)
        

        # Check for function bob_kraft_translator
        search_object = re.search(r"^def \s bob_kraft_translator\(.+ , .+ \)", filename_data, re.X| re.M | re.S)
        test_bob_kraft_translator = {"name": "Testing that bob_kraft_translator function exists with two input arguments (5 points)",
                                     "pass": True,
                                     "pass_message": "Pass.  bob_kraft_translator function exists with two input arguments (5 points)",
                                     "fail_message": "Fail.  bob_kraft_translator function does exist with two input arguments (5 points)",
        }
        if not search_object:
            test_bob_kraft_translator['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_bob_kraft_translator)

        
        # extract functions and create python test file
        extract_functions(filename)
        functions_filename = filename.replace('.py', '.functions.py')
        cmd = ' cat ' + functions_filename + \
              ' /home/ewu/CRLS_APCSP_autograder/var/6.011.test.py > /tmp/6.011.test.py'
        c = delegator.run(cmd)
        if c.err:
            flash("There was a problem creating the python test file")


        # test1 for bob
        cmd = 'python3 /tmp/6.011.test.py testAutograde.test_bob_1 2>&1 |grep -i fail |wc -l'
        c = delegator.run(cmd)
        failures = int(c.out)
        test_bob_1 = {"name": "Checking bob_kraft_translator 1 (10 points)",
                      "pass": True,
                      "pass_message": "Pass. Sent in dictionary  {'wth': 'What the heck'},"
                                      " asked for wth, got correct answer.  ",
                      "fail_message": "Fail.   Sent in dictionary  {'wth': 'What the heck'}, "
                                      "asked for wth, didn't get correct <br> "
                      " Check out your code and try again.",
        }
        if failures > 0:
            test_bob_1['pass'] = False
        else:
            score_info['score'] += 10
        tests.append(test_bob_1)
            
        # test2 for bob play_tournament prints tournmaent
        cmd = 'python3 /tmp/6.011.test.py testAutograde.test_bob_2 2>&1 |grep -i fail |wc -l'
        c = delegator.run(cmd)
        failures = int(c.out)
        test_bob_2 =  {"name": "Testing bob_kraft_translator 2.  Sending in bob_dict = {'wth': 'What the heck',"
                       "'aymm': 'Ay yo my man',}, looking for aymm, should receive 'Ay yo my man'",
                       "pass": True,
                       "pass_message": "Pass.  Sent in bob_dict = {'wth', 'What the heck',"
                       "'aymm': 'Ay yo my man',}, looked for aymm, received 'Ay yo my man'",
                       "fail_message": "Fail.    Sent in bob_dict = {'wth', 'What the heck',"
                       "'aymm': 'Ay yo my man',}, looked for aymm, received 'Ay yo my man' but did not receive it"
                       "Please check code and try again.<br>",
        }
        if failures > 0:
            test_bob_2['pass'] = False
        else:
            score_info['score'] += 10
        tests.append(test_bob_2)

        # test3 for bob play tournament prints win
        cmd = 'python3 /tmp/6.011.test.py testAutograde.test_bob_3 2>&1 |grep -i fail |wc -l'
        c = delegator.run(cmd)
        failures = int(c.out)
        test_bob_3 =  {"name":  "Testing bob_kraft_translator 3.  Sending in bob_dict = {'wth': 'What the heck',"
                       "'aymm': 'Ay yo my man',}, looking for asdfasdf, should receive something with"
                                "'do not know' (10 points)",
                       "pass": True,
                       "pass_message": "Pass.  Sent in bob_dict = {'wth': 'What the heck',"
                                       "'aymm': 'Ay yo my man',}, looked for asdfasdf, received something with"
                                       " 'do not know' (10 points)",
                       "fail_message": "Fail.  Sent in bob_dict = {'wth': 'What the heck',"
                                       "'aymm': 'Ay yo my man',}, looked for asdfasdf, received something without"
                                       " 'do not know' (10 points)<br>"
                                       "Please check your code",
        }
        if failures > 0:
            test_bob_3['pass'] = False
        else:
            score_info['score'] += 10
        tests.append(test_bob_3)



        # Check for 3 ifs on different lines
        cmd = 'grep "if" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        ifs = int(c.out)
        test_ifs = {"name": "Testing that program is efficient. (5 points)",
                    "pass": True,
                    "pass_message": "Pass.  Testing that program is efficient.  <br>",
                    "fail_message": "Fail.  Testing that program is efficient<br>"

                                    "Are you using an if/if/if/if or if/elif/elif/elif? <br>"
                                    "Check HW11.  Using if/elif/elif can get really big code with a lot of conditions <br>",
                    }
        if ifs >= 3:
            test_ifs['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_ifs)

        # Find number of PEP8 errors
        cmd = \
            '/home/ewu/CRLS_APCSP_autograder/venv1/bin/pycodestyle --ignore=E305,E226,W504,W293 --max-line-length=120 '\
            + filename + ' | wc -l  '
        c = delegator.run(cmd)
        side_errors = int(c.out)
        test_pep8 = {"name": "Testing for PEP8 warnings and errors (14 points)",
                     "pass": True,
                     "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                     "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                     "This translates to -" + str(
                             side_errors) + " point(s) deduction.<br>"
        }
        if side_errors != 0:
            test_pep8['pass'] = False
        score_info['score'] += max(0, int(14) - side_errors)
        tests.append(test_pep8)
            
            
        # Check for help comment
        cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
        c = delegator.run(cmd)
        help_comments = int(c.out)
        test_help = {"name": "Testing that you got a help and documented it as a comment (5 points)",
                     "pass": True,
                     "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                     "Be sure your comment is meaningful, otherwise this can be "
                     "overturned on review.",
                     "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                     " how somebody helped you with your code.  <br>"
                     "If you didn't have any problems, then ask somebody to check that your code"
                     " gives correct outputs, given an input.<br>"
                     "This translates to -5.0 points deduction.<br>",
        }
        if help_comments == 0:
            test_help['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_help)
        
        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)    
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)

@app.route('/feedback_6_021')
def feedback_6021():
    import re
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 69, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2019', filename)
    find_lab = re.search('6.021', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2019_luismartinez_6.021.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2019_luismartinez_6.021.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)

        with open(filename, 'r', encoding='utf8') as myfile:
            filename_data = myfile.read()
        
        # Check for function martinez_dictionary
        search_object = re.search(r"^def \s martinez_dictionary\(.+ , .+ \)", filename_data, re.X| re.M | re.S)
        test_martinez_dictionary = {"name": "Testing that martinez_dictionary function exists with two input arguments (5 points)",
                                    "pass": True,
                                    "pass_message": "Pass.  martinez_dictionary function exists with two input arguments (5 points)",
                                    "fail_message": "Fail.  martinez_dictionary function does exist with two input arguments (5 points)",
        }
        if not search_object:
            test_martinez_dictionary['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_martinez_dictionary)

        # Check that function martinez_dictionary is called 
        test_martinez_dictionary_run = {"name": "Testing that martinez_dictionary function is called at least once (5 points)",
                                        "pass": False,
                                        "pass_message": "Pass.  martinez_dictionary function is called.  <br>",
                                        "fail_message": "Fail.  martinez_dictionary function isn't called in the code. <br>"
        }
        with open(filename) as infile:
            for line in infile.readlines():
                found = re.search("(?<!def\s)martinez_dictionary" , line,  re.X | re.M | re.S)
                if found:
                    test_martinez_dictionary_run['pass'] = True
        infile.close()
        if test_martinez_dictionary_run['pass']:
            score_info['score'] += 5
        tests.append(test_martinez_dictionary_run)

        # extract functions and create python test file
        extract_functions(filename)
        functions_filename = filename.replace('.py', '.functions.py')
        cmd = ' cat ' + functions_filename + \
              ' /home/ewu/CRLS_APCSP_autograder/var/6.021.test.py > /tmp/6.021.test.py'
        c = delegator.run(cmd)
        if c.err:
            flash("There was a problem creating the python test file")

            
        # extract martinez_dictionary functions and look for dictionary
        test_martinez_dictionary_dictionary = {"name": "Testing that martinez_dictionary function has a blank dictionary to initialize(5 points)",
                                               "pass": True,
                                               "pass_message": "Pass.  martinez_dictionary function has a blank dictionary to initialize.  <br>",
                                               "fail_message": "Fail.  martinez_dictionary function does not have a blank dictionary in it to initialize. <br>"
        }
        martinez_function = extract_single_function(filename, 'martinez_dictionary')
        search_object = re.search(r"{  }", martinez_function, re.X| re.M | re.S)
        if search_object:
            score_info['score'] += 5
        else:
            test_martinez_dictionary_dictionary['pass'] = False
        tests.append(test_martinez_dictionary_dictionary)


        # test1 for martinez
        cmd = 'python3 /tmp/6.021.test.py testAutograde.test_martinez_1 2>&1 |grep -i fail |wc -l'
        c = delegator.run(cmd)
        failures = int(c.out)
        test_martinez_1 = {"name": "Checking martinez_dictionary 1 (10 points)",
                           "pass": True,
                           "pass_message": "Pass. Sent in list ['Goku', 'Goku', 'Goku', 'Goku', 'Goku'], got back {'Goku':500}",
                           "fail_message": "Fail. Sent in list ['Goku', 'Goku', 'Goku', 'Goku', 'Goku'], didn't get back {'Goku':500}"
                                           " Check out your code and try again.",
        }
        if failures > 0:
            test_martinez_1['pass'] = False
        else:
            score_info['score'] += 10
        tests.append(test_martinez_1)
            
        # test2 for martinez play_tournament prints tournmaent
        cmd = 'python3 /tmp/6.021.test.py testAutograde.test_martinez_2 2>&1 |grep -i fail |wc -l'
        c = delegator.run(cmd)
        failures = int(c.out)
        test_martinez_2 = { "name": "Checking martinez_dictionary 2 (10 points)",
                            "pass": True,
                            "pass_message": "Pass. Sent in list ['Goku', 'Goku', 'Trunks', 'Vegeta', 'Vegeta', 'Krillan', 'Goku'],"
                                            " got back  {'Goku': 300, 'Trunks': 100, 'Vegeta':200, 'Krillan':100}",
                            "fail_message": "Fail. Sent in list ['Goku', 'Goku', 'Trunks', 'Vegeta', 'Vegeta', 'Krillan', 'Goku'],"
                            " didn't get back  {'Goku': 300, 'Trunks': 100, 'Vegeta':200, 'Krillan':100} <br>"
                            "Please check your code and try again.",

        }
        if failures > 0:
            test_martinez_2['pass'] = False
        else:
            score_info['score'] += 10
        tests.append(test_martinez_2)

        # Check for function data_generator
        search_object = re.search(r"^def \s data_generator\(.+ , .+ \)", filename_data, re.X| re.M | re.S)
        test_data_generator = {"name": "Testing that data_generator function exists with two input arguments (5 points)",
                                     "pass": True,
                                     "pass_message": "Pass.  data_generator function exists with two input arguments (5 points)",
                                     "fail_message": "Fail.  data_generator function does exist with two input arguments (5 points)",
        }
        if not search_object:
            test_data_generator['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_data_generator)

        
        # test3 for martinez, checks that 2 lists are different
        cmd = 'python3 /tmp/6.021.test.py testAutograde.test_martinez_3 2>&1 |grep -i fail |wc -l'
        c = delegator.run(cmd)
        failures = int(c.out)
        test_martinez_3 = { "name": "Checking data_generator, send in ['Brolly', 'Goku', 'Gohan', 'Piccolo', 'Vegeta' ] twice, "
                                    " The two lists should be different (test of random) (5 points)",
                            "pass": True,
                            "pass_message": "Pass. Sent in ['Brolly', 'Goku', 'Gohan', 'Piccolo', 'Vegeta' ] twice, "
                                            " The two lists are different (test of random)",
                            "fail_message": "Fail. Sent in list ['Goku', 'Goku', 'Trunks', 'Vegeta', 'Vegeta', 'Krillan', 'Goku'],"
                                            " they are not different. <br>"
                                            "Please check your code and try again.",

        }
        if failures > 0:
            test_martinez_3['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_martinez_3)

        # test4 for martinez, checks that list generated has everything that's supposed to be there
        cmd = 'python3 /tmp/6.021.test.py testAutograde.test_martinez_4 2>&1 |grep -i fail |wc -l'
        c = delegator.run(cmd)
        failures = int(c.out)
        test_martinez_4 = { "name": "Checking data_generator, send in ['Brolly', 'Goku', 'Gohan', 'Piccolo', 'Vegeta' ]  "
                                    " n=100, they should all show up once at least) (5 points)",
                            "pass": True,
                            "pass_message": "Pass. Sent in ['Brolly', 'Goku', 'Gohan', 'Piccolo', 'Vegeta' ]"
                                            " n=100, they all show up once at least)",
                            "fail_message": "Fail. Sent in list ['Brolly', 'Goku', 'Gohan', 'Piccolo', 'Vegeta' ]"
                                            " n=100, they do not all show up once at least) "
                                            "Please check your code and try again.",

        }
        if failures > 0:
            test_martinez_4['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_martinez_4)

        # Find number of PEP8 errors
        cmd = \
            '/home/ewu/CRLS_APCSP_autograder/venv1/bin/pycodestyle --ignore=E305,E226,W504,W293 --max-line-length=120 '\
            + filename + ' | wc -l  '
        c = delegator.run(cmd)
        side_errors = int(c.out)
        test_pep8 = {"name": "Testing for PEP8 warnings and errors (14 points)",
                     "pass": True,
                     "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                     "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                     "This translates to -" + str(
                             side_errors) + " point(s) deduction.<br>"
        }
        if side_errors != 0:
            test_pep8['pass'] = False
        score_info['score'] += max(0, int(14) - side_errors)
        tests.append(test_pep8)
            
            
        # Check for help comment
        cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
        c = delegator.run(cmd)
        help_comments = int(c.out)
        test_help = {"name": "Testing that you got a help and documented it as a comment (5 points)",
                     "pass": True,
                     "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                     "Be sure your comment is meaningful, otherwise this can be "
                     "overturned on review.",
                     "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                     " how somebody helped you with your code.  <br>"
                     "If you didn't have any problems, then ask somebody to check that your code"
                     " gives correct outputs, given an input.<br>"
                     "This translates to -5.0 points deduction.<br>",
        }
        if help_comments == 0:
            test_help['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_help)
        
        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)    
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_6_031')
def feedback_6031():
    import re
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 69, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2019', filename)
    find_lab = re.search('6.031', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2019_luismartinez_6.031.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2019_luismartinez_6.031.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)

        with open(filename, 'r', encoding='utf8') as myfile:
            filename_data = myfile.read()
            
        search_object = re.search(r"{ \s* }", filename_data, re.X | re.M | re.S)
        test_dictionary = {"name": "Testing that there is an empty dictionary(5 points)",
                           "pass": True,
                           "pass_message": "Pass! "
                                           "Submitted file looks like it has an empty dictionary ",
                           "fail_message": "Fail. Submitted file does not look like it has an empty dictionary",
        }
        if not search_object:
            test_dictionary['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_dictionary)

        # Check for function add with 2 inputs
        search_object = re.search(r"^def \s add\(.+ , .+ \)", filename_data, re.X| re.M | re.S)
        test_add = {"name": "Testing that add function exists with two input arguments (5 points)",
                                    "pass": True,
                                    "pass_message": "Pass.  add function exists with two input arguments (5 points)",
                                    "fail_message": "Fail.  add function does exist with two input arguments (5 points)",
        }
        if not search_object:
            test_add['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_add)

        # extract functions and create python test file
        extract_functions(filename)
        functions_filename = filename.replace('.py', '.functions.py')
        cmd = ' cat ' + functions_filename + \
              ' /home/ewu/CRLS_APCSP_autograder/var/6.031.test.py > /tmp/6.031.test.py'
        c = delegator.run(cmd)
        if c.err:
            flash("There was a problem creating the python test file")

        
        # test1 for mcglathery
        cmd = 'python3 /tmp/6.031.test.py testAutograde.test_mcglathery_1 2>&1 |grep -i fail |wc -l'
        c = delegator.run(cmd)
        failures = int(c.out)
        test_mcglathery_1 = {"name": "Checking mcglathery_dictionary 1.  Adding 'fire' and 'charmander' , expect output {'fire':'charmander'}(5 points)",
                             "pass": True,
                             "pass_message": "Pass.  Added 'fire' and 'charmander' , got output {['fire':'charmander']}",
                             "fail_message": "Fail.  Added 'fire' and 'charmander' , didn't get output {['fire':'charmander']}"
                                             " Check out your code and try again.",
        }
        if failures > 0:
            test_mcglathery_1['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_mcglathery_1)

        # test2 for mcglathery
        cmd = 'python3 /tmp/6.031.test.py testAutograde.test_mcglathery_2 2>&1 |grep -i fail |wc -l'
        c = delegator.run(cmd)
        failures = int(c.out)
        test_mcglathery_2 = {"name": "Checking mcglathery_dictionary 2.  Adding 'ice' and 'iceperson2' to {'fire':['charmander'], 'ice':['iceperson']}."
                                     "expect output {['fire':['charmander'], 'ice':['iceperson','iceperson2']}(10 points)",
                             "pass": True,
                             "pass_message": "Pass.  Adding 'ice' and 'iceperson2' to {'fire':['charmander'], 'ice':['iceperson'].<br>"
                                     "got output {['fire':['charmander'], 'ice':['iceperson','iceperson2']}(10 points)",
                             "fail_message": "Fail.  Adding 'ice' and 'iceperson' to dictionary already with 'fire' and 'charmander'.<br>"
                                             "didn't get output {['fire':'charmander', 'ice':['iceperson', 'iceperson2']}(10 points)"
                                             "Check out your code and try again.",
        }
        if failures > 0:
            test_mcglathery_2['pass'] = False
        else:
            score_info['score'] += 10
        tests.append(test_mcglathery_2)
                    
        # Check for function get with 2 inputs
        search_object = re.search(r"^def \s get\(.+ , .+ \)", filename_data, re.X| re.M | re.S)
        test_get = {"name": "Testing that get function exists with two input arguments (5 points)",
                                    "pass": True,
                                    "pass_message": "Pass.  get function exists with two input arguments (5 points)",
                                    "fail_message": "Fail.  get function does exist with two input arguments (5 points)",
        }
        if not search_object:
            test_get['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_get)

        # test3 for mcglathery
        cmd = 'python3 /tmp/6.031.test.py testAutograde.test_mcglathery_3 2>&1 |grep -i fail |wc -l'
        c = delegator.run(cmd)
        failures = int(c.out)
        test_mcglathery_3 = { "name": "Checking mcglathery_dictionary 3.  testing get function with input  {'fire':['charmander']} expecting something with 'fire' (5 points)",
                              "pass": True,
                              "pass_message": "Pass. Sent in dictionary, {'fire':['charmander']}, got something back with 'fire' in it. ",
                              "fail_message": "Fail. Sent in dictionary  {'fire':['charmander']}, didn't get something back with 'fire' in it. " 
                              "Please check your code and try again.",
                              
        }
        if failures > 0:
            test_mcglathery_3['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_mcglathery_3)

        # test4 for mcglathery
        cmd = 'python3 /tmp/6.031.test.py testAutograde.test_mcglathery_4 2>&1 |grep -i fail |wc -l'
        c = delegator.run(cmd)
        failures = int(c.out)
        test_mcglathery_4 = { "name": "Checking mcglathery_dictionary 4.  testing get function with input  {'fire':['charmander','fireperson'} expecting something"
                                      "with 'fire' and 'fireperson (10 points)",
                              "pass": True,
                              "pass_message": "Pass. Sent in dictionary, {'fire':['charmander','fireperson']}, got something back with 'fire' and 'fireperson' in it. ",
                              "fail_message": "Fail. Sent in dictionary  {'fire':['charmander','fireperson']}, didn't get something back with 'fire' and 'fireperson' in it. " 
                              "Please check your code and try again.",
                              
        }
        if failures > 0:
            test_mcglathery_4['pass'] = False
        else:
            score_info['score'] += 10
        tests.append(test_mcglathery_4)

        # # Check for function data_generator
        # search_object = re.search(r"^def \s data_generator\(.+ , .+ \)", filename_data, re.X| re.M | re.S)
        # test_data_generator = {"name": "Testing that data_generator function exists with two input arguments (5 points)",
        #                              "pass": True,
        #                              "pass_message": "Pass.  data_generator function exists with two input arguments (5 points)",
        #                              "fail_message": "Fail.  data_generator function does exist with two input arguments (5 points)",
        # }
        # if not search_object:
        #     test_data_generator['pass'] = False
        # else:
        #     score_info['score'] += 5
        # tests.append(test_data_generator)

        
        # # test3 for mcglathery, checks that 2 lists are different
        # cmd = 'python3 /tmp/6.031.test.py testAutograde.test_mcglathery_3 2>&1 |grep -i fail |wc -l'
        # c = delegator.run(cmd)
        # failures = int(c.out)
        # test_mcglathery_3 = { "name": "Checking data_generator, send in ['Brolly', 'Goku', 'Gohan', 'Piccolo', 'Vegeta' ] twice, "
        #                             " The two lists should be different (test of random) (5 points)",
        #                     "pass": True,
        #                     "pass_message": "Pass. Sent in ['Brolly', 'Goku', 'Gohan', 'Piccolo', 'Vegeta' ] twice, "
        #                                     " The two lists are different (test of random)",
        #                     "fail_message": "Fail. Sent in list ['Goku', 'Goku', 'Trunks', 'Vegeta', 'Vegeta', 'Krillan', 'Goku'],"
        #                                     " they are not different. <br>"
        #                                     "Please check your code and try again.",

        # }
        # if failures > 0:
        #     test_mcglathery_3['pass'] = False
        # else:
        #     score_info['score'] += 5
        # tests.append(test_mcglathery_3)

        # # test4 for mcglathery, checks that list generated has everything that's supposed to be there
        # cmd = 'python3 /tmp/6.031.test.py testAutograde.test_mcglathery_4 2>&1 |grep -i fail |wc -l'
        # c = delegator.run(cmd)
        # failures = int(c.out)
        # test_mcglathery_4 = { "name": "Checking data_generator, send in ['Brolly', 'Goku', 'Gohan', 'Piccolo', 'Vegeta' ]  "
        #                             " n=100, they should all show up once at least) (5 points)",
        #                     "pass": True,
        #                     "pass_message": "Pass. Sent in ['Brolly', 'Goku', 'Gohan', 'Piccolo', 'Vegeta' ]"
        #                                     " n=100, they all show up once at least)",
        #                     "fail_message": "Fail. Sent in list ['Brolly', 'Goku', 'Gohan', 'Piccolo', 'Vegeta' ]"
        #                                     " n=100, they do not all show up once at least) "
        #                                     "Please check your code and try again.",

        # }
        # if failures > 0:
        #     test_martinez_4['pass'] = False
        # else:
        #     score_info['score'] += 5
        # tests.append(test_martinez_4)

        # Check for a loop of some sort (for or while)
        cmd = 'grep -E "for|while"  ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        loop = int(c.out)
        test_loop = {"name": "Testing that program has a loop. (5 points)",
                     "pass": True,
                     "pass_message": "Pass.  Testing that program has a loop.  <br>",
                     "fail_message": "Fail.  Testing that program has a loop (assume a while or for means you have a loop) <br>"
                     "The program needs a while or a for. <br>"
                     "Fix code and resubmit. <br>",
        }
        if loop == 0:
            test_loop['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_loop)

        # Find number of PEP8 errors
        cmd = \
            '/home/ewu/CRLS_APCSP_autograder/venv1/bin/pycodestyle --ignore=E305,E226,W504,W293 --max-line-length=120 '\
            + filename + ' | wc -l  '
        c = delegator.run(cmd)
        side_errors = int(c.out)
        test_pep8 = {"name": "Testing for PEP8 warnings and errors (14 points)",
                     "pass": True,
                     "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                     "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                     "This translates to -" + str(
                             side_errors) + " point(s) deduction.<br>"
        }
        if side_errors != 0:
            test_pep8['pass'] = False
        score_info['score'] += max(0, int(14) - side_errors)
        tests.append(test_pep8)
            
            
        # Check for help comment
        cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
        c = delegator.run(cmd)
        help_comments = int(c.out)
        test_help = {"name": "Testing that you got a help and documented it as a comment (5 points)",
                     "pass": True,
                     "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                     "Be sure your comment is meaningful, otherwise this can be "
                     "overturned on review.",
                     "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                     " how somebody helped you with your code.  <br>"
                     "If you didn't have any problems, then ask somebody to check that your code"
                     " gives correct outputs, given an input.<br>"
                     "This translates to -5.0 points deduction.<br>",
        }
        if help_comments == 0:
            test_help['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_help)
        
        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)    
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)




    


    







    


    




    


    



    



    


    
