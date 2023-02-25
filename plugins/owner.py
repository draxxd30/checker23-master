import json
import requests
import time
import asyncio
import random
from luhn import verify
from plugins.clases.usuarios import usuario

from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
import SQLaccounts


@Client.on_message(filters.command(["own"], prefixes=["/", "."]))
async def premium(_, m: Message):
    id = m.from_user.id
    username = m.from_user.username
    user = usuario(username, id)
    datos = user.buscar()
    if not datos or datos == False: return await m.reply('<b>Usuario no registrado porfavor registrese con /start</b>')
    if datos[2] != "Owner":
        return await m.reply("<b>Necesita ser Owner para utilizar este comando</b>")
    
    ID = m.text[len("/own "):]
    if not ID:
        return await m.reply("Ingrese ID valido")

    queryOwner = """UPDATE usuarios SET rango = "Owner" WHERE idTG = '{0}'""".format(ID)
    OwnerSQL = SQLaccounts.run_query(query=queryOwner)

    queryOwnerMV = f"""SELECT rangoM FROM usuarios WHERE idTG = '{ID}'"""
    VerSQL2 = SQLaccounts.run_query(queryOwnerMV)

    if VerSQL2[0] == "NULL" or VerSQL2[0] == "Premium" or VerSQL2[0] == "Free" or VerSQL2[0] == "Admin":
        queryUpdate = f"UPDATE usuarios SET rangoM = 'Owner' WHERE idTG = '{ID}'"
        updateSQL = SQLaccounts.run_query(queryUpdate)

    queryVer = "SELECT * FROM usuarios WHERE idTG = '{0}'".format(ID)
    VerSQL = SQLaccounts.run_query(query=queryVer)
    
    if VerSQL[2] == "Owner":
       await m.reply(f"<b>Rango owner agregado exitosamente al id [ <code>{VerSQL[4]}</code> ]</b>")
    
    else:
        await m.reply(f"<b>A ocurrido un error al cambiar el rango del id [ <code>{VerSQL[4]}</code> ]</b>")
