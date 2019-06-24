from flask import render_template, url_for, request, redirect, flash
from app import app
from app.forms import UploadForm, UploadScratchForm
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
            if request.form['lab'] in ['1.040', '1.060', '2.020', '2.032a', '2.032b', '2.040', '2.050a', '2.050b',
                                       '3.011', '3.020', '3.026', '4.011', '4.021', '4.022', '4.025', '4.031',
                                       '4.036', '6.011', '6.021', '6.031', '6.041', '7.021', '7.031', '7.034', ]:
                return redirect(url_for('feedback_' + request.form['lab'].replace(".", ""), filename=filename))

    form = UploadForm()
    user = {'username': 'CRLS Scholar!!!'}
    return render_template('index.html', title='Home', user=user, form=form)


@app.route('/scratch', methods=['GET', 'POST'])
def scratch():
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
                  'You have to turn in a Scratch 3 file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash(file.filename + ' uploaded')
            if request.form['lab'] in ['1.3', ]:
                return redirect(url_for('scratch_feedback_' + request.form['lab'].replace(".", ""), filename=filename))

    form = UploadScratchForm()
    user = {'username': 'CRLS Scratch Scholar!!'}
    return render_template('index.html', title='Home', user=user, form=form)


@app.route('/scratch/scratch_feedback_13')
def scratch_feedback_13():
    import json
    from app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help, arrange_blocks

    user = {'username': 'CRLS Scraach Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 34.5, 'manually_scored': 5.5, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = scratch_filename_test(filename, '1.3')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        abc = json.dumps(json_data, indent=4)
        print(abc)
        test_help = find_help(json_data, 5)
        tests.append(test_help)
        score_info['finished_scoring'] = True
        abc = arrange_blocks(json_data)
        for key in abc:
            print("KEY")
            print(key)
            print("VALUE")
            print(abc[key])

        for test in tests:
            if test['pass']:
                score_info['score'] += test['points']
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_1040')
def feedback_1040():

    from app.python_labs.filename_test import filename_test
    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.find_items import find_questions
    from app.python_labs.io_test import io_test
    from app.python_labs.python_1_040 import statement_variables
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 34.5, 'manually_scored': 5.5, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '1.040')
    tests.append(test_filename)

    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # Check that there are 3 input questions
        test_find_three_questions = find_questions(filename_data, 3, 5)
        test_find_three_questions['name'] += " Checking that Genie asks at least 3 questions. <br> " + \
                                             " Autograder will not continue if this test fails. <br>"
        tests.append(test_find_three_questions)
        if not test_find_three_questions['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # io test 1- a b c
            test_io_1 = io_test(filename, r'.+ a1 .+ a2 .+ a3 ', 1, points=5)
            test_io_1['name'] += "Check things are in correct order - wishing for a, b, c " +\
                                 " should print 'your wishes are a, b, and c.' <br>" \
                                 "You must have at least 1 character of some sort between your wishes.<br>"
            tests.append(test_io_1)

            # Check that there are 6 total questions (3 part 1, 3 part 2)
            test_find_six_questions = find_questions(filename_data, 6, 5)
            test_find_six_questions['name'] += " Checking that Genie asks at least 6 questions (you need 3 for" \
                                               " part 1 and 3 for part 2). <br>"
            tests.append(test_find_six_questions)

            # Check that repeated questions put into variables.
            test_input_variable = statement_variables(filename_data, 5)
            tests.append(test_input_variable)

            # io test 2 - a b c, b2, b3, b1
            test_io_2 = io_test(filename, r'.+ a1 .+ a2 .+ a3 .+ b2 .+ b3 .+ b1 ', 1, points=5)
            test_io_2['name'] += "Check things are in correct order - wishing for a, b, c, d, e, f " + \
                                 " should print 'your wishes are a, b, and c' <br>" +\
                                 " and 'your wishes are e, f, and d' <br>" \
                                 "You must have at least 1 character of some sort between your wishes.<br>"
            tests.append(test_io_2)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 7)
            tests.append(test_pep8)
            test_help = helps(filename, 2.5)
            tests.append(test_help)

            score_info['finished_scoring'] = True
            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_1060')
def feedback_1060():

    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.find_items import find_questions, find_string
    from app.python_labs.io_test import io_test_find_all, io_test
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69, 'manually_scored': 11, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '1.060')
    tests.append(test_filename)

    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # Check that there are 5 input questions
        test_find_five_questions = find_questions(filename_data, 5, 5)
        test_find_five_questions['name'] += " Checking for at least 5 questions. <br> " + \
                                            " Autograder will not continue if this test fails. <br>"
        tests.append(test_find_five_questions)
        if not test_find_five_questions['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:

            # Check that inputs are named after part of speech
            test_find_parts_of_speech = find_string(filename_data,
                                                    r'(verb|noun|adjective|adverb|preposition|place) _* [0-9]* \s* = '
                                                    r'\s* input\(',
                                                    5, points=5)
            test_find_parts_of_speech['name'] += "Testing that variables are named after parts of speech. <br>"\
                                                 "If this test fails, rename variables to parts of speech " \
                                                 "per instructions.<br>" \
                                                 "Also note, Python variable name convention is LOWERCASE, so this " \
                                                 "test will flunk variables like 'Noun1' or 'Verb2'<br>"
            tests.append(test_find_parts_of_speech)

            # Check for at least 1 print statement
            test_find_print = find_string(filename_data, r'print \s* \(', 1, points=5)
            test_find_print['name'] += "Testing for at least one print statement. <br>"
            tests.append(test_find_print)

            # Check for less than 3 print statements
            test_find_three_print = find_string(filename_data, r'print \s \(', 3, points=5, minmax='max')
            test_find_three_print['name'] += "Testing for at maximum of three print statements. <br>"
            tests.append(test_find_three_print)

            # answer 5 questions, they should all show up in printout
            test_io_five_inputs = io_test_find_all(filename, [r'a1', r'a2', r'a3', r'b1', r'b2'], 1, points=15)
            test_io_five_inputs['name'] += 'Testing for first 5 things you answered questions to show in output.<br>' \
                                           'For example, if you typed in noun1, verb1, noun2, verb2, and adjective' \
                                           '<br> noun1, verb1, noun2, verb2, and adjective should all appear ' \
                                           'in the printout. <br>'
            tests.append(test_io_five_inputs)

            # Check for 3 punctuations
            test_puncts = io_test(filename, r'(\? | ! | \.) ', 1, points=5, occurrences=3)
            test_puncts['name'] += "Testing for at least 3 punctuations.<br>"
            tests.append(test_puncts)

            # Test second 4 inputs for correct spacing
            test_io_spacing = io_test_find_all(filename, [r'(\^ | \s+ ) a2 (\s+ | \? | \. | , | !)',
                                                          r'(\^ | \s+ ) a3 (\s+ | \? | \. | , | !)',
                                                          r'(\^ | \s+ ) b1 (\s+ | \? | \. | , | !)',
                                                          r'(\^ | \s+ ) b2 (\s+ | \? | \. | , | !)'],
                                               1, points=10)
            test_io_spacing['name'] += 'Testing for spacing.  Things you enter should have spaces or punctuations<br>' \
                                       'after them and spaces before them in the printout. <br>'
            tests.append(test_io_spacing)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 14)
            tests.append(test_pep8)
            test_help = helps(filename, 5)
            tests.append(test_help)

            score_info['finished_scoring'] = True
            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']

            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_2020')
def feedback_2020():

    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.io_test import io_test, io_test_find_all
    from app.python_labs.find_items import find_questions, find_string
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 55, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '2.020')
    tests.append(test_filename)

    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # Check that there is 1 input questions
        test_find_question = find_questions(filename_data, 1, 5)
        test_find_question['name'] += " Checking for at least 1 question. <br> " + \
                                      " Autograder will not continue if this test fails. <br>"
        tests.append(test_find_question)
        if not test_find_question['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # Test for casting of any sort
            test_find_casting = find_string(filename_data, r'( int\( | float\( )', 1, points=5)
            test_find_casting['name'] += 'Checking that there is some casting of any sort to either integer or float.'
            tests.append(test_find_casting)

            # Test for casting of initial value to float.  Will crash with unknown errors later if casted to int.
            test_find_casting_2 = find_string(filename_data, r'float\( ', 1)
            test_find_casting_2['name'] += 'Test your program by manually running it and typing in 55.5 for your ' \
                                           'number. <br> If you  get an error<br>' \
                                           'ValueError: invalid literal for int() with base 10:<br>' \
                                           'This error means you are trying to convert a string that looks like' \
                                           ' a float into an integer.  ' \
                                           '<br> If you really want an integer you have to cast the string' \
                                           ' to a float first. <br> Or else if you are OK with float, cast to float ' \
                                           'instead of integer.<br> '
            tests.append(test_find_casting_2)
            if not test_find_casting_2['pass']:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:
                # Check that input1 is good (input / 2) 99 / 2 = 49.5
                test_io_1 = io_test(filename, '49.5', 1, points=10)
                test_io_1['name'] += "Checks that the number divides by 2 and prints out.  Input 99, " \
                                     "expected 49.5 and 49 in output. <br>"
                tests.append(test_io_1)

                # Check input2 is good (int(input / 2))
                test_io_2 = io_test(filename, '49$', 1, points=10)
                test_io_2['name'] += "Checks that the number divides by 2 and prints out the INTEGER only answer. " \
                                     " Input 99, expected 49 in output. <br>"
                tests.append(test_io_2)

                # Check input2 is good (int(input / 2))
                test_io_3 = io_test_find_all(filename, ['49.75', '49$'], 2, points=6)
                test_io_3['name'] += "Checks that the program works for non-whole inputs. " \
                                     " Input 99.5, expected 49.75 and 49 in output. <br>"
                tests.append(test_io_3)

                # Find number of PEP8 errors and helps
                test_pep8 = pep8(filename, 14)
                tests.append(test_pep8)
                test_help = helps(filename, 5)
                tests.append(test_help)

                score_info['finished_scoring'] = True
                for test in tests:
                    if test['pass']:
                        score_info['score'] += test['points']

                score_info['finished_scoring'] = True
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)


@app.route('/feedback_2032a')
def feedback_2032a():

    from app.python_labs.filename_test import filename_test
    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.find_items import find_if
    from app.python_labs.python_2_03x import python_2_032a
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 26.5, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '2.032a')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # Check for ifs
        test_ifs = find_if(filename_data, 0, 5, minmax='max')
        test_ifs['name'] += 'Testing for ifs.  There should be zero ifs in the code. <br>' \
                            'For example, print(1==1) NOT if (1 == 1): print("True") <br>' \
                            ''
        tests.append(test_ifs)

        if not test_ifs['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:

            debug_statement = 'Program asks for DC/Marvel, age, and power in that order. <br>' \
                              'DC must be capitalized.<br>'
            test_runs = python_2_032a(filename, filename_data, debug_statement=debug_statement)
            tests.append(test_runs)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 7)
            tests.append(test_pep8)
            test_help = helps(filename, 2.5)
            tests.append(test_help)

            score_info['finished_scoring'] = True
            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']

            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_2032b')
def feedback_2032b():

    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_if
    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.python_2_03x import python_2_032b
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 26.5, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '2.032b')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # Check for ifs
        test_ifs = find_if(filename_data, 0, 5, minmax='max')
        test_ifs['name'] += 'Testing for ifs.  There should be zero ifs in the code. <br>' \
                            'For example, print(1==1) NOT if (1 == 1): print("True") <br>' \
                            'If you think this should pass, control-F and search for "if" in your code'
        tests.append(test_ifs)

        # test all 8 cases
        debug_statement = 'Program asks for if you are Yuka Kinoshita, your stomach size, and money in that order <br>'\
                          'If you are failing 2 tests, read example 8 from the presentation.'
        test_runs = python_2_032b(filename, filename_data, debug_statement=debug_statement)
        tests.append(test_runs)

        # Find number of PEP8 errors and helps
        test_pep8 = pep8(filename, 7)
        tests.append(test_pep8)
        test_help = helps(filename, 2.5)
        tests.append(test_help)

        for test in tests:
            if test['pass']:
                score_info['score'] += test['points']

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_2040')
def feedback_2040():

    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.find_items import find_all_strings, find_questions, find_if, find_elif, find_else
    from app.python_labs.python_2_040 import python_2_040
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 61, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '2.040')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # Test for prize variables
        test_prizes = find_all_strings(filename_data, [r'prize1 \s* = \s* (\'|\")[a-zA-Z0-9!-\.\s]+',
                                                       r'prize2 \s* = \s* (\'|\")[a-zA-Z0-9!-\.\s]+',
                                                       r'prize3 \s* = \s* (\'|\")[a-zA-Z0-9!-\.\s]+',
                                                       r'prize4 \s* = \s* (\'|\")[a-zA-Z0-9!-\.\s]+', ], 6)
        test_prizes['name'] += "Testing for 4 variables names prize1, prize2, prize3, prize4 (not prize_1, prize_2..." \
                               " <br>"
        tests.append(test_prizes)
        if not test_prizes['pass']:
            test_prizes['fail_message'] += 'Be sure you have 4 variables called  prize1, prize2, prize3, prize4. <br>' \
                                           'Be sure to set their values to be prizes'
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            test_question = find_questions(filename_data, 1, 6)
            tests.append(test_question)
            if not test_question['pass']:
                test_question['fail_message'] += "You need to ask the user a question about which door to pick. <br>"
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:
                # test if, check for at least 1 if statement
                test_ifs = find_if(filename_data, 1, 6)
                tests.append(test_ifs)

                # test else check for at least 1 else statement
                test_else = find_else(filename_data, 1, 6)
                tests.append(test_else)

                # look for 3 elifs
                test_elif = find_elif(filename_data, 3, 6)
                tests.append(test_elif)

                test_correct_prizes = python_2_040(filename, filename_data)
                if not test_correct_prizes['pass']:
                    test_correct_prizes['fail_message'] += test_correct_prizes['debug']
                tests.append(test_correct_prizes)

                # Find number of PEP8 errors and helps
                test_pep8 = pep8(filename, 14)
                tests.append(test_pep8)
                test_help = helps(filename, 5)
                tests.append(test_help)

                for test in tests:
                    if test['pass']:
                        score_info['score'] += test['points']
                score_info['finished_scoring'] = True
                return render_template('feedback.html', user=user, tests=tests,
                                       filename=filename, score_info=score_info)


@app.route('/feedback_2051a')
def feedback_2051a():

    from app.python_labs.find_items import find_string, find_questions, find_all_strings
    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.python_2_05x import python_2_051a
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 32.5, 'manually_scored': 11, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '2.050a')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # test for a list being created with 4 items
        test_prizes = find_string(filename_data, r'prizes \s* = \s* \[ .+ , .+ , .+ , .+ \]', 1, points=5)
        test_prizes['name'] += "Testing that there is a variable prizes.  Prizes is a list with exactly 4 items.<br>" \
                               "Prizes is a named exactly 'prizes' and not something else."
        tests.append(test_prizes)
        if not test_prizes['pass']:
            test_prizes['fail_message'] += r"Looking for variable prizes that is a list with 4 items.  We name lists " \
                                           r"plural to help keep track of what is what.<br>  " \
                                           r"Looked for 'prizes \s* = \s* \[ .+ , .+ , .+ , .+ \]' " \
                                           r"in this string: <br>" + filename_data
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:

            # Check for question
            test_find_input = find_questions(filename_data, 1, 5)
            tests.append(test_find_input)

            # Test input gives output
            test_runs = python_2_051a(filename, filename_data)
            tests.append(test_runs)

            # Test efficiency
            test_efficiency = find_all_strings(filename_data, [r'prizes\[0\]', r'prizes\[1\]',
                                                               r'prizes\[2\]', r'prizes\[3\]'], 5)
            test_efficiency['name'] += "Testing efficiency.  Do NOT want to have a big if/elif/else.<br>" \
                                       "If you have a variable x which is a number of item in list," \
                                       " list[x-1] will get you the correct item.<br>" \
                                       "<br>  This technique saves a lot of lines of code over a big if/elif  " \
                                       "and scales to big numbers.  " \
                                       "<br>That is, a list with 10,000 items will need " \
                                       "just one line to print out the list item whereas with a big if/else, " \
                                       "you will need 20,000 lines of code.<br>" \
                                       " If this does not make sense, ask a neighbor or the teacher."
            if test_efficiency['pass']:
                test_efficiency['pass'] = False
                test_efficiency['points'] = 0
                test_efficiency['fail_message'] += "You want to use a variable for the list index of prizes."
            else:
                test_efficiency['pass'] = True
                test_efficiency['pass_message'] += "(actually, did NOT find prizes[0], prizes[1] prizes[2] prizes[3]"
                test_efficiency['points'] = 5
            tests.append(test_efficiency)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 7)
            tests.append(test_pep8)
            test_help = helps(filename, 2.5)
            tests.append(test_help)

            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']
            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_2051b')
def feedback_2051b():

    from app.python_labs.find_items import find_if, find_questions, find_list, find_elif, find_else
    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.python_2_05x import python_2_051b_1
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 32.5, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '2.051b')
    tests.append(test_filename)
    if not test_filename['pass'] is True:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # test for a list being created with 4 items
        test_lcs = find_list(filename_data, num_items=4, list_name='learning_communities', points=3)
        tests.append(test_lcs)
        if not test_lcs['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # Read in the python file to filename_data
            filename_data = read_file_contents(filename)

            test_scores = find_list(filename_data, num_items=4, list_name='scores', points=3)
            test_scores['name'] += "All items should be initially all zero (which we do not check right now).<br>"
            tests.append(test_scores)
            if not test_scores['pass']:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:
                test_question = find_questions(filename_data, 1, 1)
                if not test_question['pass']:
                    test_question['fail_message'] += "You need to ask the user a question about which " \
                                                     "LC to vote for. <br>"
                tests.append(test_question)

                # test if, check for at least 1 if statement
                test_if = find_if(filename_data, 1, 1)
                tests.append(test_if)

                # test else check for at least 1 else statement
                test_else = find_else(filename_data, 1, 4)
                tests.append(test_else)

                # test elif check for at least 3
                test_elif = find_elif(filename_data, 3, 1)
                tests.append(test_elif)

                # Try C C R L S, should get 2, 1, 1, 1
                test_1_io = python_2_051b_1(filename, 5)
                tests.append(test_1_io)

                # Try C R L S blah blah blah, should get 1, 1, 1, 1
                test_2_io = python_2_051b_1(filename, 5)
                tests.append(test_2_io)

                # Find number of PEP8 errors and helps
                test_pep8 = pep8(filename, 7)
                tests.append(test_pep8)
                test_help = helps(filename, 2.5)
                tests.append(test_help)

                for test in tests:
                    if test['pass']:
                        score_info['score'] += test['points']

                score_info['finished_scoring'] = True
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)


@app.route('/feedback_3011')
def feedback_3011():

    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.find_items import find_questions, find_list, find_random, find_print
    from app.python_labs.python_3_011 import python_3_011_2, python_3_011_1
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 64, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '3.011')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # test for a list being created with 6 items
        test_houses = find_list(filename_data, num_items=6, list_name='houses', points=10)
        tests.append(test_houses)
        if not test_houses['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # Asks a question, but that is ignore
            test_question = find_questions(filename_data, 1, 5)
            if not test_question['pass']:
                test_question['fail_message'] += "You need to ask the user a question to try to influence the hat. <br>"
            tests.append(test_question)

            # test for importing random
            test_random = find_random(filename_data, 5)
            tests.append(test_random)
            if not test_random['pass']:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:
                # test for importing randint
                test_randint = find_random(filename_data, 5, randint=True)
                tests.append(test_randint)

                # Check for at least 1 print statement
                test_find_print = find_print(filename_data, 1, 5)
                tests.append(test_find_print)

                # Test efficiency
                test_efficiency = python_3_011_1(filename_data, 5)
                tests.append(test_efficiency)

                test_runs = python_3_011_2(filename, filename_data, 10)
                tests.append(test_runs)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 14)
            tests.append(test_pep8)
            test_help = helps(filename, 5)
            tests.append(test_help)

            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_3020')
def feedback_3020():

    from app.python_labs.find_items import find_function, function_called, find_list
    from app.python_labs.filename_test import filename_test
    from app.python_labs.function_test import extract_all_functions, extract_single_function, run_unit_test, \
        create_testing_file
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8
    from app.python_labs.python_3_020 import ten_runs, check_random

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '3.020')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        test_find_function_1 = find_function(filename, 'birthday_song', 1, points=4)
        tests.append(test_find_function_1)

        # Only continue if you have a birthday_song_function
        if not test_find_function_1['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # Check that function is called once
            test_birthday_song_run = function_called(filename, 'birthday_song', 1, points=4)
            tests.append(test_birthday_song_run)

            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)

            # function test 1
            test_function_1 = run_unit_test('3.020', 1, 4)
            test_function_1['name'] += " (prints out 'birthday' somewhere) "
            tests.append(test_function_1)

            # function test 2
            test_function_2 = run_unit_test('3.020', 2, 5)
            test_function_2['name'] += " (prints out input parameter somewhere) "
            tests.append(test_function_2)

            # function test 3
            test_function_3 = run_unit_test('3.020', 3, 8)
            test_function_3['name'] += " (output looks good) "
            tests.append(test_function_3)

            test_find_function_2 = find_function(filename, 'pick_card', 0, points=4)
            tests.append(test_find_function_2)

            # Only continue if you have a birthday_song_function
            if not test_find_function_2['pass']:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:

                cards_function = extract_single_function(filename, 'pick_card')

                test_find_cards = find_list(cards_function, num_items=4, list_name='cards', points=2)
                tests.append(test_find_cards)

                test_find_suits = find_list(cards_function, num_items=4, list_name='suits', points=2)
                tests.append(test_find_suits)

                # function test 4
                test_function_4 = run_unit_test('3.020', 4, 5)
                test_function_4['name'] += " (function picks 1 card) "
                tests.append(test_function_4)

                # Check that function is called once
                test_pick_card_run = function_called(filename, 'pick_card', 1, points=4)
                tests.append(test_pick_card_run)

                # Check that random is random
                test_random = check_random(filename)
                tests.append(test_random)

                # check that pick_card prints out 10 cards (looks for 'of' 10x)
                test_run_ten_cards = ten_runs(filename)
                tests.append(test_run_ten_cards)

                # Find number of PEP8 errors and helps
                test_pep8 = pep8(filename, 14)
                tests.append(test_pep8)
                test_help = helps(filename, 5)
                tests.append(test_help)

                for test in tests:
                    if test['pass']:
                        score_info['score'] += test['points']
                score_info['finished_scoring'] = True
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)


@app.route('/feedback_3026')
def feedback_3026():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_string, find_function, function_called, find_loop
    from app.python_labs.function_test import run_unit_test, create_testing_file, extract_all_functions, \
        extract_single_function
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 44.5, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '3.026')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Check for function return_min
        test_find_function = find_function(filename, 'return_min', 1, points=5)
        tests.append(test_find_function)

        # Only continue if you have a return_min_function
        if test_find_function['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            return_min_function = extract_single_function(filename, 'return_min')

            # Check that function is called 1x
            test_function_run = function_called(filename, 'return_min', 1, points=5)
            tests.append(test_function_run)

            # find string return (return in the function)
            test_return = find_string(return_min_function, r'return \s .+', 1, points=2.5)
            test_return["name"] += " (There is a return in the function)"
            test_return["fail_message"] += " (There is a return in the function)"
            tests.append(test_return)

            # find loop in function
            test_loop = find_loop(return_min_function, 2.5)
            test_loop["name"] += " (There is a loop in the code)"
            test_loop["fail_message"] += " (There is a loop in the function)"
            tests.append(test_loop)

            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)

            # function test 1
            test_function_1 = run_unit_test('3.026', 1, 5)
            test_function_1['name'] += " (return_min with list [-1, 3, 5, 99] returns -1) "
            tests.append(test_function_1)

            # function test 2
            test_function_2 = run_unit_test('3.026', 2, 5)
            test_function_2['name'] += " (return_min with list [-1, 3, 5, -99] returns -99) "
            tests.append(test_function_2)

            # function test 3
            test_function_3 = run_unit_test('3.026', 3, 5)
            test_function_3['name'] += " (return_min with list [5] returns 5) "
            tests.append(test_function_3)

            # function test 4
            test_function_4 = run_unit_test('3.026', 4, 5)
            test_function_4['name'] += " (return_min with list [5, 4, 99, -11, 44, -241, -444, -999, 888, -2] " \
                                       "returns -444) "
            tests.append(test_function_4)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 7)
            tests.append(test_pep8)
            test_help = helps(filename, 2.5)
            tests.append(test_help)

            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_4011')
def feedback_4011():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_function, find_loop, function_called, find_if
    from app.python_labs.function_test import run_unit_test, extract_single_function,\
        extract_all_functions, create_testing_file
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '4.011')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:

        # Check for function
        test_find_function = find_function(filename, 'could_it_be_a_martian_word', 1, points=5)
        tests.append(test_find_function)

        if test_find_function['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            extract_all_functions(filename)
            function_data = extract_single_function(filename, 'could_it_be_a_martian_word')
            create_testing_file(filename)

            # Check for a loop of some sort (for or while)
            test_loop = find_loop(function_data, 5)
            test_loop['name'] += "Testing there is a loop in the could_it_be_a_martian_word function.<br>"
            tests.append(test_loop)

            if test_loop['pass'] is False:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:
                # Check that function is called 3x
                test_function_run = function_called(filename, 'could_it_be_a_martian_word', 3, points=5)
                tests.append(test_function_run)

                test_function_1 = run_unit_test('4.011', 1, 10)
                test_function_1['name'] += " (could_it_be_a_martian_word with 'bcdefgijnpqrstuvwxyz' returns []) "
                tests.append(test_function_1)

                test_function_2 = run_unit_test('4.011', 2, 10)
                test_function_2['name'] += " (could_it_be_a_martian_word with 'ba' returns ['a']) "
                tests.append(test_function_2)

                test_function_3 = run_unit_test('4.011', 3, 10)
                test_function_3['name'] += " (could_it_be_a_martian_word with 'baa' returns ['a']) "
                tests.append(test_function_3)

                test_ifs = find_if(function_data, 3, 5, minmax='max')
                tests.append(test_ifs)

                # Find number of PEP8 errors and helps
                test_pep8 = pep8(filename, 14)
                tests.append(test_pep8)
                test_help = helps(filename, 5)
                tests.append(test_help)

                for test in tests:
                    if test['pass']:
                        score_info['score'] += test['points']
                score_info['finished_scoring'] = True
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)


@app.route('/feedback_4021')
def feedback_4021():
    from app.python_labs.find_items import find_function, function_called, find_loop
    from app.python_labs.filename_test import filename_test
    from app.python_labs.function_test import run_unit_test, extract_all_functions, extract_single_function, \
        create_testing_file
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 37,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '4.021')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Check for function the_rock_says
        test_find_function = find_function(filename, 'the_rock_says', 1, points=5)
        tests.append(test_find_function)
        if test_find_function['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)
            function_data = extract_single_function(filename, 'the_rock_says')

            # Check for a loop of some sort (for or while)
            test_loop = find_loop(function_data, 2.5)
            test_loop['name'] += "Testing there is a loop in the the_rock_says function.<br>"
            tests.append(test_loop)

            if test_loop['pass'] is False:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:
                # Check that function is called 3x
                test_function_run = function_called(filename, 'the_rock_says', 3, points=5)

                tests.append(test_function_run)

                # test1 for the_rock_says
                test_function_1 = run_unit_test('4.021', 1, 5)
                test_function_1['name'] += " (Testing calling the_rock_says with list ['eggs', 'apple'] returns a " \
                                           "list ['The Rock says eggs', 'The Rock says apple']) "
                tests.append(test_function_1)

                # test2 for the_rock_says
                test_function_2 = run_unit_test('4.021', 2, 5)
                test_function_2['name'] += " (Testing calling the_rock_says withlist ['eggs', 'smell'] returns " \
                                           "['The Rock says eggs', 'Do you smell what The Rock is cooking']" \
                                           "['The Rock says eggs', 'The Rock says apple']) <br> "
                tests.append(test_function_2)

                # test3 for the_rock_says
                test_function_3 = run_unit_test('4.021', 3, 5)
                test_function_3['name'] += " (Testing calling the_rock_says with list " \
                                           "['smog', 'smells', 'smashmouth'] returns ['Do you smell what The Rock is" \
                                           " cooking', " \
                                           "'Do you smellell what The Rock is cooking', " \
                                           "'Do you smellellellellellellell what The Rock is cooking'] <br> "
                tests.append(test_function_3)

                # Find number of PEP8 errors and helps
                test_pep8 = pep8(filename, 7)
                tests.append(test_pep8)
                test_help = helps(filename, 2.5)
                tests.append(test_help)

                for test in tests:
                    if test['pass']:
                        score_info['score'] += test['points']

                score_info['finished_scoring'] = True
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)


@app.route('/feedback_4022')
def feedback_4022():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_function, function_called, find_loop
    from app.python_labs.function_test import run_unit_test, extract_all_functions, \
        extract_single_function, create_testing_file
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 37,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '4.022')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Check for function
        test_find_function = find_function(filename, 'bad_lossy_compression', 1, points=5)
        tests.append(test_find_function)
        if test_find_function['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # extract functions and create python test file
            extract_all_functions(filename)
            function_data = extract_single_function(filename, 'bad_lossy_compression')
            create_testing_file(filename)

            # Check for a loop of some sort (for or while)
            test_loop = find_loop(function_data, 2.5)
            test_loop['name'] += "Testing there is a loop in the bad_lossy_compression function.<br>"
            tests.append(test_loop)

            if test_loop['pass'] is False:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:
                # Check that function is called 3x
                test_function_run = function_called(filename, 'bad_lossy_compression', 3, points=5)
                tests.append(test_function_run)

                # test1
                test_function_1 = run_unit_test('4.022', 1, 5)
                test_function_1['name'] += " (Testing calling bad_lossy_compression with 'The rain in spain falls " \
                                           "mainly in the plain' returns 'The ain n spin flls ainl in he pain') "
                tests.append(test_function_1)

                # test2 for the_rock_says
                test_function_2 = run_unit_test('4.022', 2, 5)
                test_function_2['name'] += " (Testing calling bad_lossy_compression with " \
                                           "'I am sick and tired of these darned snakes on this darned plane'" \
                                           " returns 'I a sik ad tredof hes danedsnaes n tis arnd pane' <br> "
                tests.append(test_function_2)

                # test3 for the_rock_says
                test_function_3 = run_unit_test('4.022', 3, 5)
                test_function_3['name'] += "Testing calling bad_lossy_compression with 'Madness?!?!?!?!" \
                                           " THIS IS SPARTA!!!!'" \
                                           " returns 'Madess!?!!?!THI ISSPATA!!!' <br> "
                tests.append(test_function_3)

                # Find number of PEP8 errors and helps
                test_pep8 = pep8(filename, 7)
                tests.append(test_pep8)
                test_help = helps(filename, 2.5)
                tests.append(test_help)

                for test in tests:
                    if test['pass']:
                        score_info['score'] += test['points']
                score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)

    
@app.route('/feedback_4025')
def feedback_4025():

    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_loop, find_string
    from app.python_labs.function_test import extract_all_functions, create_testing_file, extract_single_function, \
        run_unit_test
    from app.python_labs.python_4_025 import win_all, win_most

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 114,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '4.025')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)
        play_tournament_function = extract_single_function(filename, 'play_tournament')

        test_function_1 = run_unit_test('4.025', 1, 15)
        test_function_1['name'] += " Testing game function - 1000 runs should give between 730 and 780 wins " \
                                   "(10 points) "
        tests.append(test_function_1)

        if test_function_1['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:

            test_loop = find_loop(play_tournament_function, 5)
            test_loop['name'] += " Testing for loop in play_tournament function.<br>"
            tests.append(test_loop)

            test_function_2 = run_unit_test('4.025', 2, 5)
            test_function_2['name'] += " Testing play_tournament function.  If I call play_tournament with " \
                                       "input parameters (0.75, 'Wimbledon'), play_tournament  should " \
                                       "print 'Wimbledon' somewhere (2.5 points).<br>"
            tests.append(test_function_2)

            test_function_3 = run_unit_test('4.025', 3, 5)
            test_function_3['name'] += " Testing play_tournament function.  If I call play_tournament with " \
                                       "input parameters (1.0, 'Wimbledon'), Serena should win this tournament" \
                                       "(5 points).<br>"
            tests.append(test_function_3)

            test_function_4 = run_unit_test('4.025', 4, 10)
            test_function_4['name'] += " Testing play_season function.  If I call play_season enough times," \
                                       "Serena should win US open most, followed by Wimbledon, followed by French " \
                                       "open (10 points).<br>"
            tests.append(test_function_4)

            test_function_5 = run_unit_test('4.025', 5, 10)
            test_function_5['name'] += " Testing data_analysis function, looking to see if correct percentages are " \
                                       "printed (10 points).<br>"
            tests.append(test_function_5)

            run_simulation_function = extract_single_function(filename, 'run_simulation')
            test_run_sim = find_loop(run_simulation_function, 5)
            test_run_sim['name'] = "Looking for loop in the run_simulation function (5 points).<br>"
            tests.append(test_run_sim)

            test_run_sim_data_analysis = find_string(run_simulation_function, r'\s*data_analysis\(', 1, points=5)
            test_run_sim_data_analysis['name'] = "Checking that run_simulation calls data_analysis (5 points).<br>"
            tests.append(test_run_sim_data_analysis)

            test_function_6 = run_unit_test('4.025', 6, 5)
            test_function_6['name'] = " Testing run_simulation function, verifying that if you call it with" \
                                      "p_num_simulations of 300, the printout shows 300 runs. <br>" \
                                      " Requires a working data_analysis (5 points).<br>"
            tests.append(test_function_6)

            # IO tests
            test_io_1 = win_all(filename)
            tests.append(test_io_1)

            test_io_2 = win_most(filename)
            tests.append(test_io_2)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 14)
            tests.append(test_pep8)
            test_help = helps(filename, 5)
            tests.append(test_help)

            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_6_011')
def feedback_6011():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_function, find_elif, find_dictionary
    from app.python_labs.function_test import extract_all_functions, create_testing_file, run_unit_test
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8
    from app.python_labs.read_file_contents import read_file_contents

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '6.011')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:

        test_find_function = find_function(filename, 'bob_kraft_translator', 2, points=5)
        tests.append(test_find_function)
        if not test_find_function['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:

            # Test for dictionary with 3+ items
            filename_data = read_file_contents(filename)

            test_dictionary = find_dictionary(filename_data, num_items=3, points=10)
            tests.append(test_dictionary)

            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)

            test_function_1 = run_unit_test('6.011', 1, 10)
            test_function_1['name'] += " (Sent in dictionary  {'wth': 'What the heck'}, search for 'wth', " \
                                       "returned 'what the heck') <br>"
            tests.append(test_function_1)

            test_function_2 = run_unit_test('6.011', 2, 10)
            test_function_2['name'] += " (Sent in dictionary  {'wth': 'What the heck', 'aymm': 'Ay yo my man',}, " \
                                       "looking for aymm, should receive 'Ay yo my man'. <br>"
            tests.append(test_function_2)

            test_function_3 = run_unit_test('6.011', 3, 10)
            test_function_3['name'] += " (Sent in dictionary  {'wth': 'What the heck','aymm': 'Ay yo my man',}, " \
                                       "asdfasdf, received something with 'do not know''. <br>"
            tests.append(test_function_3)

            # Check for 3 ifs on different lines
            test_elifs = find_elif(filename_data, 3, 5, minmax='max')
            tests.append(test_elifs)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 14)
            tests.append(test_pep8)
            test_help = helps(filename, 5)
            tests.append(test_help)

            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']
            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_6_021')
def feedback_6021():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_function, function_called, find_dictionary
    from app.python_labs.function_test import extract_all_functions, extract_single_function, \
        create_testing_file, run_unit_test
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '6.021')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        extract_all_functions(filename)
        create_testing_file(filename)

        test_find_function = find_function(filename, 'martinez_dictionary', 1, points=5)
        tests.append(test_find_function)

        # Check that function is called 3x
        test_function_run = function_called(filename, 'martinez_dictionary', 3, points=5)
        tests.append(test_function_run)

        # extract martinez_dictionary functions and look for dictionary
        martinez_function = extract_single_function(filename, 'martinez_dictionary')
        test_dictionary = find_dictionary(martinez_function, num_items=0, points=5)
        tests.append(test_dictionary)

        # Martinez test 1
        test_function_1 = run_unit_test('6.021', 1, 10)
        tests.append(test_function_1)

        # Martinez test 2
        test_function_2 = run_unit_test('6.021', 2, 10)
        tests.append(test_function_2)

        test_find_function = find_function(filename, 'data_generator', 2, points=5)
        tests.append(test_find_function)
        if test_find_function['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # Martinez test 3
            test_function_3 = run_unit_test('6.021', 3, 5)
            tests.append(test_function_3)

            # Martinez test 4
            test_function_4 = run_unit_test('6.021', 4, 5)
            tests.append(test_function_4)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 14)
            tests.append(test_pep8)
            test_help = helps(filename, 5)
            tests.append(test_help)

            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']
                flash(test['name'])
                flash(score_info['score'])

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_6_031')
def feedback_6031():
    from app.python_labs.function_test import extract_all_functions, run_unit_test, create_testing_file
    from app.python_labs.find_items import find_function, find_loop, find_dictionary
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test
    from app.python_labs.read_file_contents import read_file_contents
    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '6.031')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        filename_data = read_file_contents(filename)

        test_dictionary = find_dictionary(filename_data, num_items=0, points=5)
        tests.append(test_dictionary)
        if test_dictionary['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:

            # Check for function add with 3 inputs
            test_find_function = find_function(filename, 'add', 3, points=5)
            tests.append(test_find_function)
            if test_find_function['pass'] is False:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:

                extract_all_functions(filename)
                create_testing_file(filename)

                # function test 1
                test_function_1 = run_unit_test('6.031', 1, 5)
                tests.append(test_function_1)

                # function test 2
                test_function_2 = run_unit_test('6.031', 2, 10)
                tests.append(test_function_2)

                # Check for function add with 2 inputs
                test_find_function = find_function(filename, 'get', 2, points=5)
                tests.append(test_find_function)
                if test_find_function['pass'] is False:
                    return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                           score_info=score_info)
                else:
                    # function test 3
                    test_function_3 = run_unit_test('6.031', 3, 5)
                    tests.append(test_function_3)

                    # function test 3
                    test_function_4 = run_unit_test('6.031', 4, 10)
                    tests.append(test_function_4)

                    # Check for a loop of some sort (for or while)
                    test_loop = find_loop(filename_data, 5)
                    tests.append(test_loop)

                    # Find number of PEP8 errors and helps
                    test_pep8 = pep8(filename, 14)
                    tests.append(test_pep8)
                    test_help = helps(filename, 5)
                    tests.append(test_help)

                    for test in tests:
                        if test['pass']:
                            score_info['score'] += test['points']

                    score_info['finished_scoring'] = True
                    return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                           score_info=score_info)


@app.route('/feedback_6_041')
def feedback_6041():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_function, find_string
    from app.python_labs.function_test import extract_all_functions, create_testing_file, run_unit_test
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8
    from app.python_labs.python_6_041 import five_loop
    from app.python_labs.read_file_contents import read_file_contents

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '6.041')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        filename_data = read_file_contents(filename)

        # Check for function add with 1 inputs
        test_find_function = find_function(filename, 'item_list_to_dictionary', 1, points=5)
        tests.append(test_find_function)
        if test_find_function['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)

            # function test 1
            test_function_1 = run_unit_test('6.041', 1, 10)
            tests.append(test_function_1)

            # Check for function 1 inputs
            test_find_function_2 = find_function(filename, 'min_item', 1, points=5)
            tests.append(test_find_function_2)

            # unit test 2
            test_function_2 = run_unit_test('6.041', 2, 20)
            tests.append(test_function_2)

            # Check that removes, just look for del or pop
            test_removal = find_string(filename_data, r"\.pop\( | del", 1, points=5)
            tests.append(test_removal)

            # Check that it's run 5x
            test_five_times = five_loop(filename_data)
            tests.append(test_five_times)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 14)
            tests.append(test_pep8)
            test_help = helps(filename, 5)
            tests.append(test_help)

            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_7_021')
def feedback_7021():
    from app.python_labs.find_items import find_class, find_function, function_called, object_created
    from app.python_labs.function_test import extract_all_functions, create_testing_file, run_unit_test
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '7.021')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:

        # Check for class Collectible
        test_class = find_class(filename, 'Collectible', 'object', points=5)
        tests.append(test_class)

        if test_class['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:

            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)

            # function test 2
            test_function_1 = run_unit_test('7.021', 1, 15)
            tests.append(test_function_1)

            # Check for function existence
            test_find_function = find_function(filename, 'collectible_printer', 1, points=5)
            tests.append(test_find_function)

            # test 2
            test_function_2 = run_unit_test('7.021', 2, 5)
            tests.append(test_function_2)

            # test 3
            test_function_3 = run_unit_test('7.021', 3, 10)
            tests.append(test_function_3)

            # Check for all objects
            test_objects = object_created(filename, 'Collectible', 3, points=5)
            tests.append(test_objects)

            # Check that function is called
            test_function_run = function_called(filename, 'collectible_printer', 1, points=5)
            tests.append(test_function_run)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 14)
            tests.append(test_pep8)
            test_help = helps(filename, 5)
            tests.append(test_help)

            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']

            score_info['finished_scoring'] = True

            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_7_031')
def feedback_7031():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.function_test import extract_all_functions, create_testing_file, run_unit_test
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 34.5, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '7.031')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:

        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)

        # unit test 1
        test_function_1 = run_unit_test('7.031', 1, 5)
        tests.append(test_function_1)

        # unit test 2
        test_function_2 = run_unit_test('7.031', 2, 10)
        tests.append(test_function_2)

        # unit test 3
        test_function_3 = run_unit_test('7.031', 3, 10)
        tests.append(test_function_3)

        # Find number of PEP8 errors and helps
        test_pep8 = pep8(filename, 7)
        tests.append(test_pep8)
        test_help = helps(filename, 2.5)
        tests.append(test_help)

        for test in tests:
            if test['pass']:
                score_info['score'] += test['points']

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_7_034')
def feedback_7034():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.function_test import extract_all_functions, create_testing_file, run_unit_test
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 34.5,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '7.034')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)

        # unit test 1
        unit_test_1 = run_unit_test('7.034', 1, 5)
        tests.append(unit_test_1)

        # unit test 2
        unit_test_2 = run_unit_test('7.034', 2, 5)
        tests.append(unit_test_2)

        # unit test 3
        unit_test_3 = run_unit_test('7.034', 3, 5)
        tests.append(unit_test_3)

        # unit test 4
        unit_test_4 = run_unit_test('7.034', 4, 5)
        tests.append(unit_test_4)

        # unit test 5
        unit_test_5 = run_unit_test('7.034', 5, 5)
        tests.append(unit_test_5)

        # Find number of PEP8 errors and helps
        test_pep8 = pep8(filename, 7)
        tests.append(test_pep8)
        test_help = helps(filename, 2.5)
        tests.append(test_help)

        for test in tests:
            if test['pass']:
                score_info['score'] += test['points']

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)    


@app.route('/feedback_4031')
def feedback_4031():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.function_test import create_testing_file, extract_all_functions, run_unit_test
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8
    from app.python_labs.python_4_03x import python_4_031_double_loops, python_4_031_good_prints

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '4.031')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:

        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)

        # unit test 1
        unit_test_1 = run_unit_test('4.031', 1, 2.5)
        tests.append(unit_test_1)

        # unit test 2
        unit_test_2 = run_unit_test('4.031', 2, 2.5)
        tests.append(unit_test_2)

        # unit test 3
        unit_test_3 = run_unit_test('4.031', 3, 2.5)
        tests.append(unit_test_3)

        # unit test 4
        unit_test_4 = run_unit_test('4.031', 4, 5)
        tests.append(unit_test_4)

        # unit test 5
        unit_test_5 = run_unit_test('4.031', 5, 5)
        tests.append(unit_test_5)

        # unit test 6
        unit_test_6 = run_unit_test('4.031', 6, 5)
        tests.append(unit_test_6)

        # unit test 7
        unit_test_7 = run_unit_test('4.031', 7, 5)
        tests.append(unit_test_7)

        # unit test 8
        unit_test_8 = run_unit_test('4.031', 8, 7.5)
        tests.append(unit_test_8)

        # Check for double loops
        test_loop = python_4_031_double_loops(filename)
        tests.append(test_loop)

        # Check for double loops
        test_prints = python_4_031_good_prints(filename)
        tests.append(test_prints)

        # Find number of PEP8 errors and helps
        test_pep8 = pep8(filename, 14)
        tests.append(test_pep8)
        test_help = helps(filename, 5)
        tests.append(test_help)

        for test in tests:
            if test['pass']:
                score_info['score'] += test['points']

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)

    
@app.route('/feedback_4036')
def feedback_4036():
    from app.python_labs.find_items import find_function
    from app.python_labs.function_test import extract_all_functions, create_testing_file, run_unit_test
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 89,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '4.036')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:

        # Check for function existence
        test_find_function = find_function(filename, 'fried_chicken_problem_1', 2, points=5)
        tests.append(test_find_function)

        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)

        # unit test 1
        unit_test_1 = run_unit_test('4.036', 1, 10)
        tests.append(unit_test_1)

        # unit test 2
        unit_test_2 = run_unit_test('4.036', 2, 10)
        tests.append(unit_test_2)

        # Check for function existence
        test_find_function = find_function(filename, 'fried_chicken_problem_2', 2, points=5)
        tests.append(test_find_function)

        # unit test 3
        unit_test_3 = run_unit_test('4.036', 3, 10)
        tests.append(unit_test_3)

        # unit test 4
        unit_test_4 = run_unit_test('4.036', 4, 10)
        tests.append(unit_test_4)

        # Find number of PEP8 errors and helps
        test_pep8 = pep8(filename, 14)
        tests.append(test_pep8)
        test_help = helps(filename, 5)
        tests.append(test_help)

        for test in tests:
            if test['pass']:
                score_info['score'] += test['points']

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
