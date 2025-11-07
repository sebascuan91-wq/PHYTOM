cantidad = float(input("Ingrese la cantidad de dinero: "))
periodo = int(input("Ingrese el periodo en días: "))
porcentajeinteres = float(input("Ingrese el porcentaje de interés: "))
valorintereses = (cantidad * porcentajeinteres / 100 * periodo) / 360
valorimpuesto = valorintereses * 0.07
netopagar = cantidad + valorintereses - valorimpuesto
print("Intereses ganados:", valorintereses)
print("Valor del impuesto:", valorimpuesto)
print("Total a pagar al cliente:", netopagar)
