def listarCursos(cursos):
    print("Cursos: ")
    contador = 1
    for cur in cursos:
        datos="{0}. Código: {1} | Nombre: {2} | No. parcela: {3}   | Nota: {4}"
        print(datos.format(contador,cur[0], cur[1], cur[2], cur[3]))
        contador = contador + 1
    print(" ")

def pedirDatosRegistro():
    codigoCorrecto = False
    while (not codigoCorrecto):
        codigo = input("Ingrese código: ")
        if len(codigo)== 5:
            codigoCorrecto = True
        else: 
            print("Código no válido. Debe tener 5 dígitos")

    nombre = input ("Ingrese nombre: ")
    creditosCorrecto = False
    while(not creditosCorrecto):
        creditos = input("Ingrese créditos: ")
        if creditos.isnumeric():
            if  (int (creditos))> 0:
                creditosCorrecto = True
                creditos = int(creditos)
            else: 
                print ("Los créditos deben ser mayor a 0")
        else: 
            print ("Créditos no válidos. Debe ser un numero unicamente")

    cursos = (codigo, nombre, creditos)
    return cursos

def pedirDatosActualizacion(cursos):
    listarCursos(cursos)
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
    listarCursos(cursos)
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