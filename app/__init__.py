from flask_bcrypt import Bcrypt
from .resful import api
from flask import Flask

app = Flask(__name__)


def create_api(debug=False):
    app.config.from_envvar('ENV_FILE_LOCATION')

    from app.routes import initialize_routes
    initialize_routes(api)

    api.init_app(app)
    return app
