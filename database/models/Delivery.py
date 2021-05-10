import datetime

from .Address import Address
from ..db import db

STATUS_ENUM = (('WP', 'Waiting Pickup'),
               ('IR', 'Info Received'),
               ('IT', 'In Transit'),
               ('DL', 'Delivered'),
               ('EX', 'Exception'))


class Delivery(db.Document):
    """
        This class is a model for
        Deliveries collection in MongoDB
    """
    addBy = db.ReferenceField('BusinessUser', reverse_delete_rule=db.CASCADE)
    createdAt = db.DateTimeField(default=datetime.datetime.utcnow())
    pickupAt = db.DateTimeField()
    deliveredAt = db.DateTimeField()
    price = db.FloatField(min_value=0)
    srcAddress = db.EmbeddedDocumentField(Address)
    destAddress = db.EmbeddedDocumentField(Address)
    status = db.StringField(choices=STATUS_ENUM)
    courierID = db.StringField()  # can be  mongo _idObject or reference
