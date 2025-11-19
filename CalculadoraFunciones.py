def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b
def calculadora():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    op = int(input("Elija opcion: "))
    x = int(input("Número 1: "))
    y = int(input("Número 2: "))

    if op == 1:
        print("Resultado:", sumar(x, y))
    elif op == 2:
        print("Resultado:", restar(x, y))
    elif op == 3:
        print("Resultado:", multiplicar(x, y))
    elif op == 4:
        print("Resultado:", dividir(x, y))
calculadora()
