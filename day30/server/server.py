from tools import * 


@app.route('/')
def page_0():
    box = request.args
    return box

@app.route('/login')
def page_1():
  try:
    data = request.args
    user = str(data["user"])
    password = str(data["password"])
    return sql.find(user,password)
  except Exception as e:
    error = {"Message":"Fail"}
    return jsonify(error)
if __name__ == '__main__':
    server.on()
