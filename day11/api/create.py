import sqlite3
from config import path

def create_table():
  try:
    with sqlite3.connect(path) as conn :
      sql_cmd = "create table data(id primary key,user text,password text,age text ,contact text);"
      conn.execute(sql_cmd)
  except Exception as e :
      print("Error Create Table")
create_table()

