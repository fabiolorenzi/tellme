from flask import Flask, require, jsonify
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:sVChIQwU.wqjqsM7@localhost/tellme"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(db)

#-------------------------MODELS-------------------------

#-------------------------ROUTES-------------------------

#-------------------------END-------------------------

if __name__ == "__main__":
    app.run(debug=True)