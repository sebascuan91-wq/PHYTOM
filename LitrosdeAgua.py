print("Ingrese la cantidad actual de litros en el tanque: ")
litros = float(input())
if litros < 250:
    print("ABRIR la llave - Tanque necesita más agua")
elif litros > 450:
    print("CERRAR la llave - Tanque está muy lleno")
else:
    print("MANTENER estado actual - Tanque en nivel adecuado")