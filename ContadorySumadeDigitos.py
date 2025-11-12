print("Contador de cifras y suma de dígitos")
num= int(input("Ingrese un número entero positivo: "))
if num > 0:
    num = str(num)
    cantidadcifras = len(num)
    sumadigitos = 0
    for digito in num:
        sumadigitos = sumadigitos + int(digito)
    print(f"El número {num} tiene {cantidadcifras} cifras")
    print(f"La suma de sus dígitos es: {sumadigitos}")
else:
    print("El número no es positivo")