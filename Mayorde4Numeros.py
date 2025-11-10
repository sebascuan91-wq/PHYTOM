print("Ingrese el primer número: ")
n1 = float(input(n1))
print("Ingrese el segundo número: ")
n2 = float(input(n2))
print("Ingrese el tercer número: ")
n3 = float(input(n3))
print("Ingrese el cuarto número: ")
n4 = float(input(n4))
if n1 > n2:
    if n1 > n3:
        if n1 > n4:
            mayor = n1
        else:
            mayor = n4
    else:
        if n3 > n4:
            mayor = n3
        else:
            mayor = n4
else:
    if n2 > n3:
        if n2 > n4:
            mayor = n2
        else:
            mayor = n4
    else:
        if n3 > n4:
            mayor = n3
        else:
            mayor = n4

print("El número mayor es:", mayor)