import random
import string
from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.clases.usuarios import usuario
import plugins.sql.keys as keys


@Client.on_message(filters.command(["dkey"], prefixes=["/", "."]))
async def key(_, m: Message):
    nombre = m.from_user.username
    id = m.from_user.id
    user = usuario(nombre, id)
    rango = user.buscar()
    if not rango or rango == False: return await m.reply('<b>Usurio no registrado, registrese con /start</b>')
    if rango[2] == 'Free' or rango[2] == 'Premium': return await m.reply('<b>Necesita ser administrador para eliminar una key</b>')
    key = m.text[len("/dkey "):]
    if key.startswith("ckey-") == False: return await m.reply("<b>Ingrese una key valida</b>")
    if len(key) != 25: return await m.reply("<b>Ingrese una key valida</b>")
    delKey = keys.delKey(key)
    if not delKey: return await m.reply('<b>Error al eliminar la key</b>')
    await m.reply(f"<b>Key [ {key} ] eliminada con exito</b>")