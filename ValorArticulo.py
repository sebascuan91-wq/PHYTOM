print("Ingrese el valor del artículo: ")
valor = float(input())
print("Ingrese el tipo de artículo: ")
tipo = input()
if tipo == '1':
    porcentaje = 0.125  # 12.5%
elif tipo == '2':
    porcentaje = 0.083  # 8.3%
elif tipo == '3':
    porcentaje = 0.032  # 3.2%
else:
    porcentaje = 0.0
descuento = valor * porcentaje
print("El valor del descuento es:", descuento)