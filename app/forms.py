from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, SelectField, StringField


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
                                       ('4.3a_alternate', '4.3a_alternate'), ('4.3b_alternate', '4.3b_alternate'),
                                       ('4.4','4.4'),
                                       ('karel1', 'karel1'), ('karel2a', 'karel2a'),
                                       ('karel2b', 'karel2b'),
                                       ('karel3a', 'karel3a'), ('karel3b', 'karel3b'), ('karel3c', 'karel3c'),
                                       ('karel3d', 'karel3d')])
    submit = SubmitField('Submit for autograding')


class UploadDocLinkForm(FlaskForm):
    link = StringField('Copy+paste link of Google document here')
    lab = SelectField('Lab?', choices=[('binary_practice', 'binary_practice'),
                                       ('black_and_white_pixelation', 'black_and_white_pixelation'),
                                       ('encoding_color_images', 'encoding_color_images'),
                                       ('encryption_1', 'encryption_1'), ('encryption_2', 'encryption_2'),
                                       ('encryption_3', 'encryption_3'),
                                       ('encryption_4', 'encryption_4'),
                                       ('hardware_esd_formfactors_cards', 'hardware_esd_formfactors_cards'),
                                       ('hex_minilab', 'hex_minilab'),
                                       ('ip_addressing_dns', 'ip_addressing_dns'),
                                       ('privacy_policies', 'privacy_policies'),
                                       ('research_yourself', 'research_yourself'),
                                       ('routers_and_redundancy', 'routers_and_redundancy'),
                                       ('python_1.020', 'python_1.020'),
                                       ('scratch_1.2', 'scratch_1.2'),
                                       ('scratch_2.5_alternate', 'scratch_2.5_alternate')])
    submit = SubmitField('Submit for autograding')
