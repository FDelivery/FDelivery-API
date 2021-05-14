from flask import Response
from flask_restful import Resource, request
from database.models.User import User


# TODO: add option to find user by email
# TODO: add option to change password - next version not important right now

class Users(Resource):
    """ For a unique user resource """

    def get(self, user_id: str) -> User:
        user = User.objects(id=user_id).first_or_404(message='No such user').to_json()
        return Response(user, mimetype='application/json', status=200)


class UsersList(Resource):
    """
    This class provide Users information
    """

    def get(self):
        """
        :return: User serialize object
        :exception 404 if no user with _id = user_id
        """
        args = request.args.to_dict()  # get params for url query arguments
        user = User.objects(**args).to_json()
        return Response(user, mimetype='application/json', status=200)

    def post(self):
        pass
