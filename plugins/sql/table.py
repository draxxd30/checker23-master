from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
import MySQLdb
from configs import config
import re
from plugins.clases.usuarios import usuario

def creartabla(nombre, id=True):
    if id == True: 
        query = f"CREATE TABLE {nombre} (id INT AUTO_INCREMENT PRIMARY KEY)"
    if id == False:
        query = f"CREATE TABLE {nombre}"
    
    try:
        with MySQLdb.connect(host = config.DB_HOST, user = config.DB_USER, password = config.DB_PASS, database = config.DB_NAME) as connect:
            cursor = connect.cursor()
            re = cursor.execute(query)
            connect.commit()
            if re == 0:
                return True
            else:
                return False
    except Exception as e:
        return None
    
def eliminarTabla(nombre):
    query = f"DROP TABLE {nombre}"
    try:
        with MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASS, database=config.DB_NAME) as connect:
            cursor = connect.cursor()
            re = cursor.execute(query)
            connect.commit()
            if re == 0:
                return True
            else:
                return False
    except Exception:
        return None
    
def CrearCol(nombreT, nombre, tamaño):
    query = f"ALTER TABLE {nombreT} ADD {nombre} VARCHAR({tamaño})"
    try:
        with MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASS, database=config.DB_NAME) as connect:
            cursor = connect.cursor()
            res = cursor.execute(query)
            connect.commit()
            if res == 0:
                return True
            else:
                return False
    except Exception:
        return None
    
def eliminarCol(nombreT, nombreC):
    query = f"ALTER TABLE {nombreT} DROP COLUMN {nombreC}"
    try:
        with MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASS, database=config.DB_NAME) as connect:
            cursor = connect.cursor()
            res = cursor.execute(query)
            connect.commit()
            if res == 0:
                return True
            else:
                return False
    except Exception:
        return None

def renombrarCol(nombreT, nombreC, nuevonombreC):
    query = f"EXEC sp_RENAME '{nombreT}.{nombreC}' , '{nuevonombreC}', 'COLUMN'"
    try:
        with MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASS, database=config.DB_NAME) as connect:
            cursor = connect.cursor()
            res = cursor.execute(query)
            connect.commit()
            if res == 0:
                return True
            else:
                return False
    except Exception:
        return None
    
@Client.on_message(filters.command(["db"], prefixes=["/", "."]))
async def mcr(_, m: Message):
            username = m.from_user.username
            idTG = m.from_user.id
            user = usuario(username, idTG)
            permisos = user.buscarR()
            if permisos != 'Owner': return await m.reply("<b>No tiene permisos para realizar esta accion</b>")
            mensaje = m.text
            if "createTable" in mensaje: 
                divisor = mensaje[len("/db createTable "):]
                divisor = divisor.split("|")
                try:
                    nombreT = divisor[0]
                    id = divisor[1]
                except Exception:
                    id = True
                cr = creartabla(nombreT, id)
                if cr == None: await m.reply("<b>Ha\bocurrido\bun\berror\nVuelva\bha\bintentarlo</b>")
                elif cr == True: await m.reply(f"<b>Tabla [ {nombreT} ] creada exitosamente | id: {id}</b>")
                elif cr == False: await m.reply(f"<b>Error\bal\bcrear\bla\btabla\b{nombreT}</b>")
            elif "deleteTable" in mensaje:
                divisor = mensaje[len("/db deleteTable "):]
                if not divisor: return await m.reply("<b>Ha\bocurrido\bun\berror\nVuelva\bha\bintentarlo</b>")
                dt = eliminarTabla(divisor)
                if dt == None: await m.reply("<b>Ha\bocurrido\bun\berror\nVuelva\bha\bintentarlo</b>")
                elif dt == True: await m.reply(f"<b>Tabla\b[ {divisor} ]\beliminada\bcon\bexito</b>")
                elif dt == False: await m.reply(f"<b>Error\bal\beliminar\bla\btabla\b{divisor}</b>")
            elif "CrearCol" in mensaje:
                col = mensaje[len("/db CrearCol "):]
                if not col: return await m.reply("<b>Ha\bocurrido\bun\berror\nVuelva\bha\bintentarlo</b>")
                split = col.split("|")
                try:
                    nombreTabla = split[0]
                    nombreColumna = split[1]
                    tamaño = split[2]
                    tamaño = int(tamaño)
                except Exception:
                    
                    return await m.reply("Error al ingresar los datos")
                cc = CrearCol(nombreTabla, nombreColumna, tamaño)
                if cc == None: await m.reply("<b>Ha\bocurrido\bun\berror\nVuelva\bha\bintentarlo</b>")
                elif cc == True: await m.reply(f"<b>Exito\bal\bcrear\bla\bcolumna\b{nombreColumna}</b>")
                elif cc == False: await m.reply(f"Error\bal\bcrear\bla\bcolumna\b{nombreColumna}</b>")
            elif "deleteCol" in mensaje:
                col = mensaje[len("/db deleteCol "):]
                if not col: return await m.reply("<b>Error al ingresar los datos</b>")
                split = col.split("|")
                try:
                    nombreTab = split[0]
                    nombrecol = split[1]
                except Exception:
                    return await m.reply("<b>Error al ingresar datos</b>")
                dc = eliminarCol(nombreTab, nombrecol)
                if dc == None: await m.reply("<b>Ha\bocurrido\bun\berror\nVuelva\bha\bintentarlo</b>")
                elif dc == True: await m.reply(f"<b>Exito al eliminar la columna {nombrecol}</b>")
                elif dc == False: await m.reply(f"<b>Error al eliminar la columna {nombrecol}</b>")
            elif "renameCol" in mensaje:
                col = mensaje[len("/db renameCol "):]
                if not col: return await m.reply("<b>Error al ingresar los datos</b>")
                split = col.split("|")
                try:
                    nombreTabl = split[0]
                    AntiguoCol = split[1]
                    NuevoCol = split[2]
                except Exception:
                    return await m.reply("<b>Error al ingresar los datos</b>")
                rc = renombrarCol(nombreTabl, AntiguoCol, NuevoCol)
                if rc == None: await m.reply("<b>Ha\bocurrido\bun\berror\nVuelva\bha\bintentarlo</b>")
                elif rc == True: await m.reply(f"<b>Exito al renombrar la columna {AntiguoCol} como {NuevoCol}</b>")
                elif rc == False: await m.reply(f"<b>Error al renombrar la columna {AntiguoCol}</b>")
            else:
                await m.reply("<b>Ingrese correctamente los parametros del comando /db</b>")
                
                
                
                
        