from flask_mongoengine import MongoEngine

# initialization of Flask-MongoEngine.
db = MongoEngine()


# initialize the database connection to the MongoDB
# with given app parameter
def initialize_db(app):
    db.init_app(app)
