from ..db import db
from .User import User

VEHICLE_NAME = ('Bicycle', 'Car', 'motorcycle')


class CourierUser(User):
    vehicle = db.StringField(choices=VEHICLE_NAME)
    myDeliverNow = db.StringField()
    deliveriesHistory = db.ListField(db.StringField())
