import sqlite3  
  
conn = sqlite3.connect('hr.db')  
  
print ("Opened database successfully")

conn.close()