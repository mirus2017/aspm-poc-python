import sqlite3
from prettytable import from_db_cursor
  
connection = sqlite3.connect('hr.db')
print ("Opened hr database successfully")
cursor = connection.cursor()
cursor.execute("select * from employees")
print ("Executed sql")
table = from_db_cursor(cursor)
s = table.get_html_string()
print(s)
connection.close()

