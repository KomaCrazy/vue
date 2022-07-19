import sqlite3
from flask import Flask , request , jsonify
from flask_cors import CORS
from matplotlib.pyplot import table
app = Flask(__name__)
CORS(app)
host = '0.0.0.0'
port = 5000
path = './db.sqlite'
table = 'db'

class sql :
    def login(user,password):
        with sqlite3.connect(path) as conn:
            sql_cmd = 'select * from '+table+' where user="'+user+'" and password="'+password+'";'
            rr = []
            for row in conn.execute(sql_cmd):
                data = {}
                data["id"] = row[0]
                data["user"] = row[1]
                data["password"] = row[2]
                data["email"]= row[3]
                rr.append(data)
            return rr[0]
class server:
    def on():
        app.run(host,port)