def maximo_de_tres(a, b, c):
    mayor = a
    if b > mayor:
        mayor = b
    if c > mayor:
        mayor = c
    return mayor
x = int(input("A: "))
y = int(input("B: "))
z = int(input("C: "))
print("Mayor =", maximo_de_tres(x, y, z))
