import MySQLdb
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from configs import config
from plugins.clases.usuarios import usuario

def actuName(Nombre,NombreN):
    query=f"UPDATE gates SET Gate = '{NombreN}' where Gate = '{Nombre}'"
    try:
        with MySQLdb.connect(host = config.DB_HOST, user = config.DB_USER, password = config.DB_PASS, database = config.DB_NAME) as connect:
            cursor = connect.cursor()
            re = cursor.execute(query)
            connect.commit()
            if re == 1: return True
            else: return False
    except Exception: return None
def buscarT(nombre):
    query=f"SELECT * FROM gates WHERE Nombre = '{nombre}'"
    query1=f"SELECT * FROM gates WHERE Gate = '{nombre}'"
    try: 
        with MySQLdb.connect(host = config.DB_HOST, user = config.DB_USER, password = config.DB_PASS, database = config.DB_NAME) as connect:
            cursor = connect.cursor()
            cursor.execute(query)
            re = cursor.fetchone()
            if re == None: 
                cursor.execute(query1)
                re = cursor.fetchone()
                if re == None: return False
                else: return re
            else: return re
    except Exception: return None    
def buscar(nombre):
    query=f"SELECT * FROM gates WHERE Gate = '{nombre}'"
    try: 
        with MySQLdb.connect(host = config.DB_HOST, user = config.DB_USER, password = config.DB_PASS, database = config.DB_NAME) as connect:
            cursor = connect.cursor()
            cursor.execute(query)
            re = cursor.fetchone()
            if re == None: return False
            else: return True
    except Exception: return None
def añadir(nombre, status, message):
    query = f"INSERT INTO gates (Gate, Status, Mensaje) VALUES ('{nombre}', '{status}', '{message}')"
    try:
        with MySQLdb.connect(host = config.DB_HOST, user = config.DB_USER, password = config.DB_PASS, database = config.DB_NAME) as connect:
            cursor = connect.cursor()
            re = cursor.execute(query)
            connect.commit()
            if re == 1: return True
            else: return False
    except Exception: return None
    
def eliminar(nombre):
    query = f"DELETE FROM gates WHERE Gate = '{nombre}'"
    try:
        with MySQLdb.connect(host = config.DB_HOST, user = config.DB_USER, password = config.DB_PASS, database = config.DB_NAME) as connect:
            cursor = connect.cursor()
            re = cursor.execute(query)
            connect.commit()
            if re  == 1: return True
            else: return False
    except Exception: return None
def off(nombre, razon=None):
    query = f"UPDATE gates SET Status = 'off', Mensaje = '{razon}' WHERE Gate = '{nombre}'"
    if razon == None: query = f"UPDATE gates SET Status = 'off' WHERE Gate = '{nombre}'"
    try:
        with MySQLdb.connect(host = config.DB_HOST, user = config.DB_USER, password = config.DB_PASS, database = config.DB_NAME) as connect:
            cursor = connect.cursor()
            res = cursor.execute(query)
            connect.commit()
            if res == 1: return True
            else: return False
    except Exception: return None
def on(nombre):
    query = f"UPDATE gates SET Status = 'on', Mensaje = '' WHERE Gate = '{nombre}'"
    try:
        with MySQLdb.connect(host = config.DB_HOST, user = config.DB_USER, password = config.DB_PASS, database = config.DB_NAME) as connect:
            cursor = connect.cursor()
            re = cursor.execute(query)
            connect.commit()
            if re == 1: return True
            else: return False
    except Exception: return None
def actuStatus(nombre, status, message=None):
    query = f"UPDATE gates SET status = '{status}' where Gate = '{nombre}'"
    if message != None: query = f"UPDATE gates SET status = '{status}', Mensaje = '{message}' WHERE Gate = '{nombre}'"
    try:
        with MySQLdb.connect(host = config.DB_HOST, user = config.DB_USER, password = config.DB_PASS, database = config.DB_NAME) as connect:
            cursor = connect.cursor()
            re = cursor.execute(query)
            connect.commit()
            if re == 1: return True
            else: return False
    except Exception: return None
def cambiarMensaje(nombre, NewMessage):
    query = f"UPDATE gates SET Mensaje = '{NewMessage}' WHERE Gate = '{nombre}'"
    try:
        with MySQLdb.connect(host = config.DB_HOST, user = config.DB_USER, password = config.DB_PASS, database = config.DB_NAME) as connect:
            cursor = connect.cursor()
            re = cursor.execute(query)
            connect.commit()
            if re == 1: return True
            else: return False
    except Exception: return None

def listaAndDatos():
    query = 'Select * from gates'
    try:
        with MySQLdb.connect(host = config.DB_HOST, user = config.DB_USER, password = config.DB_PASS, database = config.DB_NAME) as connect:
            cursor = connect.cursor()
            cursor.execute(query)
            re = cursor.fetchall()
            if not re: return False
            return re
    except Exception: return None
    
@Client.on_message(filters.command(["gate"], prefixes=["/", "."]))
async def bin(_, m: Message):
    user_Remi, id_Remi = m.from_user.username, m.from_user.id
    remi = usuario(user_Remi, id_Remi)
    rango = remi.buscarR()
    if rango != 'Owner':
        if rango != 'Admin': return await m.reply("<b>Nececita\bser\badmin\bpara\butilizar\beste\bcomando</b>")
    mensaje = m.text
    if 'CrearGate' in mensaje:
        msj = mensaje[len("/gate CrearGate "):]
        if not msj: return await m.reply('<b>Ingrese parametros validos</b>')
        mensaje = msj.replace("/","|")
        mensaje = mensaje.replace(":","|")
        mensaje = mensaje.replace("-","|")
        split = mensaje.split("|")
        try:
            name = split[0]
            status = split[1]
            try:
                message = split[2]
            except Exception: message=None
        except Exception: return await m.reply('<b>Ha\bocurrido\bun\berror</b>')
        exist = buscar(name)
        if exist == True: return await m.reply('<b>Gate\bya\bexistente</b>')
        new_Gate = añadir(name, status, message)
        if new_Gate == True: 
            gate = buscarT(name)
            if gate == None or gate == False: return await m.reply('<b>Error\bal\bagregar\bel\bgate</b>')
            texto = f"<b>Gate creado con exito\nNombre: {gate[1]}\nStatus: {gate[2]}\nMensaje: {gate[3]}</b>"
            await m.reply(texto)
        else: await m.reply('<b>error</b>')
    elif 'ActuMensaje' in mensaje:
        msj6 = mensaje[len("/gate ActuMensaje "):]
        if not msj6: return await m.reply('<b>Ingrese parametros validos</b>')
        mensaje = msj6.replace("/","|")
        mensaje = mensaje.replace(":","|")
        mensaje = mensaje.replace("-","|")
        split = mensaje.split("|")
        try:
            nombre_Gate = split[0]
            estado = split[1]
        except Exception: return await m.reply("<b>Error al capturar los datos, revise los parametros enviados</b>")
        actu = cambiarMensaje(nombre_Gate, estado)
        if actu == None or actu == False: return await m.reply("<b>Error al actualizar el mensaje</b>")
        gate1 = buscarT(nombre_Gate)
        if gate1 == None or gate1 == False: return await m.reply("<b>Error al actualizar el mensaje</b>")
        texto = f"<b>Mensaje del Gate actualizado con exito\nNombre: {gate1[1]}\nStatus: {gate1[2]}\nMensaje: {gate1[3]}</b>"
        await m.reply(texto)
    elif 'Delete' in mensaje:
            msj8 = mensaje[len("/gate Delete "):]
            if not msj8: return await m.reply("<b>Ingrese correctamente los datos</b>")
            nombreGATE = msj8
            borrar = eliminar(nombreGATE)
            if borrar == False or borrar == None: return await m.reply(f"<b>Error al eliminar el gate [ {nombreGATE} ]</b>")
            gt = buscarT(nombreGATE)
            if gt != False: return await m.reply(f"<b>Error al eliminar el gate [ {nombreGATE} ]</b>")
            text = f"<b>Gate [ {nombreGATE} ] eliminado con exito</b>"
            await m.reply(text)
    elif 'Name' in mensaje:
            msj9 = mensaje[len("/gate Name "):]
            if not msj9: return await m.reply(f"<b>Error al ingresar los datos</b>")
            mensaje = msj9.replace("/","|")
            mensaje = mensaje.replace(":","|")
            mensaje = mensaje.replace("-","|")
            split = mensaje.split("|")
            try:
                nombreV = split[0]
                nombreN = split[1]
            except Exception: return await m.reply("<b>Error al ingresar los datos</b>")
            gtn = actuName(nombreV, nombreN)
            if gtn != True: return await m.reply("<b>Error al actualizar el nombre del gate</b>")
            gtn1 = buscarT(nombreN)
            if gtn1 == False or gtn1 == None: return await m.reply("<b>Error al actualizar el nombre del gate</b>")
            text1 = f"<b>Nombre del gate actualizado\nNombre: [ A: {nombreV}|N: {gtn1[1]} ]\nStatus: {gtn1[2]}\nMensaje: {gtn1[3]}</b>"
            await m.reply(text1)
    else:
            gate10 = mensaje[len("/gate "):]
            if not gate10: return await m.reply("<b>Datos invalidos porfavor ingrese el nombre de un gate o algun subcomando existente</b>")
            bsGate = buscarT(gate10)
            if bsGate == False: return await m.reply("<b>Gate no existente</b>")
            elif bsGate == None: return await m.reply("<b>Error al buscar el gate</b>")
            status = bsGate[2]
            mensaje = bsGate[3] 
            if status == 'on': status = 'on ✅'
            elif status == 'off': status = 'off ❌'
            if mensaje == '':
                text = f"<b>Name:</b> {bsGate[4]}\n<b>Command:</b> {bsGate[1]}\n<b>Status:</b> {status}"
            else:
                text = f"<b>Name:</b> {bsGate[4]}\n<b>Command:</b> {bsGate[1]}\n<b>Status:</b> {status}\n<b>Message:</b> {bsGate[3]}"
            await m.reply(text)



