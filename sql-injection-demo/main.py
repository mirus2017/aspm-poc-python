import sqlite3
from prettytable import from_db_cursor
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request
from typing import Optional

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def search(request: Request):
   payload='<html><head><title>SQL Injection Demo</title></head><body><form action="/employees/" method="GET"><input type="text" name="login" value=""><input type="submit" value="Search"></form></body></html>'
   return HTMLResponse(content=payload)

@app.get("/employees/", response_class=HTMLResponse)
async def employeesEndpoint(login: Optional[str] = None):  
   connection = sqlite3.connect('hr.db')
   cursor = connection.cursor()
   sql = "select * from employees where login = '{0}'".format(login)
   print("SQL: ", sql)
   cursor.execute(sql)
   table = from_db_cursor(cursor)
   htmlTableString = table.get_html_string()
   connection.close()
   payload='<html>\n  <head>\n    <title>SQL Injection Demo</title>\n  </head>\n  <body>\n    <form action="/employees/" method="GET">\n      <input type="text" name="login" value="{0}">\n      <input type="submit" value="Search">\n	</form>\n  <br/>{1}</body>\n</html>'.format(login, htmlTableString)
   return HTMLResponse(content=payload)

# To run application execute
# uvicorn main:app --reload

async def method():
   username = "mirek"
   password = "mypassowrd"
   print(f"{username} {password}")