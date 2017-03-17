 
# -*- coding: utf-8 -*-
# # Autor: GLO-pineapples
# www.glo-pineapples.com

from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
from flask import render_template
from flask import request

app = Flask(__name__, template_folder='Look4offers')

@app.route('/') 
@app.route('/index') 

@app.route('/Negocio/<Nl4o>')
def index (Nl4o ='Negocio L4O'):
    return render_template ('index.html',Negocio = Nl4o)

#@app.route("/hola/<string:name>")
@app.route("/hola/<string:name>/")
def hello(name):
#    return name
    quotes = [ u"'Un buen diseño aporta un valor añadido más rápido de lo que agrega costo.' -- Thomas C. Gale  ",
               u"'Hablar es barato. Enséñame el código' --  Linus Torvalds  ",
               u"'Siempre codifica como si la persona que finalmente mantendrá tu código fuera un psicópata violento que sabe dónde vives...' -- Martin Golding ",
               u"'Si la depuración es el proceso de eliminar errores, entonces la programación debe ser el proceso de introducirlos.' -- Edsger Dijkstra"
             ]
    randomNumber = randint(0,len(quotes)-1) 
    quote = quotes[randomNumber] 
  
    return render_template(
        'test.html',**locals())

if __name__ == '__main__':
    app.run(debug=True, port=8000)
