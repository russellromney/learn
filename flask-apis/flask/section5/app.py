from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from user import UserRegister
from item import Item,ItemList
from security import authenticate,identity

app = Flask(__name__)
app.secret_key = 'russell'
api = Api(app)
jwt = JWT(app, authenticate, identity) # /auth
        

api.add_resource(Item, '/item/<string:name>') # http://localhost:5000/item/<name>
api.add_resource(ItemList,'/items') # http://localhost:5000/items
api.add_resource(UserRegister,'/register')

# this is so importing does not run this
if __name__=='__main__':
    app.run(port=5000, debug=True)