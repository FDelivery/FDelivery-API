from datetime import datetime as dt
from werkzeug.security import check_password_hash, generate_password_hash
from ..db import db

_USER_ROLE = ('ADMIN', 'BUSINESS', 'COURIER')
_VEHICLE_NAME = ('BICYCLE', 'CAR', 'MOTORCYCLE')


class User(db.Document):
    """
    Parent class of User all user types inherent from this class
    This allows for more convenient and efficient retrieval of related documents
    """
    firstName = db.StringField(max_length=50, required=True)
    lastName = db.StringField(max_length=50, required=True)
    email = db.EmailField(max_length=50, required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    primaryPhone = db.StringField(required=True)
    secondaryPhone = db.StringField()
    role = db.StringField(required=True, choices=_USER_ROLE)
    creationDate = db.DateTimeField(default=dt.utcnow)

    meta = {'allow_inheritance': True}

    def hash_password(self):
        # noinspection SpellCheckingInspection
        """
        Generates a password hash using bcrypt. Specifying rounds sets the log_rounds parameter of bcrypt.gensalt()
        which determines the complexity of the salt. 12 is the default value. Specifying prefix sets the prefix
        parameter of bcrypt.gensalt() which determines the version of the algorithm used to create the hash.
        """
        self.password = generate_password_hash(self.password)

    def check_password(self, password: str):
        """
        Tests a password hash against a candidate password.
        The candidate password is first hashed and then subsequently compared in constant time to the existing hash.
        This will either return True or False.
        """
        return check_password_hash(self.password, password)


class BusinessUser(User):
    """ Business user class model """
    from .Address import Address  # Avoid circular import
    businessName = db.StringField(required=True)
    address = db.EmbeddedDocumentField(Address)
    deliveriesRef = db.ListField(db.ReferenceField('Delivery'), reverse_delete_rule=db.PULL)


class CourierUser(User):
    """ Courier user class model """
    vehicle = db.StringField(required=True, choices=_VEHICLE_NAME)
    currentDelivery = db.StringField()
    deliveriesHistory = db.ListField(db.ReferenceField(
        'Delivery'), reverse_delete_rule=db.PULL)
