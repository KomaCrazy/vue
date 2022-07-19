from flask import jsonify
from requests import request
from tools import * 

@app.route('/')
def page_0():
    return '0'

@app.route('/login')
def page_login():
  try:
    data = request.args
    user = str(data["user"])
    pasword = str(data["password"])
    return jsonify(sql.login(user,pasword))
  except Exception as e:
    return e
server.on()