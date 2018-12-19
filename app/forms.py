from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, SelectField

class UploadForm(FlaskForm):
    file = FileField('Select file')
    lab = SelectField('Lab?', choices=[('1.04', '1.04'), ('1.06', '1.06')])
    submit = SubmitField('Submit for autograding')