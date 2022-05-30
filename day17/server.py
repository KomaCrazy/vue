
from msilib.schema import Error
from tools import *

@app.route('/')
def page_0():
    return '0'

@app.route('/register' , methods=['GET'])
def page_register():
    try:
        data = request.args
        print(data)
        end = "success : ",data
        return 
    except Exception as e:
        Erorr = "Error :",e
        print(Error) 
        return Error

@app.route('/api')
def pagea_pi():
    try:
        conn = sqlite3.connect(path)
        rows = conn.execute(sql_find)
        data = []
        for row in rows :
            rr = {}
            rr["id"] = row[0]
            rr["user"] = row[1]
            rr["password"] = row[2]
            rr["email"] = row[3]
            rr["contact"] = row[4]
            data.append(rr)
        return jsonify(data)
    except Exception as e:
        print("Error :",e)

if __name__ == '__main__':
    app.run(host,port)


