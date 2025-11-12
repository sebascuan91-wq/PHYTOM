print("Serie de impares")
cantidad_terminos = int(input("Ingrese la cantidad de términos a generar: "))
termino = 1
for contador_numeros in range(1, cantidad_terminos):
    print(termino, end=", ")
    termino = termino + 2
print(termino)