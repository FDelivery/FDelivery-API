from flask_jwt_extended import JWTManager

jwt = JWTManager()


def initialize_jwt(app):
    jwt.init_app(app)


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    from database.models.User import User
    identity = jwt_data["sub"]
    return User.objects.get(id=identity)
