from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Gerhard! Puerto 8000, OK'

@app.route('/params')
def params():
    param = request.args.get('params1', 'no contiene parametro')
    return 'El par es {}'.format(param)

if __name__ == '__main__':
    app.run (debug = True, port = 8000)
