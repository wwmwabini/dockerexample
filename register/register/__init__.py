import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

DB_HOST = os.environ.get('DB_HOST')
DB_PASS = os.environ.get('DB_PASS')

DB_CONNECTION_STRING = "mysql+pymysql://dockerexample:"+DB_PASS+"@"+DB_HOST+":3306/dockerexample"
app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONNECTION_STRING
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.config['SECRET_KEY']='QjgVdqYKe16f52MGxaZSCzwh9kElUA7vuRoPFtObD0'

db = SQLAlchemy(app)

from register import routes