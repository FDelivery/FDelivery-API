from flask_restful import Resource
from database.models.Delivery import Delivery
from flask import Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.models.User import CourierUser


class DeliveryList(Resource):
    def get(self):
        """
        :return: json list of all deliveries
        """
        deliveries = Delivery.objects().to_json()
        if not deliveries:
            return Response({'error': 'data not found'}, status=400)
        else:
            return Response(deliveries, mimetype="application/json", status=200)


class SpecificDeliver(Resource):
    def get(self, id):
        """
        :return: json of Specific deliver
        """
        deliver = Delivery.objects.get(id=id).to_json()
        return Response(deliver, mimetype="application/json", status=200)

    def put(self, id):
        """
                     update deliver --when its he need to change the status to In Transit\delivered..
                             """
        body = request.get_json()
        Delivery.objects.get(id=id).update(**body)
        return 'done', 200

    def delete(self, id):
        """
               delete deliver from database --when its complete
                       """
        deliver = Delivery.objects.get(id=id)
        deliver.delete()
        return 'done', 200


class couriers(Resource):

    @jwt_required()
    def put(self):
        """
                     update user --when he need to change his VEHICLE or add deliver to history..
                             """
        user_id = get_jwt_identity()
        body = request.get_json()
        user = CourierUser.objects.get(id=user_id).update(**body)
        return 'done', 200

    def get(self):
        """
        :return: just for tests
        """
        user = CourierUser.objects().to_json()
        return Response(user, mimetype="application/json", status=200)
