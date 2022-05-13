import sqlite3
from config import *
id = 0
def search_cout():
  try:
    with sqlite3.connect(path) as conn :
          for row in conn.execute(sql_find) :
            print(row)
  except Exception as e:
    print("Error : Search")
def insert_data() :
  try:
    with sqlite3.connect(path) as conn :
        user = str(input("user : "))
        password = str(input("password : "))
        age = int(input("age : "))
        contact = str(input("contact : "))
        sql_insert = "insert into " + table ,"values("+str(id + 1)+\
                                "," + as_34 + user + as_34 +\
                                "," + as_34 + password + as_34+\
                                "," + as_34 + age + as_34+\
                                "," + as_34 + contact + as_34+""
        print(sql_insert)
  except Exception as e:
    print("Error")

