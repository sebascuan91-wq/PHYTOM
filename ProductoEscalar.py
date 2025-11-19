a = input("Lista A: ").split()
b = input("Lista B: ").split()
a = [int(x) for x in a]
b = [int(x) for x in b]
suma = 0
for i in range(len(a)):
    suma = suma + a[i] * b[i]

print("Producto escalar =", suma)
