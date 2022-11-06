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
    def listarCursos(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM estudiantes ORDER BY nombre ASC")
                resultados=cursor.fetchall()
                return resultados
            except Error as ex:
                print ("Error de conexión: {0}".format(ex))

    def actualizarCurso(self, curso):
        if self.conexion.is_connected():
            try:
                #Creo que aqui hay que modificar para que se adapte a los valores de parcela 
                cursor = self.conexion.cursor()
                sql = "UPDATE estudiantes SET nombre = '{0}', numero = {1}, nota = {2} WHERE codigo = '{3}'"
                cursor.execute(sql.format(curso [1], curso [2], curso[3], curso[0]))
                self.conexion.commit()
                print("¡Información del estudiante modificada exitosamente! \n")
            except Error as ex:
                print ("Error de conexión: {0}".format(ex))


    def eliminarCurso(self,codigoCursoEliminar):
        if self.conexion.is_connected():
            try:
                #Creo que aqui hay que modificar para que se adapte a los valores de parcela 
                cursor = self.conexion.cursor()
                sql = "DELETE FROM estudiantes WHERE codigo = '{0}'"
                cursor.execute(sql.format(codigoCursoEliminar))
                self.conexion.commit()
                print("¡Estudiante eliminado exitosamente! \n")
            except Error as ex:
                print ("Error de conexión: {0}".format(ex))
    
    def registrarCurso2(self, curso):
        if self.conexion.is_connected():
            try: 
                TodosDatos = False
                while (not TodosDatos):
                    cursor = self.conexion.cursor()
                    sql = "INSERT INTO estudiantes (codigo, nombre , numero, nota) VALUES('{0}', '{1}', {2}, {3})"
                    cursor.execute(sql.format(curso [0], curso [1], curso[2], curso [3]))
                    self.conexion.commit()
                    if curso == "":
                        TodosDatos = True
                        print("¡Estudiante registrado exitosamente! \n")
            except Error as ex:
                print ("Error de conexión: {0}".format(ex))