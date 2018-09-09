from authlib.flask.client import OAuth
from flask import Blueprint
from flask_login import LoginManager

from .models import User


auth_blueprint = Blueprint('auth', __name__, template_folder='templates')

login_manager = LoginManager()

oauth = OAuth()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# Set up Google OAuth.
oauth.register(
    'google',
    access_token_url='https://www.googleapis.com/oauth2/v4/token',
    authorize_url='https://accounts.google.com/o/oauth2/v2/auth',
    api_base_url='https://www.googleapis.com/',
    client_kwargs={
        'scope': 'email openid profile',
    },
)

# Set up Slack OAuth.
oauth.register(
    'slack',
    access_token_url='https://slack.com/api/oauth.access',
    authorize_url='https://slack.com/oauth/authorize',
    api_base_url='https://slack.com/api/',
    client_kwargs={
        'scope': 'identity.basic identity.email',
        'token_endpoint_auth_method': 'client_secret_post',
    },
)


# Ensure these are available when the blueprint is being registered.
from . import views
