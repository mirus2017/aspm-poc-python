import sqlite3
from prettytable import from_db_cursor
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request, Form
from typing import Optional, Annotated

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def search(request: Request):
   payload='<html><head><title>CSRF Demo</title></head><body><form action="/users/" method="POST"><label for="login">Login:</label><br/><input type="text" id="login" name="login" value=""><br/><label for="password">Password:</label><br/><input type="password" id="password" name="password" value=""><br/><label for="fullname">Full name:</label><br/><input type="text" id="fullname" name="fullname" value=""><br/><br/><input type="submit" value="Create user"></form></body></html>'
   return HTMLResponse(content=payload)

@app.get("/users/add", response_class=HTMLResponse)
async def usersAdd(login: str, password: str, fullname: str):  
   connection = sqlite3.connect('bank.db')
   sql = "INSERT INTO users (login,password,fullname) VALUES ('{0}', '{1}', '{2}')".format(login, password, fullname)
   print (sql)
   connection.execute(sql);
   connection.commit()  
   connection.close()
   payload='<html>\n  <head>\n    <title>CSRF Demo</title>\n  </head>\n  <body>User {0} was created</body>\n</html>'.format(login)
   return HTMLResponse(content=payload)


@app.post("/users/", response_class=HTMLResponse)
async def addUser(login: Annotated[str, Form()], password: Annotated[str, Form()], fullname: Annotated[str, Form()]):  
   connection = sqlite3.connect('bank.db')
   sql = "INSERT INTO users (login,password,fullname) VALUES ('{0}', '{1}', '{2}')".format(login, password, fullname)
   print (sql)
   connection.execute(sql);
   connection.commit()  
   connection.close()
   payload='<html>\n  <head>\n    <title>CSRF Demo</title>\n  </head>\n  <body>User {0} was created</body>\n</html>'.format(login)
   return HTMLResponse(content=payload)


@app.get("/users", response_class=HTMLResponse)
async def getUsers():  
   connection = sqlite3.connect('bank.db')
   cursor = connection.cursor()
   sql = "select * from users"
   cursor.execute(sql)
   table = from_db_cursor(cursor)
   htmlTableString = table.get_html_string()
   connection.close()
   payload='<html>\n  <head>\n    <title>CSRF Demo</title>\n  </head>\n  <body>{0}</body>\n</html>'.format(htmlTableString)
   return HTMLResponse(content=payload)

# To run application execute
# uvicorn main:app --reload