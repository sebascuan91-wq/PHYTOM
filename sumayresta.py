op = 0
while op != 3:
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")
    op = int(input("Elija opcion: "))
    if op == 1:
        a = int(input("Numero 1: "))
        b = int(input("Numero 2: "))
        print("Resultado:", a + b)
    elif op == 2:
        a = int(input("Numero 1: "))
        b = int(input("Numero 2: "))
        print("Resultado:", a - b)
print("Fin del programa")
