Autograder for CRLS APCSP class


written in python with flask framework

Deployment on Ubuntu 16.04 or 18.04

$ apt-get install python3

$ python3 -m venv venv1 

$ . venv1/bin/activate

$ (venv)  pip install  delegator.py flask flask-bootstrap flask-WTF python-dotenv


Test:

$ flask run

Open browser.  Go to http://localhost:5000
You should see the application.
Try to autograde a file


Set up gunicorn (internal server to run the python app)
$ (venv)  pip install gunicorn
$ <something about ngnx here>





Updating an assignment:
* Edit app/forms.py
  - Edit the line with lab (line 6 or so) and add choices

* Edit app/routes.py
  - Edit index function, create a redirect for your new lab (see line 35 or so)
  - Create a feedback_labnumber
  - Edit it, look at feedback_1.04
  
