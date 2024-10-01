import sqlite3
  
conn = sqlite3.connect('hr.db')
print ("Opened hr database successfully")
#conn.execute("INSERT INTO employees (id,login,fullname,age,address,salary) VALUES (1, 'mirek', 'Mirek Kowalski', 40, 'Warsaw, Poland', 20000.00 )");  
conn.execute("INSERT INTO employees (id,login,fullname,age,address,salary) VALUES (2, 'amir', 'Amir Kumar', 33, 'Noida, India', 4560.50 )");
conn.execute("INSERT INTO employees (id,login,fullname,age,address,salary) VALUES (3, 'james', 'James Bond', 50, 'London, UK', 9999999.0 )");
conn.execute("INSERT INTO employees (id,login,fullname,age,address,salary) VALUES (4, 'chuck', 'Chuck Norris', 60, 'Dallas, US', 50004.0 )");  
print ("Commit transaction")
conn.commit()   
print ("Row(s) inserted successfully")
conn.close()