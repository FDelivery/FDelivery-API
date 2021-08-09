
from flask import Response, request, jsonify
from flask_restful import Resource
from database.models.User import User


# TODO: add option to change password -
#   next version not important right now

class Users(Resource):
    """ For a unique user resource """

    def get(self, user_id: str):
        user = User.objects(id=user_id).first_or_404(message='No such user').to_json()
        return user, 200


    def put(self, user_id: str):
        """
        function for update user object data
        :param user_id: UUID of user object
        """
        pass


class UsersList(Resource):
    """ This class provide Users information """

    def get(self):
        """
        :return: User serialize object
        :exception 404 if no user with _id = user_id
        """
        args = request.args.to_dict()  # get params for url query arguments
        user = User.objects(**args).to_json()
        return Response(user, mimetype='application/json', status=200)


    def post(self):
        email = request.json.get('email')  # get email from post
        password = request.json.get('password')  # get password from post
        user = User.objects.get(email=email)  # retrieve user object from DB

        return str(user.id), 200
        # return str(user.id), 200

        return 'error: Email or password invalid', 401