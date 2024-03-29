from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'Store_1',
        'items': [
            {
                'name': 'Item1',
                'price': 10.00
            }
        ]
    }
]


@app.route('/')
def home():
    return 'Welcome to my Flask app'


@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': f'{name} not found'})


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': f'{name} not found'})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    new_item = {
        'name': request_data['name'],
        'price': request_data['price']
    }
    for store in stores:
        if store['name'] == name:
            store['items'].append(new_item)
            return jsonify({'items': store['items']})
    return jsonify({'message': f'{name} not found'})


if __name__ == '__main__':
    app.run(port=5000)
