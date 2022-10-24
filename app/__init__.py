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
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://uyguffmfukvhct:9293a44daa7a509b38e62b1284b5cf9bbddb8e8d8cce964aab2dc6ce09dbae45@ec2-52-23-131-232.compute-1.amazonaws.com:5432/d4pvivieq3pi5"
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

db = SQLAlchemy(app)

from app.controller import routes