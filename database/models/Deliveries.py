from ..db import db

'''
    This class is o model for
    Deliveries collaction in MongoDB    
'''
class Delivery(db.Document):
    status = db.StringField()
