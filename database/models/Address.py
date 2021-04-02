from ..db import db


class Address(db.EmbeddedDocument):
    country = db.StringField(requierd=True, defualt='Israel')
    city = db.StringField(requierd=True)
    street = db.StringField(requierd=True)
    number = db.StringField(requierd=True)
    floor = db.StringField()
    apartment = db.StringField()
    entrance = db.StringField()
