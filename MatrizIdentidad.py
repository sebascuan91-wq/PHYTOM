n = int(input("Digite n: "))
mat = []
for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    mat.append(fila)
for fila in mat:
    print(fila)
