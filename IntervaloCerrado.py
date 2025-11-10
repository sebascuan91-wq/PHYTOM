print("Ingrese el valor mínimo del intervalo: ")
minimo = int(input())
print("Ingrese el valor máximo del intervalo: ")
maximo = int(input())
print("Ingrese el número a verificar: ")
x = int(input())
if x >= minimo and x <= maximo:
    print(x, "está DENTRO del intervalo [", minimo, ",", maximo, "]")
else:
    print(x, "está FUERA del intervalo [", minimo, ",", maximo, "]")