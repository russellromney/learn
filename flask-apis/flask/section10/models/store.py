from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(80))

    # this is many-to-one relationship - so this is a dynamic list of items
    # lazy='dynamic' means the items is lazily interpreted, need to reference with self.items.all()
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self,name):
        self.name = name

    def json(self):
        return {
            'name':self.name,
            'id':self.id,
            'items':[item.json() for item in self.items.all()]
        }

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    # upsert the item to the database
    def save_to_db(self):
        # this adds this object to the database
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()