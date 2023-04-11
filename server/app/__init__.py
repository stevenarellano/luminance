from flask import Flask

from .routes import init_routes
from flask_cors import CORS


app = Flask(__name__)
init_routes(app)
CORS(app)


@app.route('/')
def home():
    return 'Welcome to my Flask app!'
