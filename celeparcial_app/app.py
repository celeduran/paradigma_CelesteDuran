import csv
import tablib, os
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_script import Manager
from forms import LoginForm, RegistrarForm, GenerarNuevoUsuarioForm
from flask import send_file

from logica.logica import *

app = Flask(__name__)
manager = Manager(app)
Bootstrap (app)
moment = Moment(app)

app.config['SECRET_KEY'] = 'thecodex'
csv_path = 'clientes.csv'
csv_obj = csv.DictReader(open(csv_path, 'r',encoding='utf-8'))
csv_list = list(csv_obj)

def tratarError(huboError):
    if huboError == 1:
        flash("Error: Error indeterminado")
    if huboError == 2:
        flash("Error: No se pudo abrir el archivo")
        
@app.route('/')
def welcome():
    return render_template('welcome.html')
    
@app.errorhandler(404)
def no_encontrado(e):
    if 'username' in session:
        return render_template('404_ingresado.html'), 404
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_interno(e): 
    if 'username' in session:
        return render_template('500_ingresado.html'), 500
    return render_template('500.html'), 500

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/ingresar', methods=['GET', 'POST'])
def ingresar():
    if 'username' in session:
        return render_template('ingresado.html')
    formulario = LoginForm()
    if formulario.validate_on_submit():
        valor, huboError = buscarUsuario(formulario.usuario.data, formulario.password.data)
        tratarError(huboError)
        if valor == 1:
            session['username'] = formulario.usuario.data
            return render_template('ingresado.html', usuario=session['username'])
        else:
            flash('Error: Revisá nombre de usuario y contraseña')
            return redirect(url_for('ingresar'))
    return render_template('login.html', formulario=formulario)

@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    return render_template('clientes.html',
        object_list=csv_list)
        
@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if 'username' in session:
        return render_template('ingresado.html')
    formulario = RegistrarForm()
    if formulario.validate_on_submit():
        if formulario.password.data == formulario.password_check.data:
            valor, huboError = validarExisteUsuario(formulario.usuario.data)
            tratarError(huboError)
            if valor==0:
                flash("Error: El usuario ya existe")
                return render_template('registrar.html', form=formulario)
            registro = [formulario.usuario.data, formulario.password.data]
            valor, huboError = grabarUsuario(registro)
            tratarError(huboError)
            if valor == 1:
                flash('Mensaje: Usuario creado correctamente')
            else:
                flash('Error: Hubo un error en la creación del usuario')
            return redirect(url_for('ingresar'))
        else:
            flash('Error: Las passwords que acaba de ingresar no son la misma')
    return render_template('registrar.html', form=formulario)

@app.route('/generarNuevoUsuario', methods=['GET', 'POST'])
def generarNuevoUsuario():
    if 'username' not in session:
        return redirect(url_for('ingresar'))
    formulario = GenerarNuevoUsuarioForm()
    if formulario.validate_on_submit():
        valor, huboError = validarExisteUsuario(formulario.usuario.data)
        tratarError(huboError)
        if valor==0:
            flash("Error: El usuario ya existe")
            return render_template('generarNuevoUsuario.html', form=formulario)
        registro = [formulario.usuario.data, formulario.password.data]
        valor, huboError = grabarUsuario(registro)
        tratarError(huboError)
        if valor == 1:
            flash('Mensaje: Usuario creado correctamente')
        else:
            flash('Error: Hubo un error en la creación del usuario')
    return render_template('generarNuevoUsuario.html', form=formulario)

@app.route('/salir', methods=['GET'])
def logout():
    if 'username' in session:
        session.pop('username')
        return render_template('salir.html')
    else:
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)