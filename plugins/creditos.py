import requests
from requests.exceptions import HTTPError, ProxyError
import re
import base64
import os
import time
import json
import string
import random
import httpx
import pymongo
import logging
import pyrogram
from plugins.clases.usuarios import usuario

from pyrogram import Client, filters
#from configs import config
from asyncio import sleep
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
import SQLaccounts

@Client.on_message(filters.command(["creditos", "créditos"], prefixes=["/", "."]))
async def mcr(_, m: Message):
    id = m.from_user.id
    username = m.from_user.username
    user = usuario(username, id)
    datos = user.buscar()
    if not datos or datos == False: return await m.reply('<b>Usuario no registrado porfavor registrese con /start')
    if datos[2] == "Free" or datos[2] == "Premium":
        return await m.reply("𝐘𝐨𝐮 𝐧𝐞𝐞𝐝 𝐭𝐨 𝐛𝐞 𝐚𝐝𝐦𝐢𝐧 𝐭𝐨 𝐮𝐬𝐞 𝐭𝐡𝐢𝐬 𝐜𝐨𝐦𝐦𝐚𝐧𝐝")
    msj = m.text[len("/creditos "):]
    mensaje = msj.replace("/", "|")
    mensaje = mensaje.replace(":", "|")
    mensaje = mensaje.replace("-", "|")
    split = mensaje.split("|")
    ID = split[0]
    cr = split[1]

    #if not cr:
        #return await m.reply(f"𝐓𝐡𝐞 𝐚𝐦𝐨𝐮𝐧𝐭 𝐨𝐟 {cr} 𝐢𝐬 𝐢𝐧𝐯𝐚𝐥𝐢𝐝")
    #if cr is not int:
        #return await m.reply(f"𝐓𝐡𝐞 𝐚𝐦𝐨𝐮𝐧𝐭 𝐨𝐟 {cr} 𝐢𝐬 𝐢𝐧𝐯𝐚𝐥𝐢𝐝")
    
    if not cr:
        cr = ID
        ID = m.from_user.username
        if cr.upper().startswith("-"):
            cr = cr.replace("-", "")
            query1 = "SELECT * FROM usuarios WHERE idTG = '{0}'".format(ID)
            resultado1 = SQLaccounts.run_query(query=query1)

            if int(resultado1[3]) == 0:
                return await m.reply(f"𝐓𝐡𝐞 𝐈𝐃 [ <code>{resultado1[4]}</code> ] 𝐚𝐥𝐫𝐞𝐚𝐝𝐲 𝐡𝐚𝐬 {resultado1[3]} 𝐜𝐫𝐞𝐝𝐢𝐭𝐬")
            else:
                creditosF = (f"{int(resultado1[3]) - int(cr)}")
                query = """UPDATE usuarios SET creditos = {0} WHERE idTG = '{1}'""".format(creditosF, ID)
                resultado2 = SQLaccounts.run_query(query=query)
                resultado3 = SQLaccounts.run_query(query=query1)
                
                
                if int(resultado3[3]) < 0:
                    query0 = """UPDATE usuarios SET creditos = "0" WHERE idTG = '{0}'""".format(ID)
                    poner0 = SQLaccounts.run_query(query=query0)
                    cambio0 = SQLaccounts.run_query(query=query1)
                    await m.reply(f"𝐓𝐡𝐞 𝐜𝐫𝐞𝐝𝐢𝐭𝐬 𝐨𝐟 𝐭𝐡𝐞 𝐈𝐃 [ <code>{resultado3[4]}</code> ] 𝐡𝐚𝐯𝐞 𝐛𝐞𝐞𝐧 𝐥𝐞𝐟𝐭 𝐚𝐭 {cambio0[3]}")
                else:
                    await m.reply(f"𝐓𝐡𝐞 𝐜𝐫𝐞𝐝𝐢𝐭𝐬 𝐨𝐟 𝐭𝐡𝐞 𝐈𝐃 [ <code>{resultado3[4]}</code> ] 𝐡𝐚𝐯𝐞 𝐛𝐞𝐞𝐧 𝐫𝐞𝐝𝐮𝐜𝐞𝐝 𝐭𝐨 {resultado3[3]}")
        
        else:
            query1 = "SELECT * FROM usuarios WHERE idTG = '{0}'".format(ID)
            resultado1 = SQLaccounts.run_query(query=query1)

            creditosF = (f"{int(resultado1[3]) + int(cr)}")
            
            query = """UPDATE usuarios SET creditos = {0} WHERE idTG = '{1}'""".format(creditosF, ID)
            resultado2 = SQLaccounts.run_query(query=query)

            resultado3 = SQLaccounts.run_query(query=query1)
            
            await m.reply(f"𝐓𝐡𝐞 𝐜𝐫𝐞𝐝𝐢𝐭𝐬 𝐨𝐟 𝐭𝐡𝐞 𝐈𝐃 [ <code>{resultado3[4]}</code> ] 𝐡𝐚𝐯𝐞 𝐢𝐧𝐜𝐫𝐞𝐚𝐬𝐞𝐝 𝐭𝐨 {resultado3[3]}")
    else:
        if cr.upper().startswith("-"):
            cr = cr.replace("-", "")
            query1 = "SELECT * FROM usuarios WHERE idTG = '{0}'".format(ID)
            resultado1 = SQLaccounts.run_query(query=query1)

            if int(resultado1[3]) == 0:
                return await m.reply(f"𝐓𝐡𝐞 𝐈𝐃 [ <code>{resultado1[4]}</code> ] 𝐚𝐥𝐫𝐞𝐚𝐝𝐲 𝐡𝐚𝐬 {resultado1[3]} 𝐜𝐫𝐞𝐝𝐢𝐭𝐬")
            else:
                creditosF = (f"{int(resultado1[3]) - int(cr)}")
                query = """UPDATE usuarios SET creditos = {0} WHERE idTG = '{1}'""".format(creditosF, ID)
                resultado2 = SQLaccounts.run_query(query=query)
                resultado3 = SQLaccounts.run_query(query=query1)
                
                
                if int(resultado3[3]) < 0:
                    query0 = """UPDATE usuarios SET creditos = "0" WHERE idTG = '{0}'""".format(ID)
                    poner0 = SQLaccounts.run_query(query=query0)
                    cambio0 = SQLaccounts.run_query(query=query1)
                    await m.reply(f"𝐓𝐡𝐞 𝐜𝐫𝐞𝐝𝐢𝐭𝐬 𝐨𝐟 𝐭𝐡𝐞 𝐈𝐃 [ <code>{resultado3[4]}</code> ] 𝐡𝐚𝐯𝐞 𝐛𝐞𝐞𝐧 𝐥𝐞𝐟𝐭 𝐚𝐭 {cambio0[3]}")
                else:
                    await m.reply(f"𝐓𝐡𝐞 𝐜𝐫𝐞𝐝𝐢𝐭𝐬 𝐨𝐟 𝐭𝐡𝐞 𝐈𝐃 [ <code>{resultado3[4]}</code> ] 𝐡𝐚𝐯𝐞 𝐛𝐞𝐞𝐧 𝐫𝐞𝐝𝐮𝐜𝐞𝐝 𝐭𝐨 {resultado3[3]}")
            
        else:
            query1 = "SELECT * FROM usuarios WHERE idTG = '{0}'".format(ID)
            resultado1 = SQLaccounts.run_query(query=query1)

            creditosF = (f"{int(resultado1[3]) + int(cr)}")
            
            query = """UPDATE usuarios SET creditos = {0} WHERE idTG = '{1}'""".format(creditosF, ID)
            resultado2 = SQLaccounts.run_query(query=query)

            resultado3 = SQLaccounts.run_query(query=query1)
            
            await m.reply(f"𝐓𝐡𝐞 𝐜𝐫𝐞𝐝𝐢𝐭𝐬 𝐨𝐟 𝐭𝐡𝐞 𝐈𝐃 [ <code>{resultado3[4]}</code> ] 𝐡𝐚𝐯𝐞 𝐢𝐧𝐜𝐫𝐞𝐚𝐬𝐞𝐝 𝐭𝐨 {resultado3[3]}")
        




     

    #crsuma = SQLaccounts.run_query(query=query)


    