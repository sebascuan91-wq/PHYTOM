print("Cálculo de factorial")
numero = int(input("Ingrese un número para calcular su factorial: "))
if numero < 0:
    print("Los números negativos no tienen factorial")
elif numero == 0:
    print("0! = 1")
else:
    factorial = 1
    print(f"Calculando {numero}! = ", end="")
    for i in range(1, numero + 1):
        factorial = factorial * i
        if i < numero:
            print(f"{i} × ", end="")
        else:
            print(f"{i} = {factorial}")
    print(f"El factorial de {numero} es: {factorial}")