from flask import Flask,jsonify,request,render_template


app = Flask(__name__)


# post - receive data
# get - send only

# item definition
stores = [
    {
        'name':'My Wonderful Store',
        'items':[
            {
                'name':'My Item',
                'price':15.99
            }
        ]
    },
    {
        'name':'StoreOne',
        'items':[
            {
                'name':'My Item',
                'price':15.99
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

# to create
# post /store data {name}
@app.route('/store',methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name':request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)


# get /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    # iterate over stores
    # if the store name matches, return it
    # if none match, return error message
    for store in stores:
        if store['name']==name:
            return jsonify(store)
    return jsonify({'error':'no store with name {}'.format(name)})

# post /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item',methods=['POST'])
def post_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name']==name:
            item = {
                'name':request_data['name'],
                'price':request_data['price']
            }
            store['items'].append(item)
            return jsonify({'item':item})
    return jsonify({'error':'no store with name {}'.format(name)})


# get /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})

# get /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify({'items':store['items']})
    return jsonify({'error':'no store with name {}'.format(name)})

app.run(port=5000)

