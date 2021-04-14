from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from flask_bcrypt import Bcrypt

# from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')

api = Api(app)
bcrypt = Bcrypt(app)
# ma = Marshmallow(app)

from resources.Auth.jwt_manger import initialize_jwt

initialize_jwt(app)
initialize_db(app)

from resources.routes import initialize_routes

initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=True)
