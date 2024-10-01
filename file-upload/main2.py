import os
from fastapi import FastAPI, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
import zipfile

app = FastAPI()

@app.post("/uploadfile")
async def upload_file(file: UploadFile):
  print (f"Received {file.filename} file, content type: {file.content_type}")
  destFilename = f"c:/Temp/file-upload/uploadFolder/"+file.filename
  print (f"Write file content to {destFilename}")
  destFile = open(destFilename, "wb")
  file_content = file.file.read()
  destFile.write(file_content)
  destFile.close()
  extract(destFilename, "c:/Temp/file-upload/extractFolder/")
  return RedirectResponse("/")

@app.post("/")
@app.get("/")
async def main():
  content = """
<html>
  <head>
    <title>Security Masters - Demo of file upload attack</title>
  </head>
  <body>
    <h2>File upload (ZIP)</h2>
    <form action="/uploadfile" method="post" enctype="multipart/form-data" accept="zip,application/octet-stream,application/zip,application/x-zip,application/x-zip-compressed">
      <input name="file" type="file" />
      <br />
      <br />
      <input type="submit" />
    </form>
  </body>
</html>
    """
  return HTMLResponse(content=content)

def extract_archive(file_path, extract_to):
  print("extract_archive(",file_path, ",", extract_to, ")")
  with zipfile.ZipFile(file_path, 'r') as zip_file:
    for zipInfo in zip_file.infolist():
      print(zipInfo)
    print ("zip_file.extractall(", extract_to, ")")
    zip_file.extractall(extract_to)

def recursive_extract(path, extract_to_root):
  print ("recursive_extract(", path, ", ", extract_to_root, ")")
  for root, _, files in os.walk(path):
    for file in files:
      file_path = os.path.join(root, file)
      if file_path.endswith(('.zip')):
        subdir_name = os.path.splitext(file)[0]
        extract_to = os.path.join(extract_to_root, subdir_name)
        os.makedirs(extract_to, exist_ok=True)
        extract_archive(file_path, extract_to)
        os.remove(file_path)
        #recursive_extract(extract_to, extract_to_root)
        recursive_extract(extract_to, extract_to)

def extract(archive_path, destination_path):
  print("extract(", archive_path, ",", destination_path, ")")
  base_name = os.path.splitext(os.path.basename(archive_path))[0]
  extract_to_root = os.path.join(destination_path, base_name)
  os.makedirs(extract_to_root, exist_ok=True)
  extract_archive(archive_path, extract_to_root)
  recursive_extract(extract_to_root, extract_to_root)
