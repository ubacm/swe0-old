import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .utils import enable_extension


app = Flask(__name__)
app.config.from_pyfile(os.path.join('..', 'config.py'))

db = SQLAlchemy(app)


# Set up auth.
from .auth import auth_blueprint, login_manager, oauth
login_manager.init_app(app)
oauth.init_app(app)
app.register_blueprint(auth_blueprint, url_prefix='/auth')

enabled_extensions = []

# Use default extensions if no extensions were explicitly enabled.
if not app.config['ENABLED_EXTENSIONS']:
    app.config['ENABLED_EXTENSIONS'] = ['portal']

for extension in app.config['ENABLED_EXTENSIONS']:
    enabled_extensions.append(enable_extension(app, extension))
