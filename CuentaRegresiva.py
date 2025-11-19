n = int(input("Digite un numero: "))
for i in range(n, -1, -1):
    print(i)
    if i % 7 == 0 and i != 0:
        print("Alerta! múltiplo de 7")
