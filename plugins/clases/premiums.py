from plugins.clases.usuarios import usuario
import MySQLdb
from configs import config

class premium(usuario):

    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id

    def buscarP(self):
        try:
            with MySQLdb.connect(host = config.DB_HOST, user = config.DB_USER, password = config.DB_PASS, database = config.DB_NAME) as connect:
                cursor = connect.cursor()

                query = f"SELECT rango FROM usuarios WHERE idTG = '{self.id}'"
                cursor.execute(query)
                re = cursor.fetchone()
                re = re[0]

                if re == None:
                    return 'Error: No encontrado'
                elif re != 'Premium':
                    return 'No es premium'
                else:
                    return 'Es premium'
        
        except Exception as a:
            return f'Error: {a}'
    
    def agregarP(self):
        try:
            br = usuario.buscarR(self.id)
            if br == 'Premium':
                return 'Ya tenia este rango'
            elif br == None:
                return 'Usuario inexistente'
            elif br == False:
                return 'Error de conexion'
            with MySQLdb.connect(host = config.DB_HOST, user = config.DB_USER, password = config.DB_PASS, database = config.DB_NAME) as connect:
                cursor = connect.cursor()

                query = f"UPDATE usuarios SET rango = 'Premium' WHERE idTG = '{self.id}'"
                res = cursor.execute(query)
                connect.commit()

                if res == 1:
                    return True
                else:
                    return False

        except Exception as a:
            return f'Error: {a}'

    def eliminarP(self):
        try:
            br = usuario.buscarR(self.id)
            if br != 'Premium':
                return 'No tiene este rango'
            elif br == None:
                return 'Usuario inexistente'
            elif br == False:
                return 'Error de conexion'
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
