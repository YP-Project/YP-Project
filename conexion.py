import mysql.connector
from mysql.connector import Error
import csv
class DAO():

    def __init__ (self):
        try: 
            self.conexion = mysql.connector.connect(
                host ='localhost',
                port = 3306,
                user ='root',
                password = '123456',
                db = 'parcela'
            )
        except Error as ex:
            print ("Error de conexión: {0}".format(ex))
    def listarEstudiantes(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM estudiantes ORDER BY nombre ASC")
                resultados=cursor.fetchall()
                return resultados
            except Error as ex:
                print ("Error de conexión: {0}".format(ex))

    def actualizarEstudiantes(self, curso):
        if self.conexion.is_connected():
            try:
                 
                cursor = self.conexion.cursor()
                sql = "UPDATE estudiantes SET nombre = '{0}', numero = {1}, nota = {2} WHERE codigo = '{3}'"
                cursor.execute(sql.format(curso [1], curso [2], curso[3], curso[0]))
                self.conexion.commit()
                print("¡Información del estudiante modificada exitosamente! \n")
            except Error as ex:
                print ("Error de conexión: {0}".format(ex))


    def eliminarEstuadiantes(self,codigoCursoEliminar):
        if self.conexion.is_connected():
            try:
                 
                cursor = self.conexion.cursor()
                sql = "DELETE FROM estudiantes WHERE codigo = '{0}'"
                cursor.execute(sql.format(codigoCursoEliminar))
                self.conexion.commit()
                print("¡Estudiante eliminado exitosamente! \n")
            except Error as ex:
                print ("Error de conexión: {0}".format(ex))
    
    def registrarEstudiantes(self, curso):
        if self.conexion.is_connected():
            try: 
                for est in curso:
                    cursor = self.conexion.cursor()
                    sql = "INSERT INTO estudiantes (codigo, nombre , numero, nota) VALUES('{0}', '{1}', {2}, {3})"
                    cursor.execute(sql.format(est [0], est [1], est[2], est [3]))
                    self.conexion.commit()
                print("¡Estudiantes registrados exitosamente! \n")
            except Error as ex:
                print ("Error de conexión: {0}".format(ex))