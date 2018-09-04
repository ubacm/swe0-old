import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile(os.path.join('..', 'config.py'))

db = SQLAlchemy(app)
