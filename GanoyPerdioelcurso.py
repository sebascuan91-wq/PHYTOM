print("Ingrese las 5 notas de los trabajos:")
sumanotas = 0
for i in range(5):
    print(f"Nota trabajo {i+1}: ")
    nota = float(input())
    sumanotas += nota
notadefinitiva = sumanotas / 5
print("Nota definitiva:", notadefinitiva)
if notadefinitiva > 3.5:
    print("GANÓ el curso")
else:
    print("PERDIÓ el curso")