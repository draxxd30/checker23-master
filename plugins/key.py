import random
import string
from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.clases.usuarios import usuario
import plugins.sql.keys as keys

 
def gen_key(text):
    src = True
    while src!=False:
        key_=keys.generar_key()
        src = keys.buscarKey(key_)
    mensaje = text[len("/key "):]
    mensaje = mensaje.replace("/", "|")
    mensaje = mensaje.replace("-", "|")
    mensaje = mensaje.replace(":", "|")
    split = mensaje.split("|")
    ad_Key = ""
    try:
        tiempo = split[0]
    except:
        tiempo = None
    if not tiempo: ad_Key = keys.añadirKey(key_)
    else:
      ad_Key = keys.añadirKey(key_, tiempo)
    if ad_Key!=True: return
    return key_


@Client.on_message(filters.command(["key"], prefixes=["/", "."]))
async def key(_, m: Message):
    user = m.from_user.username
    id = m.from_user.id
    user = usuario(user, id)
    rango = user.buscar()
    if not rango or rango == False: return await m.reply('<b>Usuario no registrado porfavor registrese con /start</b>')
    if rango[2] == 'Free' or rango[2] == 'Premium': return await m.reply("𝐘𝐨𝐮 𝐧𝐞𝐞𝐝 𝐭𝐨 𝐛𝐞 𝐚𝐝𝐦𝐢𝐧 𝐭𝐨 𝐮𝐬𝐞 𝐭𝐡𝐢𝐬 𝐜𝐨𝐦𝐦𝐚𝐧𝐝")
    key_ = gen_key(m.text)
    if not key_: return await m.reply('𝐄𝐫𝐫𝐨𝐫 𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐭𝐡𝐞 𝐤𝐞𝐲')
    await m.reply(f'𝐊𝐞𝐲 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝, 𝐲𝐨𝐮𝐫 𝐤𝐞𝐲 𝐢𝐬: <code>{key_}</code>')