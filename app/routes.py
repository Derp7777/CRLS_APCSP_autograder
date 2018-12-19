from flask import render_template, url_for, request, redirect, flash

from app import app
from app.forms import UploadForm
from werkzeug.utils import secure_filename
import os


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Please select a file');
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
            if request.form['lab'] == '1.04':
                return redirect(url_for('feedback_104', filename=filename))


    form = UploadForm()
    user = {'username':'CRLS Scholar!!!'}
    return render_template('index.html', title='Home', user=user, form=form)

@app.route('/feedback_104')
def feedback_104():
    import re
    import subprocess
    import delegator

    # have same feedback for all
    # different template
    user = {'username':'CRLS Scholar'}
    tests = list();

    score_info = {'score': 0 , 'max_score':34.5, 'finished_scoring':False}
    
   
    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2018', filename )
    find_lab = re.search('1\.04', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2018_luismartinez_1.04.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2018_luismartinez_1.04.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                    " Other tests not run. They will be run after filename is fixed.<br>"
                    }

    if find_year and find_lab:
        test_filename['pass'] = True;
        tests.append(test_filename)


        # Check for part 1 asks 3 questions
        cmd = 'grep "input" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        inputs = int(c.out)
        test_inputs_1 = {"name" : "Testing for at genie asking at least 3 questions (first part of lab) ( 5 points )",
                         "pass" : True,
                         "pass_message": "Pass!  Genie asks at least 3 questions (first part of lab)",
                         "fail_message": "Fail.  Code does not have at least 3 inputs (first part of lab).<br>"
                         "The Genie needs to ask for 3 wishes for the first part"
                         "Please fix error and resubmit (other tests not run). <br>"
                        ,
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
            cmd = '/home/ewu/autograder/venv1/bin/python ' + filename + ' < /home/ewu/autograder/var/1.04.in > '\
                  + filename_output
            c = delegator.run(cmd)
        
            with open(filename_output, 'r') as myfile:
                outfile_data = myfile.read()
                
            
            search_object = re.search(r".+ "
                                      r"a1 "
                                      r".+ "
                                      r"a2 "
                                      r".+ "
                                      r"a3 "
                                      r".+ "
                                      , outfile_data, re.X|re.M|re.S)
            test_order_1 = {"name" : "Testing that Genie answers in correct order for part 1 (5 points)",
                            "pass" : True,
                            "pass_message": "Pass!  Genie appears to answer your wishes in correct order",
                            "fail_message": "Fail.  Double check that the Genie is answering in correct order. <br>"
                            "Genie needs to reply back with the 3 wishes you asked for in a particular order. <br>"
                            "Note: you must have a comma, period, space, or something between wishes."
                            "Review the sample run if this isn't clear. <br>"
            }
            if not search_object:
                test_order_1['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_order_1)


            # Check for part 2 asks 3 more questions, 6 total
            cmd = 'grep "input" ' + filename + ' | wc -l  '
            test_inputs_2 = {"name" : "Testing for at genie asking at least 6 questions (first + second part of lab) (5 points)",
                             "pass" : True,
                             "pass_message": "Pass!  Genie asks at least 6 questions (first + second part of lab)",
                             "fail_message": "Fail.  Code does not have at least 6 inputs (first + second part of lab).<br>"
                             "The Genie needs to ask for 3 wishes for the first part and 3 for the second part"
                             ,
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
            test_input_variable = {"name" : "Testing for use of variable to sub for repeated strings in asking questions (5 points)",
                                   "pass" : True,
                                   "pass_message": "Pass!  Genie appears to have stuck repeated strings into variables,"
                                   " per instructions AND there are at least 6 inputs",
                                   "fail_message": "Fail.  There are over 3 inputs with single or double quotations. <br>"
                                   "Please recheck the instructions about putting repeated strings into variables. "
                                   "This translates to -10 points deduction.<br>"
                                   ,
            }
            flash(inputs_variable)
            if inputs_variable < 4  :
                test_input_variable['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_input_variable)

            # Check that things are in correct order (a, b, c, then b, c, a)
            
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
                                      r"b1"
                                    , outfile_data, re.X|re.M|re.S)
            test_order_2 = {"name" : "Testing that Genie answers in correct order for part 1 and part 2 (5 points)",
                          "pass" : True,
                          "pass_message": "Pass!  Genie appears to answer your wishes in correct order for part 1 and part 2",
                          "fail_message": "Fail.  Double check that the Genie is answering in correct order for both part 1 and part 2. <br>"
                          "wish1, wish2, and wish3 responses need to go in a particular order. <br>"
                            "Note: you must have a comma, period, space, or something between wishes."

                          "Review the instructions if this isn't clear. <br>"
                         }
            if not search_object:
                test_order_2['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_order_2)



            # Find number of PEP8 errors
            cmd = 'pycodestyle ' + filename + ' | wc -l  '
            c = delegator.run(cmd)
            side_errors = int(c.out)
            test_pep8 = {"name": "Testing for PEP8 warnings and errors (7 points)",
                         "pass": True,
                         "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                         "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>" \
                         "This translates to -" + str(side_errors) + " point(s) deduction.<br>"
            }
            if side_errors != 0:
                test_pep8['pass'] = False
            score_info['score'] += int(7) - side_errors

            
            tests.append(test_pep8)

            # Check for help comment
            cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
            c = delegator.run(cmd)
            help_comments = int(c.out)
            test_help = {"name" : "Testing that you got a help and documented it as a comment (2.5 points)",
                         "pass" : True,
                         "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                         "Be sure your comment is meaningful, otherwise this can be overturned on review.",
                         "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                        " how somebody helped you with your code.  <br>"
                         "If you didn't have any problems, then ask somebody to check that your code"
                         " gives correct outputs, given an input.<br>"
                         "This translates to -5 points deduction.<br>"
                         ,
            }
            if help_comments == 0:
                test_help['pass'] = False
            else:
                score_info['score'] += 2.5
            tests.append(test_help)



            
            # format: list of test
            # list item: dictsionary: pass: True/False, pass_message, fail_message\\
                # tests:
            # 1. file name is correct x
            # 2. pep8 x
            # 2. help x
            # 3. correct order
            # 4. 3 wishes x2   x
            # 4. question into variable?
            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


    # filenames
    # '1' = [list of tests]
    # '2' = list of tests 2

