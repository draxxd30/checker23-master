import MySQLdb
import pyrogram
from os import path, getenv

DB_HOST = 'localhost' 
DB_USER = 'root' 
DB_PASS = '' 
DB_NAME = 'accounts'

conn = MySQLdb.connect(host = DB_HOST, user = DB_USER, password = DB_PASS, database = DB_NAME)


def sqlFree(usuario, id):
    
            cursor = conn.cursor()
        
            sqlRegistrar = "INSERT INTO usuarios (usuario, rango, creditos, idTG) VALUES ('{0}', 'Free', '50', {1})".format(usuario, id)

            cursor.execute(sqlRegistrar)

            conn.commit()



def run_query(query=''): 
    
    try:
        with MySQLdb.connect(host = DB_HOST, user = DB_USER, password = DB_PASS, database = DB_NAME) as connect:
            cursor = connect.cursor()
            cursor.execute(query)
            
            if query.upper().startswith("SELECT"):
                data = cursor.fetchone()
            
            else:
                connect.commit()
                data = "completado"
                connect.close()

            return data
        
    except Exception as a:
        return {"status" :False}

def cambiarNombre(id, nombre):
                cursor = conn.cursor()
                
                query1 = f"SELECT * FROM usuarios WHERE idTG = '{id}'"
                query1A = cursor.execute(query1)
                query1B = cursor.fetchone()


                if query1B[5] == {nombre}:
                    resultado = "error1"
                    return resultado
                
                query2 = f"UPDATE usuarios SET rangoM = '{nombre}' WHERE idTG = '{id}'"
                query2E = cursor.execute(query2)
                conn.commit()

                query3 = f"SELECT * FROM usuarios WHERE idTG = '{id}'"
                query3A = cursor.execute(query3)
                query3B = cursor.fetchone()
                if query3B[5] == f'{nombre}':
                    resultado = "sucess"
                    return resultado
                else:
                    resultado = "error"
                    return resultado




    
    
    
    




    
