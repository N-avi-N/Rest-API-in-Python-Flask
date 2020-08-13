from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identify

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)


jwt = JWT(app, authenticate, identify) # /auth -- new endpoint created by JWT
                    # /auth gets a username and password as input and sends it to authenticate function
                    # this then is passed to identify(), final out put is a JWT token which is used to authenticate an entry

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='this field cannot be left blank')

    @jwt_required() # authentication before we can call the get function
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'Item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists".format(name)}, 400

        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['names'] != name, items))
        return {'message': 'item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)

        # if item not in list create an entry, else update the existing entry
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class Itemlist(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Itemlist, '/items')

app.run(port=5000, debug=True)