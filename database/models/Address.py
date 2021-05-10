from ..db import db


class Address(db.EmbeddedDocument):
    city = db.StringField(required=True)
    street = db.StringField(required=True)
    number = db.StringField(required=True)
    floor = db.StringField()
    apartment = db.StringField()
    entrance = db.StringField()
