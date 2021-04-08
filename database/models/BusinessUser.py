from mongoengine import PULL, CASCADE

from ..db import db
from .Address import Address
from .User import User


class BusinessUser(User):
    businessName = db.StringField()
    address = db.EmbeddedDocumentField(Address)
    deliveries = db.ListField(db.ReferenceField('Delivery'), reverse_delete_rule=db.PULL)

