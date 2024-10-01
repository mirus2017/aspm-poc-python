from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request
from typing import Optional

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root():
   return {"message": "Root path"}

@app.get("/hello/")
async def hello():
   ret='''
<html>
<body>
<h2>Hello World!</h2>
</body>
</html>
'''
   return HTMLResponse(content=ret)

@app.get("/login/", response_class=HTMLResponse)
async def login(request: Request):
   return templates.TemplateResponse("login.html", {"request": request})

@app.get("/search/", response_class=HTMLResponse)
async def search(request: Request):
   return templates.TemplateResponse("search.html", {"request": request})

@app.get("/3/", response_class=HTMLResponse)
async def searchFrom(search: Optional[str] = None):
   payload='<html>\n  <head>\n    <title>XSS Demo</title>\n  </head>\n  <body>\n    <form action="/3/" method="POST">\n      <input type="text" name="search" value="{0}">\n      <input type="submit" value="Go!">\n	</form>\n  </body>\n</html>'.format(search)
   return HTMLResponse(content=payload)
