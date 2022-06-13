import sqlite3 
import json 
from flask import Flask 
from flask_cors import CORS  
app = Flask(__name__)
CORS(app)
table = "data"
sql_create = "create ta"

def create_table():
    


host = '0.0.0.0'
port = 5000

