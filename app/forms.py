from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, SelectField


class UploadForm(FlaskForm):
    file = FileField('Select file')
    lab = SelectField('Lab?', choices=[('1.040', '1.040'), ('1.060', '1.060'), ('2.020','2.020'),
                                       ('2.032a', '2.032a'), ('2.032b', '2.032b'), ('2.040', '2.040'),
                                       ('2.051a', '2.051a'), ('2.051b', '2.051b'), ('3.011', '3.011'),
                                       ('3.020', '3.020'),  ('3.026', '3.026'),  ('4.011', '4.011'),
                                       ('4.021', '4.021'), ('4.022', '4.022'),  ('4.025', '4.025'),
                                       ('4.031', '4.031'),  ('4.036', '4.036'), ('6.011', '6.011'), ('6.021', '6.021'),
                                       ('6.031', '6.031'),
                                       ('6.041', '6.041'), ('7.021', '7.021'), ('7.031', '7.031'),
                                       ('7.034', '7.034'), ])
    submit = SubmitField('Submit for autograding')


class UploadScratchForm(FlaskForm):
    file = FileField('Select file')
    lab = SelectField('Lab?', choices=[('1.3', '1.3'), ('1.4_1.5', '1.4_1.5'),
                                       ('1.x_family_migration_story', '1.x_family_migration_story'), ('2.2', '2.2'),
                                       ('2.4_alternate', '2.4_alternate'), ('2.5_alternate', '2.5_alternate'),
                                       ('2.6', '2.6'), ('3.2_alternate', '3.2_alternate'),
                                       ('3.3_3.4_alternate', '3.3_3.4_alternate'), ('4.2_alternate', '4.2_alternate'),
                                       ('4.3a_alternate', '4.3a_alternate'), ('karel1', 'karel1'), ('karel2a', 'karel2a'),
                                       ('karel2b', 'karel2b'),
                                       ('karel3a', 'karel3a'), ('karel3b', 'karel3b'), ('karel3c', 'karel3c'),
                                       ('karel3d', 'karel3d')])
    submit = SubmitField('Submit for autograding')
