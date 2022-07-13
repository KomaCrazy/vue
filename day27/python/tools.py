import sqlite3 
from flask import Flask , jsonify ,request
from flask_cors import CORS 
path = 'box1.sqlite'
port = 5000
table = "box"
sql_find = "select * from "+table+";"
sql_create = "create table if not exists "+ table +\
    "(id integer primary key,"+\
    "user text not null,"+\
    "password text not null,"+\
    "email text not null,"+\
    "age text,"+\
    "constraint user unique(user),"+\
    "constraint email unique(email));"

def error(val):
    return val

def create_table():
    try:
        conn = sqlite3.connect(path)
        conn.execute(sql_create)
        return 'OK'
    except Exception as e:
        error(e)
print(create_table())