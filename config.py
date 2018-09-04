import os
import re


# Only log-in attempts with email addresses that match this pattern will be accepted.
AUTH_EMAIL_PATTERN = re.compile(os.getenv('AUTH_EMAIL_PATTERN', '.+@buffalo.edu$'))


SECRET_KEY = os.getenv('SECRET_KEY', 'placeholder')

SLACK_CLIENT_ID = os.getenv('SLACK_CLIENT_ID')
SLACK_CLIENT_SECRET = os.getenv('SLACK_CLIENT_SECRET')

SQLALCHEMY_DATABASE_URI = os.getenv(
    'DATABASE_URI', 'sqlite:///{}'.format(os.path.abspath('database.sqlite3')))
SQLALCHEMY_TRACK_MODIFICATIONS = False
