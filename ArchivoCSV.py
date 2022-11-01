import csv
nombre_archivo =  "DatosParcela.csv"
with open (nombre_archivo, "r") as archivo:
    lector = csv.reader (archivo, delimiter = ";")
    next (lector, None)
    for fila in lector:
        nombre = fila [0]
        codigo = int(fila[1])
        NumeroParcela = float(fila[2])
        nota = int(fila[3])
        print(
            f"Nombre y apellido:  {nombre} | Código {codigo} | No. parcela {NumeroParcela} | Nota {nota}")