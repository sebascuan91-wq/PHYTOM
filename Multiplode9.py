n = int(input("Digite N: "))
m = int(input("Digite M: "))
encontro = False
for i in range(n, m+1):
    if i % 9 == 0:
        print("Primer múltiplo de 9:", i)
        encontro = True
        break

if encontro == False:
    print("No hay múltiplos de 9")
