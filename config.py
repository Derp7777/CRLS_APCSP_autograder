import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    UPLOAD_FOLDER = '/tmp'
    ALLOWED_EXTENSIONS = set(['py', 'sb3'])
