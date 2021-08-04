from flask_mongoengine import MongoEngine

# initialization of Flask-MongoEngine.
db = MongoEngine()


# initialize the database connection to the MongoDB
# with given app parameter
def initialize_db(app):
    db.init_app(app)


# def populate_db():
#     users = [
#         {"firstName": "Raphael",
#          "lastName": "Gozlan",
#          "email": "Raphael@gmail.com",
#          "password": "hey",
#          "primaryPhone": "058 497 5977",
#          "role": "Admin",
#          "address": {
#                  "country": "USA",
#                  "street": "Swartze",
#                  "number": "3b",
#                  "city": "ranna"
#          }},
#         {},
#         {}
#     ]
