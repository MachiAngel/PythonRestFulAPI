import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))  # 沒加逗點會認為 (5+8)之類的，參數必須是turple
        row = result.fetchone()  # get frist row
        if row:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))  # 沒加逗點會認為 (5+8)之類的，參數必須是turple
        row = result.fetchone()  # get frist row
        if row:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user


class UserRegister(Resource):
    """
    進來這個class先檢查傳入的參數 
    """
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type = str,
        required = True,
        help = "This field cannot be blank"
    )
    parser.add_argument('password',
        type = str,
        required = True,
        help = "This field cannot be blank"
    )

    def post(self):
        # Get data from the payload
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(**data) # data['username'], data['password']
        user.save_to_db()
        return {"message": "User created successfully."}, 201
