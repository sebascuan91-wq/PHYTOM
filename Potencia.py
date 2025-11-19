def potencia(base, exp):
    res = 1
    for i in range(exp):
        res = res * base
    return res
b = int(input("Base: "))
e = int(input("Exponente: "))
print("Resultado =", potencia(b, e))
