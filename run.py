from app import app
from db import db

db.init_app(app)

#執行第一次request的時候才執行的方法
@app.before_first_request
def create_tables():
    db.create_all()