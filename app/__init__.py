from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://b75abb904531b7:daa70e6e@us-cdbr-east-06.cleardb.net/heroku_7d9b43f40f807f9?reconnect=true"
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

db = SQLAlchemy(app)

from app.controller import routes
