n = int(input("Digite un numero: "))
invertido = 0
while n > 0:
    dig = n % 10
    invertido = invertido * 10 + dig
    n = n // 10
print("Invertido es:", invertido)
