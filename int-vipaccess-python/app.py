from flask import Flask
import os

app = Flask(__name__)

@app.route('/', methods = ['GET'])
@app.route('/int-vipaccess-python', methods = ['GET'])
def index():
    stream = os.popen('/usr/local/bin/vipaccess show -f .vipaccess-isetm2m')
    output = stream.read()
    return output
