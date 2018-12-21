from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, SelectField


class UploadForm(FlaskForm):
    file = FileField('Select file')
    lab = SelectField('Lab?', choices=[('1.040', '1.040'), ('1.060', '1.060'), ('2.020','2.020')])
    submit = SubmitField('Submit for autograding')
