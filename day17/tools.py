import sqlite3
from flask import Flask , jsonify ,  request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
table = "box1"
port = 5000
host = '0.0.0.0'
path = "data.sqlite3"

sql_find = "select * from "+table +";"

sql_create = "create table if not exists " + table +\
             "(id integer primary key, "+\
             "user text not null, "+\
             "password text not null, "+\
             "email text not null, "+\
             "contact text not null,"+\
             "constraint user unique(user),"+\
             "constraint email unique(email));"

def create_table():
    try:
        conn = sqlite3.connect(path)
        conn.execute(sql_create)
    except Exception as e:
        print("Error :",e)