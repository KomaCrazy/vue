import sqlite3
from unittest import result
from flask import Flask , jsonify , request 
from flask_cors import CORS
 
app = Flask(__name__)
CORS(app)

host = '0.0.0.0'
port = 3000
path = './db.sqlite'
table = 'db'

class sql :
    def login(user,password):
        with sqlite3.connect(path) as conn :
            result = []
            sql_login = 'select * from '+table+' where user="'+user+'" and password="'+password+'";'
            for item in conn.execute(sql_login):
                data = {}
                data["id"] = item[0]
                data["user"] = item[1]
                data["password"] = item[2]
                result.append(data)
            return result[0]
class server :
    def on():
        app.run(host,port)