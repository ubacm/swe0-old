from flask import flash, redirect, render_template, request, session, url_for
from flask_login import current_user, login_user, logout_user

from swe0 import app, db
from . import auth_blueprint, oauth
from .models import User


__LOG_IN_REDIRECT_SESSION_KEY = 'swe0_auth_log_in_redirect'


@auth_blueprint.route('/log-in')
def log_in():
    # Redirect user to the page from the "next" param after login.
    next_path = request.args.get('next')
    if next_path and next_path.startswith('/'):
        session[__LOG_IN_REDIRECT_SESSION_KEY] = next_path
    if current_user.is_authenticated:
        next_path = session.pop(__LOG_IN_REDIRECT_SESSION_KEY, None)
        if next_path:
            return redirect(next_path)

    return render_template('log_in.html')


@auth_blueprint.route('/log-out')
def log_out():
    logout_user()
    return redirect(url_for('.log_in'))


@auth_blueprint.route('/log-in/slack')
def log_in_slack():
    redirect_uri = url_for('.authorize_slack', _external=True)
    return oauth.slack.authorize_redirect(redirect_uri)


@auth_blueprint.route('/log-in/google')
def log_in_google():
    redirect_uri = url_for('.authorize_google', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


@auth_blueprint.route('/authorize/slack')
def authorize_slack():
    try:
        token = oauth.slack.authorize_access_token()
    except KeyError:
        flash('You canceled Slack authentication.')
    else:
        email = token['user']['email']
        name = token['user']['name']
        _authorize(email, name)
    return redirect(url_for('.log_in'))


@auth_blueprint.route('/authorize/google')
def authorize_google():
    oauth.google.authorize_access_token()
    user_info = oauth.google.get('oauth2/v3/userinfo').json()
    email = user_info['email']
    name = user_info['name']
    _authorize(email, name)
    return redirect(url_for('.log_in'))


def _authorize(email, name):
    user = User.query.filter_by(email=email).first()
    if user is None:
        # Only create an account if the pattern is matched.
        if app.config['AUTH_EMAIL_PATTERN'].match(email):
            user = User(email=email, name=name)
            db.session.add(user)
            db.session.commit()
        else:
            flash('Your email address, "{}", does not have access to log in.'.format(email))
    elif user.name != name:
        user.name = name
        db.session.commit()

    if user is not None:
        login_user(user)
