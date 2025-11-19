pares = 0
impares = 0
while True:
    n = int(input("Numero (0 para terminar): "))
    if n == 0:
        break
    if n % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
print("Pares:", pares)
print("Impares:", impares)
