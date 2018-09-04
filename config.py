import os


SECRET_KEY = os.getenv('SECRET_KEY', 'placeholder')

SLACK_CLIENT_ID = os.getenv('SLACK_CLIENT_ID')
SLACK_CLIENT_SECRET = os.getenv('SLACK_CLIENT_SECRET')

SQLALCHEMY_DATABASE_URI = os.getenv(
    'DATABASE_URI', 'sqlite:///{}'.format(os.path.abspath('database.sqlite3')))
SQLALCHEMY_TRACK_MODIFICATIONS = False
