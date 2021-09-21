from flask import Flask, require, jsonify
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:sVChIQwU.wqjqsM7@localhost/tellme"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(db)

#-------------------------SECURITY-------------------------

#-------------------------MODELS-------------------------

#-------------------------ROUTES-------------------------

#-------------------------END-------------------------

if __name__ == "__main__":
    app.run(debug=True)