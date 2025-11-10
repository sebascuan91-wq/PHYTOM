
print("=== PRIMER INTERVALO ===")
print("Ingrese límite inferior del primer intervalo: ")
inf1 = int(input())
print("Ingrese límite superior del primer intervalo: ")
sup1 = int(input())
print("=== SEGUNDO INTERVALO ===")
print("Ingrese límite inferior del segundo intervalo: ")
inf2 = int(input())
print("Ingrese límite superior del segundo intervalo: ")
sup2 = int(input())
print("=== TERCER INTERVALO ===")
print("Ingrese límite inferior del tercer intervalo: ")
inf3 = int(input())
print("Ingrese límite superior del tercer intervalo: ")
sup3 = int(input())
print("Ingrese el número a verificar: ")
x = int(input())
en_intervalo = False
if x > inf1 and x < sup1:
    en_intervalo = True
    print("Está en el primer intervalo")
elif x > inf2 and x < sup2:
    en_intervalo = True
    print("Está en el segundo intervalo")
elif x > inf3 and x < sup3:
    en_intervalo = True
    print("Está en el tercer intervalo")
if en_intervalo:
    print(x, "está DENTRO de alguno de los intervalos")
else:
    print(x, "está FUERA de todos los intervalos")