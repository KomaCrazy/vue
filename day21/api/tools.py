import sqlite3
from flask import Flask , jsonify ,request
from flask_cors import CORS
import json 
app = Flask(__name__)
CORS(app)

t1 = []
path = "./db.sqlite" # path for sqlite3
table = "box1" # for sqlite3 

host = '0.0.0.0' # for api server 
port = 5000 # for api server

conn = ""
sql_find = "select * from "+table+";"
sql_create = "create table if not exists "+ table +\
    "(id integer primary key,"+\
    "user text not null,"+\
    "password text not null,"+\
    "email text not null,"+\
    "age text,"+\
    "constraint user unique(user),"+\
    "constraint email unique(email));"



def create_table():
    try:
        conn = sqlite3.connect(path)
        conn.execute(sql_create)
    except Exception as e:
        print("Error",e)

def error(e):
    error = "Error :",e
    print("_________________________________________________________")
    print(error)
    print("_________________________________________________________")