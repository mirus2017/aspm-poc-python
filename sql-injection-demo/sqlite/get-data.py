import sqlite3
  
conn = sqlite3.connect('hr.db')
print ("Opened hr database successfully")
data = conn.execute("select * from employees")
print ("Executed sql")
  
for row in data:
  print ("id: {0}".format(row[0]))
  print ("login: {0}".format(row[1]))
  print ("fullname: {0}".format(row[2]))
  print ("age: {0}".format(row[3]))
  print ("address: {0}".format(row[4]))
  print ("salary: {0}".format(row[5]))
  print ("------------------------------")

conn.close()