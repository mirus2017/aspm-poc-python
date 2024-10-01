import sqlite3
  
conn = sqlite3.connect('bank.db')
print ("Opened hr database successfully")
  
conn.execute('CREATE TABLE users (login CHAR(10) NOT NULL, password TEXT NOT NULL, fullname TEXT NOT NULL);')
print ("Table created successfully")
conn.close()