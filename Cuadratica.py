import math
print("Ingrese coeficiente a: ")
a = float(input())
print("Ingrese coeficiente b: ")
b = float(input())
print("Ingrese coeficiente c: ")
c = float(input())
# Calcular discriminante
discriminante = b**2 - 4*a*c
if a == 0:
    print("NO es ecuación cuadrática (a no puede ser cero)")
elif discriminante >= 0:
    print("La ecuación cuadrática TIENE solución real")
    # Opcional: calcular las soluciones
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    print("Soluciones: x1 =", x1, ", x2 =", x2)
else:
    print("La ecuación cuadrática NO tiene solución real")