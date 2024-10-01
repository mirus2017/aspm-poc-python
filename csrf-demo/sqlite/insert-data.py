import sqlite3
  
conn = sqlite3.connect('bank.db')
print ("Opened bank database successfully")
conn.execute("INSERT INTO users (login,password,fullname) VALUES ('mirek', 'Mirek123', 'Mirek Kowalski')");  
conn.execute("INSERT INTO users (login,password,fullname) VALUES ('amir',  'Bolywood', 'Amir Kumar')");
conn.execute("INSERT INTO users (login,password,fullname) VALUES ('james', 'Mi6', 'James Bond')");
conn.execute("INSERT INTO users (login,password,fullname) VALUES ('chuck', 'Texas', 'Chuck Norris')");  
print ("Commit transaction")
conn.commit()   
print ("Row(s) inserted successfully")
conn.close()