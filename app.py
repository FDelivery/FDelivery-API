from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
# from flask_marshmallow import Marshmallow
from resources.routes import initialize_routes


app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')

api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
# ma = Marshmallow(app)

# app.config['MONGODB_SETTINGS'] = {
#     'host': 'mongodb://localhost/production'
# }

initialize_db(app)
initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=True)
