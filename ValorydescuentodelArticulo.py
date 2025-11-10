print("Ingrese el valor del artículo: ")
valor = float(input())
print("Tipo de artículo:")
print("1 Textil")
print("2 Electrodoméstico") 
print("3 Elementos de cocina")
print("4 Video juego")
print("Ingrese el tipo (1-4): ")
tipo = input()
if tipo == '1':
    porcentaje = 0.0  # 0%
    tipo_nombre = "Textil"
elif tipo == '2':
    porcentaje = 0.037  # 3.7%
    tipo_nombre = "Electrodoméstico"
elif tipo == '3':
    porcentaje = 0.042  # 4.2%
    tipo_nombre = "Elementos de cocina"
elif tipo == '4':
    porcentaje = 0.078  # 7.8%
    tipo_nombre = "Video juego"
descuento = valor * porcentaje
total_pagar = valor - descuento
print("Tipo de artículo:", tipo_nombre)
print("Valor original:", valor)
print("Descuento aplicado:", descuento)
print("Total a pagar:", total_pagar)