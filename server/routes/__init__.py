from flask import Blueprint
from .api.taskroute import task_api  # Import the task_api Blueprint from the api folder

api_blueprint = Blueprint('api', __name__)

# Register the task_api Blueprint under the '/api' prefix
api_blueprint.register_blueprint(task_api, url_prefix='/api')