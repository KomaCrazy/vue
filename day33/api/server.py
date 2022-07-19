from tools import *

@app.route('/')
def pageNaN():
    return '0'

@app.route('/login')
def pageLogin():
    data = request.args
    user = str(data["user"])
    password = str(data["password"])
    return jsonify(sql.login(user,password))



if __name__ == '__main__':
    server.on()