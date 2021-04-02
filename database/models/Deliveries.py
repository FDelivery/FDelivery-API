from ..db import db
from database.models.Address import Address
from datetime import datetime

'''
    This class is a model for
    Deliveries collection in MongoDB    
'''

STATUS_ENUM = (('WD', 'Waiting Delivery'),
               ('IR', 'Info Received'),
               ('IT', 'In Transit Delivery'),
               ('EX', 'Exception'),
               ('DL', 'Delivered'))


class Delivery(db.Document):
    createdAt = db.DateTimeField(defualt=datetime.utcnow())
    pickupAt = db.DateTimeField()
    deliveredAt = db.DateTimeField()
    price = db.FloatField(min_value=0)
    srcAddress = db.EmbeddedDocumentField(Address)
    destAddress = db.EmbeddedDocumentField(Address)
    status = db.StringField(choices=STATUS_ENUM)
    delivererID = db.StringField()
