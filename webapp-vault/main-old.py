from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request, Form
from typing import Optional, Annotated
import hvac

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def read_secret(solution, microservice, secret):
   vault_token = ""
   if (microservice == "microservice-a"):
       vault_token = "hvs.CAESIEGFHQdPuX4NxosQ8JYMORVd6VCR4VasHkyqJqtkvkpaGh4KHGh2cy5yRU5HcjFPUDhxc0xFdnJJOVNPc1R5RGM"
   elif (microservice == "microservice-b"):
       vault_token = "hvs.CAESINwL02sfgvtQKvabmvqxK__VvpXgysHLAz8UtmIp4wvIGh4KHGh2cy42YlU0TWxkSDZiUmNlMk5MNno2VDNXQzE"
   elif (microservice == "microservice-c"):
       vault_token = "hvs.CAESIGIolF_i4czyqjX-wJVr3ZzudBcdDo1fuVx-pFnPfrjQGh4KHGh2cy5DS253Mkc2S25lQ2hneGltR0NCNGE3MzE"
   print ("vault_token:", vault_token)
   client = hvac.Client(url='http://127.0.0.1:8200', token=vault_token)
   print ("Is authenticated:", client.is_authenticated())
   vault_path = f"{solution}/{secret}"
   print ("vault_path:", vault_path)
   response = ""
   try:
      response = client.secrets.kv.v1.read_secret(mount_point='secret', path=vault_path)["data"]
   except hvac.exceptions.Forbidden:
      response = "hvac.exceptions.Forbidden: Permission deny"
   return response


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
   return templates.TemplateResponse("mainp.html", {"request": request, "param_solution": "solution-abc", "param_microservice": "microservice-a", "param_secret": "ad/egad", "vault_result": ""})

@app.post("/", response_class=HTMLResponse)
async def submit(solution: Annotated[str, Form()], microservice: Annotated[str, Form()], secret: Annotated[str, Form()], request: Request):
   print("solution=", solution)
   print("microservice=", microservice)
   print("secret=", secret)
   vault_result = read_secret(solution, microservice, secret)
   return templates.TemplateResponse("mainp.html", { "request": request, "param_solution": solution, "param_microservice": microservice, "param_secret": secret, "vault_result": vault_result})

