from tools import *

@app.route('/')
def page0():
    return '0'

@app.route('/login')
def pageLogin():
  try: 
    data = request.args
    user = data["user"]
    password = data["password"]
    return jsonify(sql.login(user,password))
  except Exception as e:
    return jsonify(server.error(e))

@app.route('/register')
def pageRegister():
    data = request.args
    user = data["user"]
    password = data["password"]
    email = data["email"]
    return jsonify(sql.register(user,password,email))

@app.route('/delete')
def pageDelete():
  data = request.args
  id = data["id"]
  return jsonify(sql.delete(id))

if __name__ == '__main__':
    server.on()