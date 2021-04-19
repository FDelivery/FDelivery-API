from flask_restful import Resource
from database.models.Delivery import Delivery
from database.models.BusinessUser import BusinessUser
from flask import Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity, current_user
from flask_user import login_required


# TODO: plan end-points and resource needed
# TODO: validate args (marshmallow?)

"""
get list of all deliveries  -   maybe use url args to narrow it down
                                for starter just return all list
                                
Add delivery                -   add delivery to the DB

update delivery status      -   recorde change when delivery is being delivered

cancle/delete delivery      -   need to make sure only the user whom added the delivery can delete it 

"""

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
        print("check")
        """
        post a delivery to DB
        :return: id of new post delivery
        """
        print(current_user.id, current_user.firstName)
        user_id = get_jwt_identity()
        body = request.get_json()
        user = BusinessUser.objects.get(id=user_id)
        delivery = Delivery(**body, addBy=user)
        delivery_id = delivery.id
        delivery = delivery.save()
        user.deliveries.append(delivery)
        user.save()
        return {'id': str(delivery.id)}, 200
