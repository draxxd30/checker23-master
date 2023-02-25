import MySQLdb
from configs import config
import random
import string
from plugins.clases.usuarios import usuario

def buscarKey(key):
    query = f"SELECT * FROM llaves WHERE Llave = '{key}'"
    try:
        with MySQLdb.connect(host = config.DB_HOST, user = config.DB_USER, password = config.DB_PASS, database = config.DB_NAME) as connect:
            cursor = connect.cursor()
            cursor.execute(query)
            res = cursor.fetchone()
            if not res: return False
            else: return res
    except Exception as e: return e
    
def generar_key(): 
  key = [] 
  for i in range(20): 
    key.append(random.choice(string.ascii_uppercase+string.digits))
  return "ckey-"+''.join(key)
    
def añadirKey(key, tiempo=30):
    query = f"INSERT INTO llaves (Llave, Tiempo, Status) VALUES ('{key}', '{tiempo}', 'False')"
    try:
        with MySQLdb.connect(host = config.DB_HOST, user = config.DB_USER, password = config.DB_PASS, database = config.DB_NAME) as connect:
            cursor = connect.cursor()
            re = cursor.execute(query)
            connect.commit()
            if re == 1: return True
            else: False
    except Exception: return None
    
def canjear(key, id):
    query = f"UPDATE llaves SET Status = 'True' WHERE Llave = '{key}'"
    queryP = f"UPDATE usuarios SET rango = 'Premium' WHERE idTG = '{id}'"
    try:
        with MySQLdb.connect(host = config.DB_HOST, user = config.DB_USER, password = config.DB_PASS, database = config.DB_NAME) as connect:
            cursor = connect.cursor()
            re1 = cursor.execute(query)
            connect.commit()
            if re1 !=1: return False
            re2 = cursor.execute(queryP)
            connect.commit()
            if re2 !=1: return False
            if re1 ==1 and re2 == 1: return True
    except Exception: return None

def delKey(key):
    query = f"DELETE FROM llaves WHERE Llave = '{key}'"
    try:
        with MySQLdb.connect(host = config.DB_HOST, user = config.DB_USER, password = config.DB_PASS, database = config.DB_NAME) as connect:
            cursor = connect.cursor()
            re = cursor.execute(query)
            connect.commit()
            if re == 1: return True
            else: return
    except Exception: return