import csv
def listarEstudiantes(cursos):
    print("Estudiantes: ")
    contador = 1
    for cur in cursos:
        datos="{0}. Código: {1} | Nombre: {2} | No. parcela: {3}   | Nota: {4}"
        print(datos.format(contador,cur[0], cur[1], cur[2], cur[3]))
        contador = contador + 1
    print(" ")

def pedirDatosActualizacion(cursos):
    listarEstudiantes(cursos)
    existeCodigo = False
    codigoEditar = input("Ingrese el código del estudiante a actualizar: ")
    for cur  in cursos:
        if cur [0] == codigoEditar:
            existeCodigo = True
            break
        
    if existeCodigo:
        nombre = input ("Ingrese nombre del estudiante a modificar: ")

        #Validacion del numero de parcela
        NoparcelaCorrecto = False
        while (not NoparcelaCorrecto):
            Noparcela = input ("Ingrese No. parcela a modificar: ")
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
            nota = input ("Ingrese nota a modificar: ")
            if nota.isnumeric():
                if (int(nota) >= 0) and (int(nota) <= 100):
                    notaCorrecta = True
                    nota = int(nota)
                else:
                    print("La nota ingresada debe ser un valor entre 0 y 100")
            else:
                print ("Nota incorrecta: Por favor ingresar un número")

        curso = (codigoEditar, nombre, Noparcela, nota)
    else:
        curso = None
    return curso
    
def pedirDatosEliminacion(cursos):
    listarEstudiantes(cursos)
    existeCodigo = False
    codigoEliminar = input("Ingrese el código del curso a eliminar: ")
    for cur  in cursos:
        if cur [0] == codigoEliminar:
            existeCodigo = True
            break
    if not existeCodigo:
        codigoEliminar = ""

    return codigoEliminar

def pedirdatosReg():
    _registros = []
    nombre_archivo = input("Ingrese el nombre del archivo csv: ")
    with open(nombre_archivo, "r") as archivo:
        lector = (csv.reader)(archivo, delimiter=",")
        next(lector, None)
        for fila in lector:
            nombrecsv = fila[0]
            codigocsv = int(fila[1])
            Noparcelacsv = float(fila[2])
            notacsv = int(fila[3])

            curso = (codigocsv, nombrecsv, Noparcelacsv, notacsv)
            _registros.append(curso)
            type(curso)
    return _registros
               
