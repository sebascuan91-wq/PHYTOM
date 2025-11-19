def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f
numero = int(input("Digite un número: "))
print("Factorial =", factorial(numero))
