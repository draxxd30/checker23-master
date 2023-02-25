import MySQLdb
from plugins.clases.usuarios import usuario

def buscarIdioma(user, id):
    user = usuario(user, id)
    datos = user.buscar()
    if not datos or datos == False: return False
    idioma = datos[6]
    return idioma

##bin##
        
    