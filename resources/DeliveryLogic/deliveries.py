from flask_restful import Resource
from database.models.Delivery import Delivery
from database.models.BusinessUser import BusinessUser
from flask import Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity


# TODO: validate args (marshmallow?)

class Deliveries(Resource):
    def get(self):
        """
        :return: json list of all deliveries
        """
        deliveries = Delivery.objects().to_json()
        if not deliveries:
            return Response({'error': 'data not found'}, status=400)
        else:
            return Response(deliveries, mimetype="application/json", status=200)

    @jwt_required()
    def post(self):
        """
        post a delivery to DB
        :return: id of new post delivery
        """
        user_id = get_jwt_identity()
        body = request.get_json()
        user = BusinessUser.objects.get(id=user_id)
        delivery = Delivery(**body, addBy=user)
        delivery_id = delivery.id
        user.update(push_deliveries=delivery)
        delivery.save()
        return {'id': str(delivery_id)}, 200
