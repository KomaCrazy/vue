import email
import sqlite3
from flask import Flask, request ,jsonify 
from flask_cors import CORS 
app = Flask(__name__)
CORS(app)

host = '0.0.0.0'
port = 3000
table = 'profiles'
path = 'db.sqlite'

class sql:
    def login(data):
        user = str(data["user"])
        password = str(data["password"])
        with sqlite3.connect(path) as conn :
            sql_cmd = 'select * from '+table+' where user="'+user+'" and password="'+password+'";'
            for row in conn.execute(sql_cmd):
                data = {}
                data["id"] = row[0]
                data["user"]=row[1]
                data["password"] = row[2]
                data["email"] = row[3]
                return data
    def register(data):
        user = str(data["user"])
        password = str(data["password"])
        email = str(data["email"])
        with sqlite3.connect(path) as conn :
            sql_cmd = 'insert into '+ table+'(user,password,email)values("'+user+'","'+password+'","'+email+'");'        
            conn.execute(sql_cmd)
        return [{"status":'0'}]

    def delete(data):
        id = str(data["id"])
        with sqlite3.connect(path) as conn:
            sql_cmd = 'delete from '+table+ ' where id='+id+';'
            print(sql_cmd)
            conn.execute(sql_cmd)
        return [{"status":"0"}]

class server :
    def error(e):
        alert = [{"status":str(e)}]
        return alert
    def on():

            app.run(host,port)