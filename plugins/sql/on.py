from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.sql.gates import buscar, buscarT, on


@Client.on_message(filters.command(["on"], prefixes=["/", "."]))
async def bin(_, m: Message):
    msj = m.text[len("/on "):]
    nombre = msj
    src = buscar(nombre)
    if src != True: return await m.reply('<b>Gate no encontrado</b>')
    src2 = on(nombre)
    if src == False or src == None: return await m.reply('<b>Error al actualizar el Gate</b>')
    src3 = buscarT(nombre)
    if src3 == False or src3 == None: return await m.reply('<b>Error al actualizar el estado</b>')
    texto = f"<b>Gate ON\nNombre: {src3[1]}\nEstado: {src3[2]}</b>"
    await m.reply(texto)
    