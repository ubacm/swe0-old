from flask import Blueprint

name = 'Index'
description = 'Homepage'
override_url_prefix = ''
portal_blueprint = Blueprint('portal', __name__, template_folder='templates')


# Ensure these are available when the blueprint is being registered.
from . import views
