import re
from tkinter import E
from tools import * 



@app.route('/')
def page0():
    return '0'

@app.route('/apidata')
def page_apidata():
    try:
        t1 = []
        conn = sqlite3.connect(path)
        for row in conn.execute(sql_find):
            data = {}
            data["id"] = row[0]
            data["user"] = row[1]
            data["password"] = row[2]
            data["email"] = row[3]
            data["age"] = row[4]
            t1.append(data)
        return jsonify(t1)
    except Exception as e:
        error(e)
        return 'Error'

@app.route('/register')
def page_register():
    try:
        data = request.args
        user = str(data["user"])
        password = str(data["password"])
        email = str(data["email"])
        age = str(data["age"])
        conn = sqlite3.connect(path)
        sql_regis = " insert into "+table+"(user,password,email,age)values(?,?,?,?)"
        cur = conn.cursor()
        cur.execute(sql_regis,(user,password,email,age))
        conn.commit()
        return "sucess"
    except Exception as e:
        error(e)
        return "Error"

@app.route('/login')
def page_find():
    try:
        data = request.args
        user = data["user"]
        password = data["password"]
        conn = sqlite3.connect(path)
        sql_select_find = 'select * from '+table+' where user="'+user+'" and password="' + password + '";'
        t1 = []
        for row in conn.execute(sql_select_find):
            data = {}
            data["id"] = row[0]
            data["user"] = row[1]
            data["password"] = hash(row[2])
            data["email"] = row[3]
            data["age"] = row[4]
            t1.append(data)
            
        return jsonify(row)
    except Exception as e:
        error(e)
        return "Error"

@app.route('/del')
def page_del():
    try:
        data = request.args
        id = data["id"] 
        conn = sqlite3.connect(path)
        sql_del = "delete from "+table+" where id="+str(id)+";"
        cur = conn.cursor()
        cur.execute(sql_del)
        conn.commit()
        return '0'
    except Exception as e:
        error(e) 
        return 'Error'        

if __name__ == '__main__':
    app.run(host,port)