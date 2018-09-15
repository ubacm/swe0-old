from flask import Blueprint


resumes_blueprint = Blueprint('resumes', __name__, template_folder='templates')


# Ensure these are available when the blueprint is being registered.
from . import views
