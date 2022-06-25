
from tools import * 

@app.route('/')
def page0():
    return ''

@app.route('/login')
def page_login():
    return '' 

@app.route('/data')
def page_data():
    try :
        table = []
        conn = sqlite3.connect(path)
        for row in conn.execute(sql_find):
            data={}
            data["id"] = row[0]
            data["user"]= row[1]
            data["password"] = row[2]
            data["email"] = row[3]
            data["age"] = row[4]
            table.append(data)
        return jsonify(table)
    except Exception as e :
        return 'Error'

if __name__ == '__main__':
    app.run(host,port)