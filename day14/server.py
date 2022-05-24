from flask import Flask , jsonify,request,jsonify
from flask_cors import CORS
import sqlite3
import json

from tools import *

app = Flask(__name__)
CORS(app)

@app.route(link0)
def link0():
    try:
        return '0'
    except Exception as e:
        print("Error : " + link0)

@app.route(link1)
def link1():
    try:
        d = []
        with sqlite3.connect("data.sqlite") as conn :
          for row in conn.execute(sql_select) :
            a = {}
            a["id"] = row[0]
            a["user"] = row[1]
            a["password"] = row[2]
            a["age"] = row[3]
            d.append(a)
        return jsonify(d)
    except Exception as e:
        print("Error : "+link1)

@app.route('/register')
def register():
    try:
        data = request.args
        username = data["username"]
        lastname = data["lastname"]
        password = data["password"]
        email = data["email"]
        age = data["age"]
        return jsonify("OK")
    except Exception as e:
       return jsonify(e)

if __name__ == '__main__' :
    app.run(host,port)