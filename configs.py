from os import path, getenv

class config:
    API_ID = int(getenv("API_ID",'24054386'))
    API_HASH = getenv("API_HASH",'6684db1e16988756df0d5c12ad3e6b09')
    BOT_TOKEN = getenv("BOT_TOKEN",'5895609920:AAGZML4udfhG2TfSft_jgL5Cds0Rgnkq_ks')
    DB_HOST = 'localhost' 
    DB_USER = 'root' 
    DB_PASS = '' 
    DB_NAME = 'accounts'

config = config()
