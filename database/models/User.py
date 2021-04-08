from ..db import db
from datetime import datetime as dt

from flask_bcrypt import generate_password_hash, check_password_hash

USER_ROLE = ('Admin', 'Business', 'Courier')


class User(db.Document):
    """
    Parent class of User all user types inherent from this class
    This allows for more convenient and efficient retrieval of related documents
    """
    firstName = db.StringField(max_length=50, required=True)
    lastName = db.StringField(max_length=50, required=True)
    email = db.EmailField(max_length=50, required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    primaryPhone = db.StringField(required=True, unique_with='primaryPhone')
    secondaryPhone = db.StringField()
    role = db.StringField(required=True, choices=USER_ROLE)
    createdAt = db.DateTimeField(defualt=dt.utcnow())

    meta = {'allow_inheritance': True}

    def hash_password(self):
        """
        Generates a password hash using bcrypt.
        Specifying rounds sets the log_rounds parameter of bcrypt.gensalt() which determines the complexity of the salt.
        12 is the default value.
        Specifying prefix sets the prefix parameter of bcrypt.gensalt() which determines the version of the algorithm used to create the hash.
        """
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password: str):
        """
        Tests a password hash against a candidate password.
        The candidate password is first hashed and then subsequently compared in constant time to the existing hash.
        This will either return True or False.
        """
        return check_password_hash(self.password, password)