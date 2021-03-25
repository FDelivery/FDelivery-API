@app.route('/api/deliveries', methods=['GET'])
def get_deliveries():
    deliveries = Delivery.objects().to_json()
    if not deliveries:
        return  Response({'error': 'data not found'}, status=400)
    else:
        return Response(deliveries, mimetype="application/json", status=200)

@app.route('/api/deliveries/', methods=['POST'])
def method_name():
   pass

@app.route('/api/deliveries/<id>',methods=['GET'])  
def get_delivery():
    delivery = Delivery.objects(id=id).to_json();
    return Response(delivery, mimetype="application/json", status=200)


@app.route('/api/deliveries/<id>', methods=['POST'])
def add_deliveries():
    body = request.get_json()
    delivery = Delivery(**body).save()
    id = delivery.id
    return {'id: str(id)'}, 200

@app.route('/api/deliveries/<id>', methods=['DELETE'])
def delete_movie(index):
    Delivery.objects(id=id).DELETE()
    return '', 200
    