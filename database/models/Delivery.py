import datetime

from .Address import Address
from ..db import db

_STATUS_ENUM = ('COURIER_SEARCHING'
                'COURIER_ACCEPTED',
                'WAITING_PICKUP',
                'IN_TRANSIT',
                'DELIVERED',
                'EXCEPTION')


class Delivery(db.Document):
    """ Class is a model for Deliveries collection """
    businessRef = db.ReferenceField('BusinessUser', reverse_delete_rule=db.CASCADE)
    creationDate = db.DateTimeField(default=datetime.datetime.utcnow())
    pickedDate = db.DateTimeField()
    deliveredDate = db.DateTimeField()
    price = db.FloatField(min_value=0)
    srcAddress = db.EmbeddedDocumentField(Address)
    destAddress = db.EmbeddedDocumentField(Address)
    status = db.StringField(choices=_STATUS_ENUM)
    courierRef = db.ReferenceField('CourierUser', reverse_delete_rule=db.CASCADE)
