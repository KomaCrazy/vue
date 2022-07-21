from tools import *


@app.route('/')
def pageHome():
    return '0'

@app.route('/login')
def pageLogin():
  try:
    data = request.args
    return jsonify(sql.login(data))
  except Exception as e:
    return jsonify(server.error(e))

@app.route('/register')
def pageRegister():
  try:
    data = request.args
    return jsonify(sql.register(data))
  except Exception as e:
    return jsonify(server.error(e))

@app.route('/del')
def pageDelete():
  try:
    data = request.args
    return jsonify(sql.delete(data))
  except Exception as e:
    return jsonify(server.error(e))


if __name__ == '__main__':
    server.on()