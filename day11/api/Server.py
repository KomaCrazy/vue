import sqlite3
from flask import Flask , jsonify
from config import *
import json

app = Flask(__name__)

@app.route(link0)
def link_0():
    try:
        return '0'
    except Exception as e:
        print("Error : " + link0)

@app.route(link1)
def link_1():
    try:
        with sqlite3.connect(path) as conn :
            for row in conn.execute(sql_find) :

                table = {}
                table["id"] = row[0]
                table["user"] = row[1]
                table["password"] = row[2]
                table["age"] = row[3]
                table["contact"] = row[4]
                data.append(table)

        return jsonify(data)
    except Exception as e:
        print("Error : " + link1)

if __name__ == '__main__':
    app.run(host,port)