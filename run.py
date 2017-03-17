from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Gerhard! Puerto 8000, OK'

if __name__ == '__main__':
    app.run (debug = True, port = 8000)
