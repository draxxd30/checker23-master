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

@Client.on_message(filters.command(["creditos", "crรฉditos"], prefixes=["/", "."]))
async def mcr(_, m: Message):
    id = m.from_user.id
    username = m.from_user.username
    user = usuario(username, id)
    datos = user.buscar()
    if not datos or datos == False: return await m.reply('<b>Usuario no registrado porfavor registrese con /start')
    if datos[2] == "Free" or datos[2] == "Premium":
        return await m.reply("๐๐จ๐ฎ ๐ง๐๐๐ ๐ญ๐จ ๐๐ ๐๐๐ฆ๐ข๐ง ๐ญ๐จ ๐ฎ๐ฌ๐ ๐ญ๐ก๐ข๐ฌ ๐๐จ๐ฆ๐ฆ๐๐ง๐")
    msj = m.text[len("/creditos "):]
    mensaje = msj.replace("/", "|")
    mensaje = mensaje.replace(":", "|")
    mensaje = mensaje.replace("-", "|")
    split = mensaje.split("|")
    ID = split[0]
    cr = split[1]

    #if not cr:
        #return await m.reply(f"๐๐ก๐ ๐๐ฆ๐จ๐ฎ๐ง๐ญ ๐จ๐ {cr} ๐ข๐ฌ ๐ข๐ง๐ฏ๐๐ฅ๐ข๐")
    #if cr is not int:
        #return await m.reply(f"๐๐ก๐ ๐๐ฆ๐จ๐ฎ๐ง๐ญ ๐จ๐ {cr} ๐ข๐ฌ ๐ข๐ง๐ฏ๐๐ฅ๐ข๐")
    
    if not cr:
        cr = ID
        ID = m.from_user.username
        if cr.upper().startswith("-"):
            cr = cr.replace("-", "")
            query1 = "SELECT * FROM usuarios WHERE idTG = '{0}'".format(ID)
            resultado1 = SQLaccounts.run_query(query=query1)

            if int(resultado1[3]) == 0:
                return await m.reply(f"๐๐ก๐ ๐๐ [ <code>{resultado1[4]}</code> ] ๐๐ฅ๐ซ๐๐๐๐ฒ ๐ก๐๐ฌ {resultado1[3]} ๐๐ซ๐๐๐ข๐ญ๐ฌ")
            else:
                creditosF = (f"{int(resultado1[3]) - int(cr)}")
                query = """UPDATE usuarios SET creditos = {0} WHERE idTG = '{1}'""".format(creditosF, ID)
                resultado2 = SQLaccounts.run_query(query=query)
                resultado3 = SQLaccounts.run_query(query=query1)
                
                
                if int(resultado3[3]) < 0:
                    query0 = """UPDATE usuarios SET creditos = "0" WHERE idTG = '{0}'""".format(ID)
                    poner0 = SQLaccounts.run_query(query=query0)
                    cambio0 = SQLaccounts.run_query(query=query1)
                    await m.reply(f"๐๐ก๐ ๐๐ซ๐๐๐ข๐ญ๐ฌ ๐จ๐ ๐ญ๐ก๐ ๐๐ [ <code>{resultado3[4]}</code> ] ๐ก๐๐ฏ๐ ๐๐๐๐ง ๐ฅ๐๐๐ญ ๐๐ญ {cambio0[3]}")
                else:
                    await m.reply(f"๐๐ก๐ ๐๐ซ๐๐๐ข๐ญ๐ฌ ๐จ๐ ๐ญ๐ก๐ ๐๐ [ <code>{resultado3[4]}</code> ] ๐ก๐๐ฏ๐ ๐๐๐๐ง ๐ซ๐๐๐ฎ๐๐๐ ๐ญ๐จ {resultado3[3]}")
        
        else:
            query1 = "SELECT * FROM usuarios WHERE idTG = '{0}'".format(ID)
            resultado1 = SQLaccounts.run_query(query=query1)

            creditosF = (f"{int(resultado1[3]) + int(cr)}")
            
            query = """UPDATE usuarios SET creditos = {0} WHERE idTG = '{1}'""".format(creditosF, ID)
            resultado2 = SQLaccounts.run_query(query=query)

            resultado3 = SQLaccounts.run_query(query=query1)
            
            await m.reply(f"๐๐ก๐ ๐๐ซ๐๐๐ข๐ญ๐ฌ ๐จ๐ ๐ญ๐ก๐ ๐๐ [ <code>{resultado3[4]}</code> ] ๐ก๐๐ฏ๐ ๐ข๐ง๐๐ซ๐๐๐ฌ๐๐ ๐ญ๐จ {resultado3[3]}")
    else:
        if cr.upper().startswith("-"):
            cr = cr.replace("-", "")
            query1 = "SELECT * FROM usuarios WHERE idTG = '{0}'".format(ID)
            resultado1 = SQLaccounts.run_query(query=query1)

            if int(resultado1[3]) == 0:
                return await m.reply(f"๐๐ก๐ ๐๐ [ <code>{resultado1[4]}</code> ] ๐๐ฅ๐ซ๐๐๐๐ฒ ๐ก๐๐ฌ {resultado1[3]} ๐๐ซ๐๐๐ข๐ญ๐ฌ")
            else:
                creditosF = (f"{int(resultado1[3]) - int(cr)}")
                query = """UPDATE usuarios SET creditos = {0} WHERE idTG = '{1}'""".format(creditosF, ID)
                resultado2 = SQLaccounts.run_query(query=query)
                resultado3 = SQLaccounts.run_query(query=query1)
                
                
                if int(resultado3[3]) < 0:
                    query0 = """UPDATE usuarios SET creditos = "0" WHERE idTG = '{0}'""".format(ID)
                    poner0 = SQLaccounts.run_query(query=query0)
                    cambio0 = SQLaccounts.run_query(query=query1)
                    await m.reply(f"๐๐ก๐ ๐๐ซ๐๐๐ข๐ญ๐ฌ ๐จ๐ ๐ญ๐ก๐ ๐๐ [ <code>{resultado3[4]}</code> ] ๐ก๐๐ฏ๐ ๐๐๐๐ง ๐ฅ๐๐๐ญ ๐๐ญ {cambio0[3]}")
                else:
                    await m.reply(f"๐๐ก๐ ๐๐ซ๐๐๐ข๐ญ๐ฌ ๐จ๐ ๐ญ๐ก๐ ๐๐ [ <code>{resultado3[4]}</code> ] ๐ก๐๐ฏ๐ ๐๐๐๐ง ๐ซ๐๐๐ฎ๐๐๐ ๐ญ๐จ {resultado3[3]}")
            
        else:
            query1 = "SELECT * FROM usuarios WHERE idTG = '{0}'".format(ID)
            resultado1 = SQLaccounts.run_query(query=query1)

            creditosF = (f"{int(resultado1[3]) + int(cr)}")
            
            query = """UPDATE usuarios SET creditos = {0} WHERE idTG = '{1}'""".format(creditosF, ID)
            resultado2 = SQLaccounts.run_query(query=query)

            resultado3 = SQLaccounts.run_query(query=query1)
            
            await m.reply(f"๐๐ก๐ ๐๐ซ๐๐๐ข๐ญ๐ฌ ๐จ๐ ๐ญ๐ก๐ ๐๐ [ <code>{resultado3[4]}</code> ] ๐ก๐๐ฏ๐ ๐ข๐ง๐๐ซ๐๐๐ฌ๐๐ ๐ญ๐จ {resultado3[3]}")
        




     

    #crsuma = SQLaccounts.run_query(query=query)


    