print("Ingrese un número entre 0 y 20: ")
numero = int(input())
primos = [2, 3, 5, 7, 11, 13, 17, 19]
if numero in primos:
    print(numero, "es un número primo")
else:
    print(numero, "NO es un número primo")