print("Genero del aspirante (M/F): ")
genero = input()
print("Estado civil del aspirante (S/C/V/D/U): ")
estado_civil = input()
print("Estatura del aspirante: ")
estatura = float(input())
print("Edad del aspirante: ")
edad = int(input())
if estado_civil == 'S' or estado_civil == 's':
    if genero == 'F' or genero == 'f':
        if estatura > 1.60 and edad >= 20 and edad <= 25:
            salida = "Es Apto"
        else:
            salida = "No es Apto"
    elif genero == 'M' or genero == 'm':
        if estatura > 1.65 and edad >= 18 and edad <= 24:
            salida = "Es Apto"
        else:
            salida = "No es Apto"
    else:
        salida = "No es Apto"
else:
    salida = "No es Apto"

print(salida)