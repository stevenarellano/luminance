
from flask import Blueprint

upload_blueprint = Blueprint('upload_blueprint', __name__)


@upload_blueprint.route('/upload')
def index():
    return "This is an upload blueprint"
