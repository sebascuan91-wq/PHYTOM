notas = {}

notas["Ana"] = 4.0
notas["Luis"] = 3.5
notas["Sofia"] = 4.5

suma = 0
for n in notas.values():
    suma = suma + n

prom = suma / len(notas)
print("Promedio general:", prom)
