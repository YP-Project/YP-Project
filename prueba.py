import mysql.connector
from mysql.connector import Error
import csv
def pedirdatosReg2():
    print("a) Registro manual")
    print("b) Lectura archivo csv")
    leer = input("Seleccione una letra: ")
    if leer == "a":
        #Validacion del codigo
        CodigoCorrecto = False
        while(not CodigoCorrecto):
            codigo = input ("Ingrese código: ")
            if len (codigo) == 5:
                CodigoCorrecto = True
            else:
                print ("Código incorrecto: Debe tener 5 dígitos") 

        nombre = input ("Ingrese nombre: ")

        #Validacion del numero de parcela
        NoparcelaCorrecto = False
        while (not NoparcelaCorrecto):
            Noparcela = input ("Ingrese No. parcela: ")
            if Noparcela.isnumeric():
                if (int(Noparcela) > 0) and (int(Noparcela) <350):
                    NoparcelaCorrecto = True
                    Noparcela = int(Noparcela)
                else:
                    print ("Debe ingresar un No. de parcela entre 1 y 350")
            else:
                print ("No. de parcela incorrecto: Debe ser un número")

        #Validacion de la nota
        notaCorrecta = False
        while (not notaCorrecta):
            nota = input ("Ingrese nota: ")
            if nota.isnumeric():
                if (int(nota) >= 0) and (int(nota) <= 100):
                    notaCorrecta = True
                    nota = int(nota)
                else:
                    print("La nota ingresada debe ser un valor entre 0 y 100")
            else:
                print ("Nota incorrecta: Por favor ingresar un número")
        curso = (codigo, nombre, Noparcela, nota)
        return curso
    elif leer == "b":  
        nombre_archivo =  input("Ingrese el nombre del archivo csv: ")
        with open (nombre_archivo, "r") as archivo:
            lector = csv.reader (archivo, delimiter = ",")
            next (lector, None)
            for fila in lector:
                nombrecsv =fila [0]
                codigocsv = int(fila[1])
                Noparcelacsv = int(fila[2])
                notacsv = int(fila[3])
                contador = 0
                curso = (codigocsv, nombrecsv, Noparcelacsv, notacsv)
                listacurso = [codigocsv, nombrecsv, Noparcelacsv, notacsv]
                print(listacurso[contador +1])
                
        
    else:
        print("Por favor ingrese una letra valida")

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


def registrarCurso(self, curso):
    if self.conexion.is_connected():
        try: 
            cursor = self.conexion.cursor()
            sql = "INSERT INTO estudiantes (codigo, nombre , numero, nota) VALUES('{0}', '{1}', {2}, {3})"
            cursor.execute(sql.format(curso [0], curso [1], curso[2], curso [3]))
            self.conexion.commit()
            print("¡Estudiante registrado exitosamente! \n")
        except Error as ex:
            print ("Error de conexión: {0}".format(ex))
def pedirdatosReg():

    #Validacion del codigo
    CodigoCorrecto = False
    while(not CodigoCorrecto):
        codigo = input ("Ingrese código: ")
        if len (codigo) == 5:
            CodigoCorrecto = True
        else:
            print ("Código incorrecto: Debe tener 5 dígitos") 

    nombre = input ("Ingrese nombre: ")

    #Validacion del numero de parcela
    NoparcelaCorrecto = False
    while (not NoparcelaCorrecto):
        Noparcela = input ("Ingrese No. parcela: ")
        if Noparcela.isnumeric():
            if (int(Noparcela) > 0) and (int(Noparcela) <350):
                NoparcelaCorrecto = True
                Noparcela = int(Noparcela)
            else:
                print ("Debe ingresar un No. de parcela entre 1 y 350")
        else:
            print ("No. de parcela incorrecto: Debe ser un número")

    #Validacion de la nota
    notaCorrecta = False
    while (not notaCorrecta):
        nota = input ("Ingrese nota: ")
        if nota.isnumeric():
            if (int(nota) >= 0) and (int(nota) <= 100):
                notaCorrecta = True
                nota = int(nota)
            else:
                print("La nota ingresada debe ser un valor entre 0 y 100")
        else:
            print ("Nota incorrecta: Por favor ingresar un número")
    curso = (codigo, nombre, Noparcela, nota)
    return curso


pedirdatosReg2()