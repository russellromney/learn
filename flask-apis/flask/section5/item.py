from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3


class Item(Resource):

    parser = reqparse.RequestParser()
    # enforces a single price argument
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help='this field cannot be blank'
    )
    
    @jwt_required()
    def get(self,name):
        item = Item.find_by_name(name)
        if item:
            return item
        return {'message':'Item not found'},404

    @classmethod
    def find_by_name(cls,name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = 'select * from items where name=?'
        result = cursor.execute(query,(name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item':{'name':row[0],'price':row[1]}}
        


    def post(self,name):
        if Item.find_by_name(name):
            return {'message':'item already exists with name {}'.format(name)}, 400 # request problem, not server problem
        
        item = Item.parser.parse_args()
        item = {
            'name':name,
            'price':item['price']
        }
        try:
            Item.insert(item)
        except:
            {'message':'An error occured inserting the item'}, 500 # internal server error
        return item, 201

    @classmethod
    def insert(cls,item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = 'insert into items values (?, ?)'
        cursor.execute(query,(item['name'],item['price']))
        
        connection.commit()
        connection.close()

    def delete(self,name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = 'delete from items where name=?'
        cursor.execute(query,(name,))
        
        connection.commit()
        connection.close()

        return {'message':'item deleted'}


    def put(self,name):
        data = Item.parser.parse_args()
        
        item = Item.find_by_name(name)
        updated_item = {'name':name,'price':data['price']}
        
        # if item didn't exist already
        if item is None:
            try:
                Item.insert(updated_item)
            except:
                return {"message":'An error occurred inserting the item'}, 500
        # if item already exists
        else:
            try:
                Item.update(updated_item)
            except:
                return {"message":'An error occurred updating the item'}, 500
        return updated_item

    @classmethod
    def update(cls,item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = 'update items set price=? where name=?'
        cursor.execute(query, ( item['price'], item['name'] ))
        
        connection.commit()
        connection.close()


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = 'select * from items'
        result = cursor.execute(query)

        items = [{'name':row[0],'price':row[1]} for row in result]

        connection.commit()
        connection.close()

        return {"items":items}
