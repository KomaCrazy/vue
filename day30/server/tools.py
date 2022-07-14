from importlib.resources import path
import sqlite3
from flask import Flask , jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
port = 5000
host = '0.0.0.0'
path = './db.sqlite'


class sql:

    def insert(val1,val2):
        print("insert ",val1,val2)

    def find(val1,val2):
        sql_find = 'select * from data where user="'+val1+'" and password="'+val2+'";'
        conn = sqlite3.connect(path)
        rr = []
        for row in conn.execute(sql_find):
            data = {}
            data["id"] = row[0]
            data["user"] = row[1]
            data["password"]= row[2]
            data["age"] = row[3]
            rr.append(data)
        return jsonify(rr[0])


class server:
    def on():
        app.run(host,port)