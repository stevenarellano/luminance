
from .upload import upload_blueprint


def init_routes(app):
    app.register_blueprint(upload_blueprint)
