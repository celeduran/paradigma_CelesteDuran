from datos.datos import *

def validarExisteUsuario(usuario):
    valor,huboError = validarExisteUsuarioDatos(usuario)
    return valor, huboError

def grabarUsuario(registro):
    valor,huboError = grabarUsuarioDatos(registro)
    return valor, huboError

def buscarUsuario(nombreUsuario, password):
    valor,huboError = buscarUsuarioDatos(nombreUsuario, password)
    return valor, huboError
  
def grabarPwdUsuario(registro):
    valor,huboError = grabarPwdUsuarioDatos(registro)
    return valor, huboError