from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identify
from resources.user import UserRegister
from resources.item import Item, Itemlist
from db import db
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identify) # /auth -- new endpoint created by JWT
                    # /auth gets a username and password as input and sends it to authenticate function
                    # this then is passed to identify(), final out put is a JWT token which is used to authenticate an entry

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Itemlist, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)