from flask import Blueprint
from flask_restful import Api


rewards_blueprint = Blueprint('rewards', __name__)
rewards_api = Api(rewards_blueprint)


# Ensure these are available when the blueprint is being registered.
from . import api
