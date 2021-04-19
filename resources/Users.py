from flask import Response
from flask_restful import Resource
from database.models.User import User


# TODO: add option to find user by email
# TODO: add option to change password - next version not important right now

class Users(Resource):
    """
    This class provide Users information endpoint
    """

    def get(self, user_id: str):
        print('hey')
        """
        :param user_id: string representing _id user
        :return: User serializable object

        :exception 404 if no user with _id = user_id
        """
        user = User.objects.get_or_404(id=user_id).to_json()
        return Response(user, mimetype='application/json', status=200)
