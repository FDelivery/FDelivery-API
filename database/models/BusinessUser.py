from database.db import db


class BusinessUser(db.Document):
    name = db.StringField(required=True)
    primeriePhone = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    # password = db.StringField(required=True, min_length=6)
    # address = db.StringField(required=True)
    # secondaryPhone = db.StringField(required=False)
