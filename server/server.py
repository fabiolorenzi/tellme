from flask import Flask, request, jsonify
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



class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(25))
    date = db.Column(db.Date)
    message = db.Column(db.String(1000))

    def __init__(self, user, date, message):
        self.user = user
        self.date = date
        self.message = message

class PostSchema(ma.Schema):
    class Meta:
        fields = ("id", "user", "date", "message")

post_schema = PostSchema()
posts_schema = PostSchema(many=True)

#-------------------------SECURITY-------------------------

file = open("key.key", "rb")
key = file.read()
file.close()
f = Fernet(key)

#-------------------------ROUTES-------------------------

@app.route("/api/users", methods = ["GET"])
def getAllUsers():
    users = Users.query.all()
    results = users_schema.dump(users)
    return jsonify(results)

@app.route("/api/users/<id>", methods = ["GET"])
def getUserById(id):
    user = Users.query.get(id)
    return user_schema.jsonify(user)

@app.route("/api/users/<id>/<passW>", methods = ["GET"])
def loginUser(id, passW):
    user = Users.query.get(id)
    bytePssw = bytes(user.password, encoding="utf-8")
    password = f.decrypt(bytePssw)
    return password

@app.route("/api/users", methods = ["POST"])
def addUser():
    username = request.json["username"]
    name = request.json["name"]
    surname = request.json["surname"]
    birthday = request.json["birthday"]
    subscribed_since = datetime.now()
    city = request.json["city"]
    email = request.json["email"]
    prePassword = request.json["password"]

    bytePassword = prePassword.encode()
    password = f.encrypt(bytePassword)

    users = Users(username, name, surname, birthday, subscribed_since, city, email, password)
    db.session.add(users)
    db.session.commit()
    return user_schema.jsonify(users)

#-------------------------END-------------------------

if __name__ == "__main__":
    app.run(debug=True)