import csv
import os

path = ""
archivoUsuarios = path + "usuarios.csv"
archivoUsuariosTemp = path + "usuariosTemp.csv"

def validarExisteUsuarioDatos(usuario):
    try:
        with open(archivoUsuarios) as archivo:
            archivo_csv = csv.reader(archivo)
            registro = next(archivo_csv)
            while registro:
                if usuario == registro[0]:
                    return 0, 0
                registro = next(archivo_csv, None)
            return 1, 0
    except OSError:
        return 0, 2
    else: 
        return 0, 1

def grabarUsuarioDatos(registro):
    try:
        with open(archivoUsuarios, 'a+') as archivo:
            archivo_csv = csv.writer(archivo)
            archivo_csv.writerow(registro) 
        return 1, 0       
    except OSError:
        return 0, 2
    else: 
        return 0, 1

def buscarUsuarioDatos(nombreUsuario, password): 
    try:
        with open(archivoUsuarios) as archivo:
            archivo_csv = csv.reader(archivo)
            registro = next(archivo_csv)
            while registro:
                if nombreUsuario == registro[0] and password == registro[1]:
                    return 1, 0
                registro = next(archivo_csv, None)
            else:
                return 0, 0
    except OSError:
        return 0, 2
    else: 
        return 0, 1

def grabarPwdUsuarioDatos(registro): 
    try:
        with open (archivoUsuarios, 'r') as archivoOrigen:
            reader=csv.reader(archivoOrigen)
            with open (archivoUsuariosTemp, 'w') as archivoDestino:
                writer=csv.writer(archivoDestino)
                for registroLeido in reader:
                    if registroLeido[0] == registro[0]:
                        registroLeido[1] = registro[1]
                    writer.writerow(registroLeido)
        os.remove(archivoUsuarios)
        os.rename(archivoUsuariosTemp, archivoUsuarios)
        return 1, 0       
    except OSError:
        return 0, 2
    else: 
        return 0, 9