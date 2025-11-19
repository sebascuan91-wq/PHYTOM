suma = 0
while True:
    n = int(input("Digite numero (0 para salir): "))

    if n == 0:
        break

    if n < 0:
        continue

    suma = suma + n
print("La suma es:", suma)
