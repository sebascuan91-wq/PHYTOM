print("Serie de impares")
cantidadterminos = int(input("Ingrese la cantidad de términos a generar:"))
contadornumeros = 0
termino = 1
if cantidadterminos > 0:
    while True:
        print(termino, end="")
        contadornumeros = contadornumeros + 1
        
        if contadornumeros < cantidadterminos - 1:
            print(", ", end="")
            termino = termino + 2
        else:
            break
    if cantidadterminos > 1:
        print(",", termino + 2)
    else:
        print()