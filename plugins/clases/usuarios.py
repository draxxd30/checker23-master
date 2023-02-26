import pyrogram
import MySQLdb
from configs import config

class usuario:

    DB_HOST = config.DB_HOST
    DB_USER = config.DB_USER
    DB_PASS = config.DB_PASS
    DB_NAME = config.DB_NAME

    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id

    def buscar(self):
        try:
            with MySQLdb.connect(host = self.DB_HOST, user = self.DB_USER, password = self.DB_PASS, database = self.DB_NAME) as connect:
                cursor = connect.cursor()

                query = f"SELECT * FROM usuarios WHERE idTG = '{self.id}'"
                cursor.execute(query)
                res = cursor.fetchone()

                if res == None:
                    return False
                else:
                    return res #Tambien se puede poner un string de bien para que solo  devuelva si existe o no el usuario
        
        except Exception as a:
            return None
    
    def agregar(self):
        try:
            with MySQLdb.connect(host = self.DB_HOST, user = self.DB_USER, password = self.DB_PASS, database = self.DB_NAME) as connect:
                cursor = connect.cursor()

                query = f"INSERT INTO usuarios (usuario, rango, creditos, idTG, rangoM) VALUES ('{self.nombre}', 'Free', '50', {self.id}, 'Free')"
                result = cursor.execute(query)
                connect.commit()

                if result == 1:
                    return True
                else:
                    return False
        
        except Exception as a:
            return None

    def eliminar(self):
        try:
            with MySQLdb.connect(host = self.DB_HOST, user = self.DB_USER, password = self.DB_PASS, database = self.DB_NAME) as connect:
                cursor = connect.cursor()

                query = f"DELETE FROM usuarios WHERE idTG = '{self.id}'"
                result = cursor.execute(query)
                connect.commit()

                if result == 1:
                    return True
                else:
                    return False
        
        except Exception as a:
            return None

    
    def buscarR(self):
        try:
            with MySQLdb.connect(host = self.DB_HOST, user = self.DB_USER, password = self.DB_PASS, database = self.DB_NAME) as connect:
                cursor = connect.cursor()

                query = f"SELECT rango FROM usuarios WHERE idTG = '{self.id}'"
                cursor.execute(query)
                res = cursor.fetchone()

                if res == None:
                    return None
                else:
                    return res[0]
                
        except Exception as a:
            return False
    
    def buscarUser(self):
        try:
            with MySQLdb.connect(host = self.DB_HOST, user = self.DB_USER, password = self.DB_PASS, database = self.DB_NAME) as connect:
                cursor = connect.cursor()
                
                query = f"SELECT * FROM usuarios WHERE usuario = '{self.nombre}'"
                cursor.execute(query)
                res = cursor.fetchone()
                
                if res == None:
                    return False
                else:
                    return res
        
        except Exception:
            return None
            

