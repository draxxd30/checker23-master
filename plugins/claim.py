from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.clases.usuarios import usuario
import plugins.sql.keys as keys

@Client.on_message(filters.command(["claim"], prefixes=["/", "."]))
async def claim(_, m: Message):
    user = m.from_user.username
    id = m.from_user.id
    user = usuario(user, id)
    rango = user.buscar()
    if not rango or rango == False: return await m.reply('<b>Usurio no registrado porfavor registrse con /start</b>')
    if rango[2] == 'Owner' or rango[2] == 'Admin': return await m.reply('<b>Ustes es administrador, no tiene porque canjear una key</b>')
    elif rango[2] == 'Premium': return await m.reply('<b>Usted ya es un usuario premium</b>')
    key = m.text[len("/claim "):]
    if len(key) != 25: return await m.reply('<b>Ingrese una key valida</b>')
    if key.startswith("ckey-") == False: return await m.reply('<b>Ingrese una key valida</b>')
    srcKey = keys.buscarKey(key)
    if srcKey == False or srcKey == None: return await m.reply('<b>Key no existente, ingrese una key valida</b>')
    if srcKey[3] == 'True': return await m.reply('<b>Esta key ya se encuentra activa, ingrese otra que no este canjeada</b>')
    clmKey = keys.canjear(key, id)
    if clmKey !=True: return await m.reply('<b>Error al canjear la key, porfavor vuelva a intentarlo mas tarde</b>')
    datos = user.buscar()
    if datos[2] != 'Premium': return await m.reply('<b>Error al ingresar el rango premium</b>')
    await m.reply(f'<b>Key activada con exito, ahora es {datos[2]}</b>')