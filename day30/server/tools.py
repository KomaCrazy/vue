import sqlite3
from flask import Flask 
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
port = 5000
host = '0.0.0.0'

class sql:
    def insert(val1,val2):
        print("insert ",val1,val2)

    def find(val1,val2):
        print("find")

    def update(val1,val2):
        print("update")

    def delete(val1,val2):
        print("delete",val1,val2)

class 

class server:
    def on():
        app.run(host,port)