from flask import Flask, request, Response, jsonify
from database.models.BusinessUser import BusinessUser
from flask.blueprints import Blueprint

businessUsers = Blueprint('users', __name__)


@businessUsers.route('/api/users', methods=['GET'])
def get_users():
    businessUsers = BusinessUser.objects().to_json()
    if not businessUsers:
        return  {'error': 'data not found'}, 400
    else:
        return businessUsers, 200

@businessUsers.route('/api/users', methods=['POST'])
def add_user():
   body = request.get_json()
   user = BusinessUser(**body).save()
   return jsonify(user), 200