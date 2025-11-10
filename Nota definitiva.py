print("Ingrese la nota definitiva: ")
nota = float(input())
print("Su nota es", end=" ")
if nota < 3.0:
    print("Insuficiente")
elif nota <= 3.5:
    print("Aceptable")
elif nota <= 4.0:
    print("Sobresaliente")
else:
    print("Excelente")