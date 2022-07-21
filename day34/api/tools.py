import email
from flask import Flask , request ,jsonify
from flask_cors import CORS
import sqlite3
app = Flask(__name__) 
CORS(app)
host = '0.0.0.0'
port = 5000

path = './db.sqlite'
table = 'db'


class server :
    def error(e):
        return {"status":"1"}
    def on():
        app.run(host,port)

class sql :
    def login(user,password):
        sql_cmd = 'select * from '+table+' where user="'+user+'" and password="'+password+'";'
        with sqlite3.connect(path) as conn :
            results = []
            for row in conn.execute(sql_cmd):
                box = {}
                box["id"] = row[0]
                box["user"] = row[1]
                box["password"] = row[2]
                box["email"] = row[3]
                results.append(box)
            return results[0]

    def register(user,password,email):
      try:
        sql_cmd = 'insert into '+table+'(user,password,email)values("'+user+'","'+password+'","'+email+'");'
        print(sql_cmd)
        with sqlite3.connect(path) as conn:
            conn.execute(sql_cmd)
        return [{"Status":"Success"}]
      except Exception as e:
        return [{"Status":str(e)}]
    def delete(id):
      try:
        sql_cmd = 'delete from '+table+' where id="'+id+'";'
        with sqlite3.connect(path) as conn:
            conn.execute(sql_cmd)
        return [{"Status":"Delete Success"}]
      except Exception as e:
        return [{"Status":str(e)}]