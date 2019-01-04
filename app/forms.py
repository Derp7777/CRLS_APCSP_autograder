from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, SelectField


class UploadForm(FlaskForm):
    file = FileField('Select file')
    lab = SelectField('Lab?', choices=[('1.040', '1.040'), ('1.060', '1.060'), ('2.020','2.020'),
                                       ('2.032a', '2.032a'), ('2.032b', '2.032b'), ('2.040', '2.040'),
                                       ('2.050a','2.050a'), ('2.050b','2.050b'), ('3.011','3.011')])
    submit = SubmitField('Submit for autograding')
