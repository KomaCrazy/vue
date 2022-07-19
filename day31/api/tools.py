from importlib.resources import path
import sqlite3
from flask import Flask , request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
host = '0.0.0.0'
port = 5000
table = 'db'
path = './db.sqlite'

class sql :
    def login(user,password):
        items = []
        sql_find = 'select * from '+table+' where user="'+user+'" and password="'+password+'";'
        with sqlite3.connect(path) as conn :
            for row in conn.execute(sql_find):
                data = {}
                data["id"] = row[0]
                data["user"] = row[1]
                data["password"] = row[2]
                data["email"] = row[3]
                items.append(data)
            return items[0]
class server :
    def on():
        app.run(host,port) 