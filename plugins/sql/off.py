from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.sql.gates import off, buscarT


@Client.on_message(filters.command(["off"], prefixes=["/", "."]))
async def bin(_, m: Message):
        msj7 = m.text[len("/off "):]
        if not msj7: return await m.reply("<b>Ingrese parametros validos</b>")
        mensaje = msj7.replace("/","|")
        mensaje = mensaje.replace(":","|")
        mensaje = mensaje.replace("-","|")
        split = mensaje.split("|")
        try:
            nombre_gate = split[0]
            try:
                razon = split[1]
            except Exception: razon = None
        except Exception: return await m.reply("<b>Ingrese correctamente los datos</b>")
        st = off(nombre_gate, razon)
        if st == False or st == None: return await m.reply("<b>Error al actualizar el estado del gate</b>")
        gate = buscarT(nombre_gate)
        if gate == None or gate == False: return await m.reply("<b>Error al actualizar el estado del gate</b>")
        if razon == None:
            text_Actu = f"<b>Status del gate actualizado\nNombre: {gate[1]}\nStatus: {gate[2]}\nMensaje: {gate[3]}</b>"
        else:
            text_Actu = f"<b>Status y Mensaje del Gate actualizados\nNombre: {gate[1]}\nStatus: {gate[2]}\nMensaje: {gate[3]}</b>"
        await m.reply(text_Actu)