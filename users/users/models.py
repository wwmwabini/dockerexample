from users import db, app
from datetime import datetime

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(63), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    datecaptured = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
