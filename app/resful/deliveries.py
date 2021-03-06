from bson import ObjectId

from flask_restful import Resource
from app.socketio import socketio
from app.database.models.Delivery import Delivery
from flask import request
from flask_jwt_extended import jwt_required, get_current_user
from app.database.models.User import User

# TODO: plan end-points and resource needed
# TODO: validate args (marshmallow?)


"""
cancel/delete delivery - need to make sure only the user whom added the delivery can delete it
"""


class Deliveries(Resource):

    def get(self, delivery_id: str):
        delivery = Delivery.objects(id=delivery_id).first_or_404('Delivery not found').to_json()
        return delivery, 200

    @jwt_required()
    def put(self, delivery_id: str):
        body = request.get_json()
        print(body)
        delivery = Delivery.objects(id=delivery_id).first_or_404('Delivery not found')
        if body.get('status') == 'COURIER_ACCEPTED':
            user = get_current_user()
            if Delivery.objects(courierRef=user.id, status='COURIER_ACCEPTED'):
                return 'you already registered for a delivery', 400
            delivery.update(courierRef=user.id)
            user.deliveriesHistory.append(delivery)

            # inform couriers that certain delivery is taken by other courier
            socketio.emit("delivery_accepted_for_courier", "1")

            # inform delivery owner(business user) that some courier chose to take his delivery
            socketio.emit("delivery_accepted", "", to=delivery.AddedBy)
        delivery.update(**body)
        return 204

    @jwt_required()
    def delete(self, delivery_id: str):
        """ delete an delivery """
        user = get_current_user()
        update_qry = {"$pull": {"deliveriesRef": ObjectId(delivery_id)}}
        User.objects(id=user.id).update(__raw__=update_qry)
        Delivery.objects(id=delivery_id).first_or_404('Delivery not found').delete()

        return 200


class DeliveriesList(Resource):
    def get(self):
        """ :return: json list of all deliveriesRef query from url query params"""
        args = request.args.to_dict()
        deliveries = Delivery.objects(**args)
        if not deliveries:
            return 'error: data not found', 400
        dell = []
        for d in deliveries:
            dell.append(d.to_json())
        return dell, 200

    @jwt_required()
    def post(self):
        """
        post a delivery to DB
        :return: id of new post delivery
        """

        user = get_current_user()  # get user object from jwt
        body = request.get_json()
        print(body)
        delivery = Delivery(**body, AddedBy=str(user.id), srcAddress=user.address)
        delivery = delivery.save()
        user.deliveriesRef.append(delivery)
        user.save()

        # inform couriers that new delivery has been posted
        socketio.emit("delivery_posted", delivery.to_json())

        return str(delivery.id), 200
