from flask_restful import Resource
from database.models.Delivery import Delivery
from database.models.User import User
from flask import Response, request
from flask_jwt_extended import jwt_required, get_current_user, current_user
from marshmallow import Schema, fields

# TODO: plan end-points and resource needed
# TODO: validate args (marshmallow?)

"""
get list of all deliveries  -   maybe use url args to narrow it down
                                for starter just return all list

Add delivery                -   add delivery to the DB

update delivery status      -   recorde change when delivery is being delivered

cancle/delete delivery      -   need to make sure only the user whom added the delivery can delete it

"""


class DeliverySchema(Schema):
    pass


class AddressSchema(Schema):
    country = fields.Str()
    city = fields.Str()
    street = fields.Str()
    number = fields.Str()
    apartment = fields.Str()
    entrance = fields.Str()


class Deliveries(Resource):
    """
    get by
    """

    def get(self):
        """ :return: json list of all deliveries """
        args = request.args
        deliveries = Delivery.objects(**args).to_json()
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
        user = get_current_user()  # get user object from jwt
        print(type(user))
        body = request.get_json()
        # user = User.objects.get()
        delivery = Delivery(**body, addBy=user, srcAddress=user.address)
        delivery_id = delivery.id
        delivery = delivery.save()
        user.deliveries.append(delivery)
        user.save()
        return {'id': str(delivery.id)}, 200

    """
    update an delivery
    """

    def put(self):
        pass

    def delete(self):
        pass

