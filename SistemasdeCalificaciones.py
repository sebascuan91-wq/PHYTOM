print("Sistema de calificaciones")
cantidadestudiantes = int(input("Ingrese la cantidad de estudiantes: "))
contadorestudiantes = 0
aprobados = 0
reprobados = 0
sumadefinitivas = 0
while contadorestudiantes < cantidadestudiantes:
    codigoestudiante = input("Ingrese el código del estudiante: ")
    notadefinitiva = float(input("Ingrese la nota definitiva: "))
    if notadefinitiva >= 3.0:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1
    sumadefinitivas = sumadefinitivas + notadefinitiva
    contadorestudiantes = contadorestudiantes + 1
promediogrupo = sumadefinitivas / cantidadestudiantes
print(" RESULTADOS ")
print("La cantidad que aprobaron es:", aprobados)
print("La cantidad que reprobaron es:", reprobados)
print("El promedio es:", round(promediogrupo, 2))