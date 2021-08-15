
from app import create_app, socketIO
# TODO: marshmallow validation of IO
# TODO: Generate Swagger


app = create_app(debug=True)


if __name__ == '__main__':
    socketIO.run(app, host='0.0.0.0')
