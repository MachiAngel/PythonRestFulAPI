import os

from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.item import Item, ItemList
from resources.user import UserRegister
from security import authenticate, identity
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') #'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)


jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores/')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items/')
api.add_resource(UserRegister, '/register/')


"""
只有執行此程式檔案 __main__ 才執行此程式碼
要是import之類的  不會執行
"""
if __name__ == '__main__':
    #寫在這邊防止循環 cycle import  -> db import model model import db
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True)
