from flask import Flask, jsonify 
from flask_cors import CORS 
app = Flask(__name__)
CORS(app)

@app.route('/')
def page_0():
    return jsonify("OK")

    
if __name__ == '__main__':
    app.run('0.0.0.0',5000)