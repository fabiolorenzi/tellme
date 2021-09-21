from flask import Flask, require, jsonify
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet
from datetime import datetime

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:sVChIQwU.wqjqsM7@localhost/tellme"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(db)

#-------------------------MODELS-------------------------

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25))
    name = db.Column(db.String(25))
    surname = db.Column(db.String(30))
    birthday = db.Column(db.Date)
    subscribed_since = db.Column(db.Date)
    city = db.Column(db.String(30))
    email = db.Column(db.String(40))
    password = db.Column(db.String(20))

    def __init__(self, username, name, surname, birthday, subscribed_since, city, email, password):
        self.username = username
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.subscribed_since = subscribed_since
        self.city = city
        self.email = email
        self.password = password

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "name", "surname", "birthday", "subscribed_since", "city", "email", "password")

user_schema = UserSchema()
users_schema = UserSchema(many=True)

#-------------------------ROUTES-------------------------

#-------------------------END-------------------------

if __name__ == "__main__":
    app.run(debug=True)