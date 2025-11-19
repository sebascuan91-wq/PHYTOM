A = [[1,2,3],[4,5,6]]
filas = len(A)
cols = len(A[0])
T = []
for j in range(cols):
    fila = []
    for i in range(filas):
        fila.append(A[i][j])
    T.append(fila)

print(T)
