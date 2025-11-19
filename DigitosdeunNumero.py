def contar_digitos(n):
    cont = 0
    if n == 0:
        return 1
    while n != 0:
        cont = cont + 1
        n = n // 10
    return cont
num = int(input("Número: "))
print("Dígitos:", contar_digitos(num))
