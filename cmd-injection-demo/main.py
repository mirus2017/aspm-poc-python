import subprocess
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request
from typing import Optional

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def search(request: Request):
   payload='<html><head><title>Command Injection Demo</title></head><body><form action="/metadata/" method="GET"><label>URL of image:</label><input type="text" name="image_url" size="100" value="https://paulinakita.com/wp-content/uploads/2023/09/kwadrat3-1-768x775.jpg"><input type="submit" value="Get metadata info"></form></body></html>'
   return HTMLResponse(content=payload)

@app.get("/metadata/", response_class=HTMLResponse)
async def metadataEndpoint(image_url: Optional[str] = None):  
   print("image_url:", image_url)
   cmd = 'curl -s {0} | exiftool -short -'.format(image_url)
   print("Shell command:", cmd)
   ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
   output = ps.communicate()[0]
   text_output = output.decode('iso-8859-1').replace('\r', '')
   payload='<html>\n  <head>\n    <title>Command Injection Demo</title>\n  </head>\n  <body>\n    <form action="/metadata/" method="GET">\n      <label>URL of image:</label>\n      <input type="text" name="image_url" size="100" value="{0}">\n      <input type="submit" value="Get metadata info">\n    </form>\n  <br/>\n  <textarea rows="92" cols="200">{1}\n  </textarea>\n</body>\n</html>'.format(image_url, text_output)
   return HTMLResponse(content=payload)

# To run application execute
# uvicorn mainc:app --reload