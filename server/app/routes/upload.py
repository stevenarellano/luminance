from flask import Blueprint

from ..llm import create_llm

upload_blueprint = Blueprint('upload_blueprint', __name__)


@upload_blueprint.route('/upload')
def index():
    return 'Upload'
