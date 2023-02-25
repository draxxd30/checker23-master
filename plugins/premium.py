import json
import requests
import time
import asyncio
import random
from luhn import verify
from plugins.clases.usuarios import usuario

from asyncio import sleep
from pyrogram import Client, filters
import MySQLdb
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
import SQLaccounts





@Client.on_message(filters.command(["premium"], prefixes=["/", "."]))
async def premium(_, m: Message):
    id = m.from_user.id
    username = m.from_user.username
    user = usuario(username, id)
    datos = user.buscar()
    if not datos or datos == False: return await m.reply('<b>Usuario no registrado porfavor registrese con /start</b>')
    if datos[2] == "Free" or datos[2] == "Premium":
        return await m.reply("𝐘𝐨𝐮 𝐧𝐞𝐞𝐝 𝐭𝐨 𝐛𝐞 𝐚𝐝𝐦𝐢𝐧 𝐭𝐨 𝐮𝐬𝐞 𝐭𝐡𝐢𝐬 𝐜𝐨𝐦𝐦𝐚𝐧𝐝")
    
    ID = m.text[len("/premium "):]
    if not ID:
        return await m.reply("𝐄𝐧𝐭𝐞𝐫 𝐚 𝐯𝐚𝐥𝐢𝐝 𝐈𝐃")

    queryVer = f"SELECT * FROM usuarios WHERE idTG = '{ID}'"
    queryver1 = SQLaccounts.run_query(queryVer)
    if str(queryver1).find("False") != -1:
        return await m.reply("𝐀𝐧 𝐮𝐧𝐞𝐱𝐩𝐞𝐜𝐭𝐞𝐝 𝐞𝐫𝐫𝐨𝐫 𝐨𝐜𝐜𝐮𝐫𝐫𝐞𝐝, 𝐭𝐫𝐲 𝐚𝐠𝐚𝐢𝐧 𝐥𝐚𝐭𝐞𝐫.")

    if queryver1[2] == "Admin" or queryver1[2] == "Owner":
        return await m.reply("𝐓𝐡𝐢𝐬 𝐩𝐞𝐫𝐬𝐨𝐧 𝐡𝐚𝐬 𝐚𝐝𝐦𝐢𝐧𝐢𝐬𝐭𝐫𝐚𝐭𝐨𝐫 𝐫𝐚𝐧𝐤") 

    queryPremium = """UPDATE usuarios SET rango = "Premium" WHERE idTG = '{0}'""".format(ID)
    premiumSQL = SQLaccounts.run_query(query=queryPremium)


    if queryver1[5] == "NULL" or queryver1[5] == "Free":
        queryUpdate = f"UPDATE usuarios SET rangoM = 'Premium' WHERE idTG = '{ID}'"
        updateSQL = SQLaccounts.run_query(queryUpdate)
    
    sqlver = "SELECT * FROM usuarios WHERE idTG = '{0}'".format(ID)
    VerSQL = SQLaccounts.run_query(query=sqlver)

    if VerSQL[2] == "Premium":
        await m.reply(f"𝐔𝐬𝐞𝐫 <code>{VerSQL[4]}</code> 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐮𝐩𝐠𝐫𝐚𝐝𝐞𝐝 𝐭𝐨 𝐩𝐫𝐞𝐦𝐢𝐮𝐦. ")
    
    else:
        await m.reply(f"𝐔𝐧𝐚𝐛𝐥𝐞 𝐭𝐨 𝐚𝐝𝐝 𝐩𝐫𝐞𝐦𝐢𝐮𝐦 𝐭𝐨 𝐭𝐡𝐞 𝐈𝐃  <code>{VerSQL[4]}</code> ")

        
       