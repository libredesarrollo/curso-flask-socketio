from flask_login import UserMixin
from werkzeug.security import check_password_hash

from app import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(400))
    name = db.Column(db.String(100))

    def check_password(self, password):
        return check_password_hash(self.password,password)
    