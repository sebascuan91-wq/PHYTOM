print("Ingrese el costo del artículo: ")
costo = float(input())
if costo > 150000:
    descuento = costo * 0.05
    print("Tiene descuento del 5%:", descuento)
else:
    print("No aplica descuento")
    descuento = 0
print("Valor total a pagar:", costo - descuento)