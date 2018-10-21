from flask import Blueprint
from flask_restful import Api


events_blueprint = Blueprint('events', __name__)
events_api = Api(events_blueprint, prefix='/api')


# Ensure these are available when the blueprint is being registered.
from . import api
