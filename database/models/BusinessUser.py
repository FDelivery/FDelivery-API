from database.db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class BusinessUser(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    # name = db.StringField(required=True)
    # address = db.StringField(required=True)
    # primeriePhone = db.StringField(required=True)
    # secondaryPhone = db.StringField(required=False)


    '''
    Generates a password hash using bcrypt. 
    Specifying rounds sets the log_rounds parameter of bcrypt.gensalt() which determines the complexity of the salt. 
    12 is the default value. 
    Specifying prefix sets the prefix parameter of bcrypt.gensalt() which determines the version of the algorithm used to create the hash.
    '''
    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    '''
    Tests a password hash against a candidate password. 
    The candidate password is first hashed and then subsequently compared in constant time to the existing hash. 
    This will either return True or False.
    '''
    def check_password(self, password:str):
        return check_password_hash(self.password, password)

