from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message':'Store not found'}, 404

    def post(self,name):
        if StoreModel.find_by_name(name):
            return {'message':'Store already exists with that name'}

        store = StoreModel(name)
        try:
            store.save_to_db()
            return store.json()
        except:
            return {'message':'An error occured while creating the store'}, 500
    
    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {"messaged":'Successfully deleted store.'}


class StoreList(Resource):
    def get(self):
        return {'stores':[ x.json() for x in StoreModel.find_all() ]}