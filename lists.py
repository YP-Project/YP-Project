import csv


def leerArchivo():
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
            # print(curso)
            # si hacen return en el ciclo, solo entrará una vez y
            # luego retorna
    # retornar despues de finalizar el ciclo
    # retornar una lista con todos los  resultados
    return _registros


registros = leerArchivo()
# print(registros)

# al receibir todos los valores leidos
# hacer un ciclo con la lista
# el tipo (tuple) de cada registro es el mismo del curso (variable individual anterior)
for registro in registros:
    print(registro)
