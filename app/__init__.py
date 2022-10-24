from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy


'''
## Gambiarra pra funcionar nos pc lab
import pymysql
from requests import Session
pymysql.install_as_MySQLdb()
'''

app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
#app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://root:abrl0404@127.0.0.1/musicate"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://tftuhkeidvlfmf:0323ca8cfe512c3d74812311eb0df73f02b5376f19e23e8171c24395af38904c@ec2-44-207-126-176.compute-1.amazonaws.com:5432/d3nd1ppttdbtcq"
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

db = SQLAlchemy(app)

from app.controller import routes
