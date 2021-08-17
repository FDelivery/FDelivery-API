import datetime

from .Address import Address
from ..db import db

_STATUS_ENUM = ('COURIER_SEARCHING',
                'COURIER_ACCEPTED',
                'WAITING_PICKUP',
                'IN_TRANSIT',
                'DELIVERED',
                'EXCEPTION')


class Delivery(db.Document):
    """ Class is a model for Deliveries collection """
    destAddress = db.EmbeddedDocumentField(Address)
    clientPhone = db.StringField()
    clientName = db.StringField()
    Note = db.StringField()
    Time = db.StringField()
    deliveredDate = db.StringField()
    pickedDate = db.DateTimeField()
    price = db.FloatField(min_value=0)
    AddedBy = db.StringField()
    businessRef = db.ReferenceField('BusinessUser', reverse_delete_rule=db.CASCADE)
    creationDate = db.DateTimeField(default=datetime.datetime.utcnow())
    srcAddress = db.EmbeddedDocumentField(Address)
    status = db.StringField(choices=_STATUS_ENUM)
    courierRef = db.ReferenceField('CourierUser', reverse_delete_rule=db.CASCADE)
