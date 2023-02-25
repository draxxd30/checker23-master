import MySQLdb
from plugins.clases.usuarios import usuario
from configs import config

class Owner(usuario):

    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
    
    def BuscarO(self):
        try:
            with MySQLdb.connect(host = config.DB_HOST, user = config.DB_USER, password = config.DB_PASS, database = config.DB_NAME) as connect:
                cursor = connect.cursor()

                query = f"SELECT rango FROM usuarios WHERE idTG = '{self.id}'"
                cursor.execute(query)
                res = cursor.fetchone()
                res = res[0]

                if res == None:
                    return 'Error: No encontrado'
                elif res != 'Owner':
                    return 'No es owner'
                else:
                    return 'Es Owner'

        except Exception as a:
            return f'Error: {a}'

    def agregarO(self):
        try:
            br = usuario.buscarR(self.id)
            if br == 'Owner':
                return 'Error: Ya lo tiene'
            with MySQLdb.connect(host = config.DB_HOST, user = config.DB_USER, password = config.DB_PASS, database = config.DB_NAME) as connect:
                cursor = connect.cursor()

                query = f"UPDATE usuarios SET rango = 'Owner' WHERE idTG = '{self.id}'"
                res = cursor.execute(query)
                connect.commit()

                if res == 1:
                    return True
                else:
                    return False
        
        except Exception as a:
            return f'Error: {a}'

    def quitarO(self):
        try:
            br = usuario.buscarR(self.id)
            if br != 'Owner':
                return 'Error: No tiene Owner'
            with MySQLdb.connect(host = config.DB_HOST, user = config.DB_USER, password = config.DB_PASS, database = config.DB_NAME) as connect:
                cursor = connect.cursor()

                query = f"UPDATE usuarios SET rango = 'Free' WHERE idTG = '{self.id}'"
                res = cursor.execute(query)
                connect.commit()

                if res == 1:
                    return True
                else:
                    return False
       
        except Exception as a:
            return f'Error: {a}'
