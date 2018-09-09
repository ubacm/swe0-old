import os
import re


# Only log-in attempts with email addresses that match this pattern will be accepted.
AUTH_EMAIL_PATTERN = re.compile(os.getenv('AUTH_EMAIL_PATTERN', '.+@buffalo.edu$'))


# Prevent Flask-RESTful from adding to error responses.
ERROR_404_HELP = False


# List of extensions to be enabled; if empty, a default list of extensions will be enabled.
ENABLED_EXTENSIONS = list(filter(None, re.split(' *, *', os.getenv('ENABLED_EXTENSIONS', ''))))


SECRET_KEY = os.getenv('SECRET_KEY', 'placeholder')


# Client IDs and secrets for OAuth.
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
SLACK_CLIENT_ID = os.getenv('SLACK_CLIENT_ID')
SLACK_CLIENT_SECRET = os.getenv('SLACK_CLIENT_SECRET')


SQLALCHEMY_DATABASE_URI = os.getenv(
    'DATABASE_URI', 'sqlite:///{}'.format(os.path.abspath('database.sqlite3')))
SQLALCHEMY_TRACK_MODIFICATIONS = False
