from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.clases.usuarios import usuario
import re
    
@Client.on_message(filters.command(["src"], prefixes=["/", "."]))
async def mcr(_, m: Message):
    nombreR = None
    nombre = m.from_user.username
    id_command = m.from_user.id
    user_command = usuario(nombre=nombre, id=id_command)
    rango = user_command.buscar()
    if not rango or rango == False: return await m.reply('<b>Usuario no registrado porfavor registrse</b>')
    if rango[2] != 'Owner':
        if rango != 'Admin': return await m.reply('No\btiene\brango\bpara\brealizar\besta\bbusqueda')
    id = re.search(r"\d{10}", m.text)
    try:
        id = id[0]
    except Exception:
        id = None
    if not id: 
        nombreR = re.search(r"@[a-zA-Z0-9]+", m.text)
        try:
            nombreR = nombreR[0]
        except Exception:
            nombreR = None
        if not nombreR: return await m.reply('<b>No\bse\bingresaron\bbien\blos\bdatos</b>')
        nombreR = nombreR.replace("@", "")
    user = usuario(nombre=nombreR, id=id)
    if id != None: datos = user.buscar()
    if id == None: datos = user.buscarUser()
    if datos == False: return await m.reply('<b>Usuario\bno\bregistrado</b>')
    try:
        nombreU = datos[1]
        rangoI = datos[2]
        Creditos = datos[3]
        idU = datos[4]
        rangoP = datos[5]
        rangoPP = f" | {rangoP}"
        if rangoP == None: rangoPP = ""
    except Exception:
        return await m.reply('<b>Error\bal\brecibir\bdatos</b>')
    texto = f"""<b>Usuario\bencontrado\b✅\nusuario:\b<code>{nombreU}</code>\nrango:\b{rangoI}{rangoPP}\ncreditos:\b{Creditos}\nid:\b[\b<code>{idU}</code>\b]</b>"""
    await m.reply(texto)    