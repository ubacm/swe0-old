from flask import Blueprint

name = 'Voting'
description = 'Vote'
voting_blueprint = Blueprint('voting', __name__, template_folder='templates')


# Ensure these are available when the blueprint is being registered.
from . import views
