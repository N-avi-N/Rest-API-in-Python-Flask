
from flask import Flask, request, render_template, jsonify #converts a dictionary to a string/json

app = Flask(__name__)

stores = [
    {
        'name': 'My Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

# POST = to receive data
# get = to send data only

# POST /store data:{name}
# creates a store information
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
# retrieves a store information
@app.route('/store/<string:name>') # 'http//127.0.0.1:5000/store/store_name
def get_store(name):
    # iterate over stores
    # return store if it matches
    # if none match return error
    for store_name in stores:
        if store_name['name'] == name:
            return jsonify(store_name)
    return jsonify({'message': 'store not found'})


# GET /store to get all the stores list
@app.route('/store') # 'http//127.0.0.1:5000/store/store_name
def get_stores():
    return jsonify({'stores': stores})      # our store variable is a list we need to convert it to a dictionary and then it can be converted to a json

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

    pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item') # 'http//127.0.0.1:5000/store/store_name
def get_item_in_store(name):
    for store_name in stores:
        if store_name['name'] == name:
            return jsonify({'items': store_name['items']})
    return jsonify({'message': 'item not found'})

app.run(port=5000)