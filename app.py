from flask import Flask, request, Response
from database.db import initialize_db
# from database.models import Delivery
# from database.models import BusinessUser
from resources.businessUser import businessUsers


app = Flask(__name__)



app.config['MONGODB_SETTINGS'] = {
    'host' : 'mongodb://localhost/api'
}

initialize_db(app)




# @app.route('/api/deliveries/<int:index>', methods=['GET'])
# def get_movie(index):
#     return jsonify(movies[index])



# @app.route('api/deliveries/<id>', methods=['PUT'])
# def update_movie(index):
#     body = request.get_json()
#     Delivery.objects.get(id=id).update(**body)
#     return 'Updated Delivery', 200

app.register_blueprint(businessUsers)

if __name__ == '__main__':
    app.run(debug=True)



