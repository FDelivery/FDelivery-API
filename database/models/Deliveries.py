from ..db import db

'''
    This class is o model for
    Deliveries collection in MongoDB    
'''


class Delivery(db.Document):
    status = db.StringField()
