print("Verificador de números de Armstrong")
num= int(input("Ingrese un número para verificar si es Armstrong: "))
numerstr = str(num)
n = len(numerstr) 
sumapotencias = 0
print(f"Procesando {num} (tiene {n} dígitos):")
for digito in numerstr:
    digitoint = int(digito)
    potencia = digitoint ** n
    sumapotencias = sumapotencias + potencia
    print(f"  {digito}^{n} = {potencia}")
print(f"Suma total: {sumapotencias}")
if sumapotencias == num:
    print(f"¡{num} SÍ es un número de Armstrong ")
else:
    print(f"{num} NO es un número de Armstrong")