# FDelivery api
A flask restful API for our Business and Couriers application.

The API allows communication between businesses looking for delivery services to couriers looking to do accept those deliveries.  
Using real-time communication over SocketIO to allow synchronization between all clients running over the Android application, the API has multiple REST Service Endpoints to manganese resources states.  
The API uses JWT for authorization and authentication, allowing scalability over sessions because the token is on the client side.




## Technologies used
* **[Python3](https://www.python.org/downloads/)** - A programming language that lets you work more quickly (The universe loves speed!).
* **[Flask](flask.pocoo.org/)** - A microframework for Python based on Werkzeug, Jinja 2 and good intentions
* **[Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/index.html)** -  A Flask extension that adds support for building REST APIs that works with your existing ORM/libraries.
* **[Pipenv](https://pipenv.pypa.io/en/latest/)** - A tool to create isolated virtual environments
* **[MongoDB](https://www.mongodb.com/)** – MongoDB is a source-available cross-platform document-oriented database program.
* **[MongoEngine](https://www.python.org/downloads/)** - MongoEngine is an Object-Document Mapper, written in Python for working with MongoDB.
* **[Socket.IO](https://www.python.org/downloads/)** - Socket.IO enables real-time, bidirectional and event-based communication.



## Installation / Usage
* If you wish to run your own build, first ensure you have python3 globally installed in your computer. If not, you can get python3 [here](https://www.python.org).
* After this, ensure you have installed virtualenv globally as well. If not, run this:
    ```
        $ pip install pipenv
    ```
* Git clone this repo to your PC
    ```
        $ git clone git@github.com:gitgik/flask-rest-api.git
    ```


* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```
        $ cd flask-rest-api
        ```

    2. Create and fire up your virtual environment in python3:
        ```
        $ pipenv install autoenv
        ```

* #### Environment Variables
    Create a .env file and add the following:

    ```
        $ JWT_SECRET_KEY = 'VERY-SECRET'
        $ MONGODB_HOST = 'mongodb://localhost:27017/app'
    ```

    Save the file. CD out of the directory and back in. `Autoenv` will automagically set the variables.
    We've now kept sensitive info from the outside world! 😄

* #### Install your requirements
    ```
    $ pipenv install
    ```


* #### Running It
    On your terminal, run the server using this one simple command:
    ```
    (venv)$ flask run
    ```
    You can now access the app on your local browser by using
    ```
    http://localhost:5000/
    ```
    Or test creating deliveries using Postman