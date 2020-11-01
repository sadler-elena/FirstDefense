from flask import Flask
from flask import request
from requestHandle import websiteScan

app = Flask(__name__)

@app.route('/')
def handler():
    return websiteScan(request.args.get("url"))

if __name__ == '__main__':
    app.run(ssl_context='adhoc')


