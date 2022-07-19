from tools import *

@app.route('/')
def page_0():
    return '0'

@app.route('/login')
def page_login():
    data = request.args
    user = data["user"]
    password = data["password"]
    return jsonify(sql.login(user,password))

server.on()