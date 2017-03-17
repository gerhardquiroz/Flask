from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='Look4offers')

@app.route('/Negocio/<Nl4o>')
def index (Nl4o ='Negocio L4O'):
    return render_template ('index.html',Negocio = Nl4o)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
