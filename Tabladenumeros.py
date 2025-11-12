print("Tabla de números")
cantidadnumeros = int(input("Ingrese la cantidad de números: "))
print("Número | Cuadrado | Triple")
print("-" * 25)
for numero in range(1, cantidadnumeros + 1):
    cuadrado = numero * numero
    triple = numero * 3
    print(f"{numero:6} | {cuadrado:8} | {triple:6}")