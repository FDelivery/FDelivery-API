from app.database import db


# initialize the database connection to the MongoDB
# with given app parameter
def initialize_db(app):
    db.init_app(app)
