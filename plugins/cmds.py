import json
import requests
import time
import asyncio
from plugins.clases.usuarios import usuario
from plugins.sql.gates import listaAndDatos
from plugins.sql.config import configIdioma

from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import (
   Message,
   InlineKeyboardButton,
   InlineKeyboardMarkup,
   CallbackQuery
   )
textoInicial = "𝐇𝐞𝐥𝐥𝐨, 𝐭𝐡𝐞𝐬𝐞 𝐚𝐫𝐞 𝐚𝐥𝐥 𝐭𝐡𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐜𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐚𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞.\n𝐁𝐫𝐨𝐰𝐬𝐞 𝐭𝐡𝐞 𝐛𝐮𝐭𝐭𝐨𝐧𝐬 𝐭𝐨 𝐯𝐢𝐞𝐰 𝐭𝐡𝐞𝐦."
nuevo = [[InlineKeyboardButton("Tools", callback_data="tools"), InlineKeyboardButton("Gates", callback_data='Gates'), InlineKeyboardButton("CCN Charged", url="https://t.me/none")]]
reply_markupInicio = InlineKeyboardMarkup(nuevo)
@Client.on_message(filters.command(["cmds"], prefixes=["/", "."]))
async def cmds(_, m: Message):
    username = m.from_user.username
    id = m.from_user.id
    user = usuario(username, id)
    datos = user.buscar()
    if not datos or datos == False: return await m.send_message(Message.chat.id, '<b>Usuario no registrado porfavor registrse con /start</b>')
    texto = """
𝐇𝐞𝐥𝐥𝐨, 𝐭𝐡𝐞𝐬𝐞 𝐚𝐫𝐞 𝐚𝐥𝐥 𝐭𝐡𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐜𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐚𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞.\n𝐁𝐫𝐨𝐰𝐬𝐞 𝐭𝐡𝐞 𝐛𝐮𝐭𝐭𝐨𝐧𝐬 𝐭𝐨 𝐯𝐢𝐞𝐰 𝐭𝐡𝐞𝐦.   
"""
    nuevo = [[InlineKeyboardButton("Tools", callback_data="tools"), InlineKeyboardButton("Gates", callback_data='Gates'), InlineKeyboardButton("CCN Charged", url="https://t.me/none")]]
    reply_markupInicio = InlineKeyboardMarkup(nuevo)
    await m.reply(texto, reply_markup=reply_markupInicio)

@Client.on_callback_query()
async def query(cl: Client, cb: CallbackQuery):
    if cb.data == "Gates":
        texto = '<b>Gates disponibles</b>\n\n'
        gates = listaAndDatos()
        #print(gates)
        for nombre in gates:
            try:
                gate = nombre[4]
                status = nombre[2]
                command = nombre[1]
            except Exception: return await cb.answer('Error') 
            if status == 'off': status = '❌'
            elif status == 'on': status = '✅'
            texto = str(texto)+f'<b>{gate}|{command}</b>'+' '+f'<b>{status}</b>'+'\n\n'
            
        reply_markup2 = InlineKeyboardMarkup([[InlineKeyboardButton("atras", callback_data="inicio")]])
        await cb.edit_message_text(texto, reply_markup=reply_markup2)
        
    elif cb.data == 'inicio':
        await cb.edit_message_text(textoInicial, reply_markup=reply_markupInicio)
        
    elif cb.data == 'commansStart':
        reply_markup_atrascommandsStart = InlineKeyboardMarkup([[InlineKeyboardButton("Tools", callback_data="tools"), InlineKeyboardButton("Gates", callback_data='Gates'), InlineKeyboardButton("CCN Charged", url="https://t.me/none")], [InlineKeyboardButton('Atras', callback_data='inicioStart')]])
        await cb.edit_message_text('𝐭𝐡𝐞𝐬𝐞 𝐚𝐫𝐞 𝐚𝐥𝐥 𝐭𝐡𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐜𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐚𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞.\n𝐁𝐫𝐨𝐰𝐬𝐞 𝐭𝐡𝐞 𝐛𝐮𝐭𝐭𝐨𝐧𝐬 𝐭𝐨 𝐯𝐢𝐞𝐰 𝐭𝐡𝐞𝐦.', reply_markup=reply_markup_atrascommandsStart)
    #elif cb.data == "idioma":
    #    idiomaMarkup = InlineKeyboardMarkup([[InlineKeyboardButton("Español", callback_data="Español")], [InlineKeyboardButton("Inglish", callback_data="ingles")]])
    #    await cb.edit_message_text('<b>select the language you want to see</b>', reply_markup=idiomaMarkup)
    #elif cb.data == 'Español': 
    #    cambio = configIdioma('es', cb.from_user.username, cb.from_user.id)
    #    replymarkupIdioma = InlineKeyboardMarkup([[InlineKeyboardButton("inicio", callback_data="inicioStart")]])
    #    await cb.edit_message_text(cambio, reply_markup=replymarkupIdioma)
    #elif cb.data == 'ingles':
    #    cambio = configIdioma('en', cb.from_user.username, cb.from_user.id)
    #    replymarkupIdioma = InlineKeyboardMarkup([[InlineKeyboardButton("inicio", callback_data="inicioStart")]])
    #    await cb.edit_message_text(cambio, reply_markup=replymarkupIdioma)
    elif cb.data == 'inicioStart':
        await cb.edit_message_text(f"""𝐖𝐞𝐥𝐜𝐨𝐦𝐞 @{cb.from_user.username} 𝐮𝐬𝐞 /cmds 𝐭𝐨 𝐯𝐢𝐞𝐰 𝐚𝐥𝐥 𝐚𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬.""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Owner", url="https://t.me/Draxxd30"),InlineKeyboardButton("Commands", callback_data='commansStart')]]))
