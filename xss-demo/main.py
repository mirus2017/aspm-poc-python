from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request
from typing import Optional

app = FastAPI()

@app.get("/")
async def root():
   return "XSS (Cross-Site Scripting) demo, use /searchForm"

@app.get("/searchForm/", response_class=HTMLResponse)
async def searchFrom(search: Optional[str] = ""):
   payload='<html>\n  <head>\n    <title>XSS (Cross-Site Scripting) demo</title>\n  </head>\n  <body>\n    <form action="/searchForm/" method="GET">\n      <input type="text" size="80" name="search" value="">\n      <input type="submit" value="Go!">\n	</form>\n<br>Input parameter: <b>{0}</b></br>\n  </body>\n</html>'.format(search)
   return HTMLResponse(content=payload)
