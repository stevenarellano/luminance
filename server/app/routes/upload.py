from flask import Blueprint, request, jsonify

from ..llm import CurriculumList, get_curriculum

upload_blueprint = Blueprint('upload_blueprint', __name__)


@upload_blueprint.route('/upload')
def index():
    topic = request.args.get('topic', default=None)
    if not topic:
        return jsonify({"error": "Missing 'topic' query parameter"}), 400

    curriculum_list: CurriculumList = get_curriculum(topic)
    return jsonify(curriculum_list)
