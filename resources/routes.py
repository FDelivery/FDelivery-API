from .Auth.businessUserAuth import *
from .DeliveryLogic.deliveries import Deliveries


def initialize_routes(api):
    api.add_resource(BusinessUserRegisterApi, '/api/business/auth/register/')
    api.add_resource(BusinessUserLoginApi, '/api/business/auth/login/')

    api.add_resource(Deliveries, '/api/deliveriesLogic/deliveries/')
