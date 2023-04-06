from flask import Flask

from .routes import init_routes


def luminance_app():
    app = Flask(__name__)
    init_routes(app)

    @app.route('/')
    def home():
        return 'Welcome to my Flask app!'

    return app
