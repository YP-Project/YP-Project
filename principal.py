
from tkinter import Menu
from BD.conexion import DAO
import funciones

def menuPrincipal():
    continuar=True
    while(continuar):
        opcioncorrecta = False
        while( not opcioncorrecta):
            print("__________MENÚ PRINCIPAL__________")
            print(" ")
            print("1. Listado de estudiantes")
            print("2. Registrar estudiante")
            print("3. Actualizar información de estudiante")
            print("4. Eliminar estudiante")
            print("5. Salir")
            print("___________________________________")
            opcion = int(input("Seleccióne una acción: "))
        
            if opcion < 1 or opcion > 5:
                print ("Por favor seleccione una acción válida")
            
            elif opcion==5:
                print ("¡Muchas gracias por usar nuestro programa, hasta la próxima!")
                continuar = False
                break
            else:
                opcioncorrecta = True
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    dao=DAO()
    
    if opcion==1:
        try:
            cursos=dao.listarEstudiantes()
            if len (cursos)>0:
                funciones.listarEstudiantes(cursos)
            else:
                print ("No se encontraron estudiantes")        
        except:
            print ("Ocurrió un error")
    elif opcion ==2 :
        curso = funciones.pedirdatosReg()
        try:
            dao.registrarEstudiantes(curso)
        except:
            print ("Ocurrió un error")
    elif opcion ==3 :
        try:
            cursos = dao.listarEstudiantes()
            if len (cursos)>0:
                curso = funciones.pedirDatosActualizacion(cursos)
                if curso:
                    dao.actualizarEstudiantes(curso)
                else:
                    print ("Código de estudiante a actualizar no encontrado\n")
            else:
                print ("Código de estudiante no encontrado\n")
        except:
            print ("Ocurrió un error") 
    elif opcion==4 :
        try:
            cursos = dao.listarEstudiantes()
            if len (cursos)>0:
                codigoEliminar = funciones.pedirDatosEliminacion(cursos)
                if not (codigoEliminar == ""):
                    dao.eliminarEstuadiantes(codigoEliminar)
                else:
                    print ("Código de curso no encontrado...")
            else:
                print ("Código de curso no encontrado\n")
        except:
            print ("Ocurrió un error")    
    else:
        print("Por favor seleccione una acción válida")
menuPrincipal()
