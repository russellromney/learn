from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    jwt_required,
    jwt_optional,
    fresh_jwt_required,
    get_jwt_claims,
    get_jwt_identity,
)

from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    # enforces a single price argument
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help='this field cannot be blank'
    )
    parser.add_argument('store_id',
        type=int,
        required=True,
        help='Every item needs a store id'
    )
    
    @jwt_required
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message':'Item not found'}, 404

    @fresh_jwt_required
    def post(self,name):
        if ItemModel.find_by_name(name):
            return {'message':'item already exists with name {}'.format(name)}, 400 # request problem, not server problem
        
        data = Item.parser.parse_args()
        
        item = ItemModel(name,**data)

        try:
            item.save_to_db()
        except BaseException as e:
            print(e)
            return {'message':'An error occured inserting the item'}, 500 # internal server error
        return item.json(), 201

    @jwt_required
    def delete(self,name):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message':'Admin privilege required'}, 401
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message':'item deleted'}, 200

    def put(self,name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name,**data)
        else:
            item.price = data['price']
            item.sotre_id = data['store_id']
        
        item.save_to_db()

        return item.json()


class ItemList(Resource):
    @jwt_optional
    def get(self):
        user_id = get_jwt_identity() # returns a user if logged in, or None
        items = [x.json() for x in ItemModel.find_all()]
        if user_id:
            return {'items':items},200
        return {
            'items':[item['name'] for item in items],
            'message':'More data available after login'
        }, 200

