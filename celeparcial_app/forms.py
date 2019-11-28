from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import Required
from logica.logica import *
from datetime import datetime

class LoginForm(FlaskForm):
    usuario = StringField('Nombre de usuario', validators=[Required()])
    password = PasswordField('Contraseña', validators=[Required()])
    enviar = SubmitField('Ingresar')

class RegistrarForm(LoginForm):
    password_check = PasswordField('Verificar Contraseña', validators=[Required()])
    enviar = SubmitField('Registrarse')

class GenerarNuevoUsuarioForm(FlaskForm):
    usuario = StringField('Nombre de usuario', validators=[Required()])
    password = StringField('Contraseña', validators=[Required()])
    enviar = SubmitField('Aceptar')