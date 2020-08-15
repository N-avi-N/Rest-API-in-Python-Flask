from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identify
from user import UserRegister
from item import Item, Itemlist

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)


jwt = JWT(app, authenticate, identify) # /auth -- new endpoint created by JWT
                    # /auth gets a username and password as input and sends it to authenticate function
                    # this then is passed to identify(), final out put is a JWT token which is used to authenticate an entry

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Itemlist, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)