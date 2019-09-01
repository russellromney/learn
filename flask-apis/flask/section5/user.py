import sqlite3
from flask_restful import Resource, reqparse



class UserRegister(Resource):
    parser = reqparse.RequestParser()
    # enforces a single price argument
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help='this field cannot be blank'
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help='this field cannot be blank'
    )

    
    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {'message':'A user with that username already exists'}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'insert into users values (NULL, ?, ?)'
        cursor.execute(query,(data['username'],data['password']))

        connection.commit()
        connection.close()

        return {'message':'User created successfully.'},201