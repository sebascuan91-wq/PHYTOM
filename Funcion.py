print("Cálculo de función ")
valor_x = -1
while valor_x < 0:
    valor_x = int(input("Ingrese el máximo valor para x: "))
    if valor_x < 0:
        print("El valor no puede ser negativo. Intente nuevamente.")
print("\nx\tf(x)")
print("-" * 15)
for x in range(0, valor_x + 1, 2):
    funcion = x**3 + x**2 - 5
    print(f"{x}\t{funcion}")