num = int(input("Digite un numero: "))
primo = True
for i in range(2, num):
    if num % i == 0:
        primo = False
if primo == True:
    print("Es primo")
else:
    print("No es primo")
