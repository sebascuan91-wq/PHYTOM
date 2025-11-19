nums = input("Digite números separados por espacio: ")
lista = nums.split()
lista = [int(x) for x in lista]
suma = 0
for x in lista:
    suma = suma + x
prom = suma / len(lista)
print("Promedio:", prom)
mayores = []
for x in lista:
    if x > prom:
        mayores.append(x)
print("Mayores que el promedio:", mayores)
