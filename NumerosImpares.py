print("Serie de números impares")
cantidadterminos = int(input("Ingrese la cantidad de términos a generar: "))
contadornumeros = 0
termino = 1
while contadornumeros < cantidadterminos - 1:
    print(termino, end=", ")
    termino = termino + 2
    contadornumeros = contadornumeros + 1
print(termino)