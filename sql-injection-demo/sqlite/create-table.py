import sqlite3
  
conn = sqlite3.connect('hr.db')
print ("Opened hr database successfully")
  
conn.execute('CREATE TABLE employees (id INT PRIMARY KEY NOT NULL, login CHAR(10) NOT NULL, fullname TEXT NOT NULL, age INT NOT NULL, address CHAR(50) NULL, salary REAL NULL);')
print ("Table created successfully")
conn.close()