from hotp import HOTP
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

shared_secrets_dict = {'XXXXXX' : 'abcd efgh ijkl dj2z', 'YYYYYY':'zxcd bnmk 0934 vt5b'}
app = FastAPI()
hotp = HOTP()
@app.get("/otps/{signum}", response_class=PlainTextResponse)
@app.get("/int-msauthenticator-python/otps/{signum}", response_class=PlainTextResponse)
async def get_security_code(signum: str):
  shared_secret = shared_secrets_dict.get(signum.upper())
  shared_secret = "".join(shared_secret.split()).upper()
  secret_key = hotp.convert_base32_secret_key(shared_secret)
  code_string, remaining_seconds = hotp.generate_code_from_time(secret_key)
  return code_string
