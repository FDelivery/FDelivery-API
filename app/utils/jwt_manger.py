from flask_jwt_extended import JWTManager
from app.database.models.User import User  # avoid circular import

jwt = JWTManager()


def initialize_jwt(app):
    jwt.init_app(app)


# Register a callback function that takes whatever object is passed in as the
# identity when creating JWT and converts it to a UUID JSON serialize format.
@jwt.user_identity_loader
def user_identity_lookup(user: User) -> str:
    return str(user.id)


# Register a callback function that loads a user from your database whenever
# a protected route is accessed. This should return User object on a
# successful lookup, or None if the lookup failed for any reason (for example
# if the user has been deleted from the database).
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data) -> User:
    identity = jwt_data["sub"]
    return User.objects.get(id=identity)
