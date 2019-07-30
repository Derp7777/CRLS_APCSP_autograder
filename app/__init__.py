from flask import Flask, flash, request, redirect, url_for
from flask_bootstrap import Bootstrap
from config import Config
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

bootstrap = Bootstrap(app)
