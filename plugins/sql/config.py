from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from plugins.clases.usuarios import usuario
import MySQLdb
from configs import config

def configIdioma(idioma, user, id):
    user = usuario(user, id)
    datos = user.buscar()
    if not datos or datos == False: return '<b>Usuario no registrado porfavor registrese con /start</b>'
    try:
        isiomaU = datos[6]
    except Exception: return 'Error al ver el idioma'
    if isiomaU == idioma: return 'Usted ya tiene este idioma seleccionado'
    query = f"UPDATE usuarios SET Idioma = '{idioma}' WHERE idTG = '{id}'"
    try:
        with MySQLdb.connect(host = config.DB_HOST, user = config.DB_USER, password = config.DB_PASS, database = config.DB_NAME) as connect:
            cursor = connect.cursor()
            re = cursor.execute(query)
            connect.commit()
            if re != 1: return 'False'
    except Exception: return 'None'
    datos2 = user.buscar()
    if datos2[6] != str(idioma): return 'Error al actualizar el idioma' 
    if idioma == 'es': idioma = 'Español'
    elif idioma == 'en': idioma = 'Inglish'
    return f'<b>Idioma actualizado con exito a {idioma}</b>'