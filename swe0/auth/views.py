from flask import redirect, render_template, url_for
from flask_login import login_user, logout_user

from swe0 import app, db
from . import auth_blueprint, oauth
from .models import User


@auth_blueprint.route('/log-in')
def log_in():
    return render_template('log_in.html')


@auth_blueprint.route('/log-out')
def log_out():
    logout_user()
    return redirect(url_for('.log_in'))


@auth_blueprint.route('/log-in/slack')
def log_in_slack():
    redirect_uri = url_for('.authorize_slack', _external=True)
    return oauth.slack.authorize_redirect(redirect_uri)


@auth_blueprint.route('/authorize/slack')
def authorize_slack():
    try:
        token = oauth.slack.authorize_access_token()
    except KeyError:
        # This will happen if the user clicks Cancel instead of Continue.
        pass
    else:
        email = token['user']['email']
        name = token['user']['name']

        if app.config['AUTH_EMAIL_PATTERN'].match(email):
            user = User.query.filter_by(email=email).first()
            if user is None:
                user = User(email=email, name=name)
                db.session.add(user)
                db.session.commit()
            elif user.name != name:
                user.name = name
                db.session.commit()

            login_user(user)

    return redirect(url_for('.log_in'))
