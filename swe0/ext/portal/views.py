import os

from flask import render_template
from flask_login import current_user, login_required

from swe0 import db
from swe0.auth.models import User
from . import portal_blueprint


@portal_blueprint.route('')
def index():
    return render_template('portal/index.html')
