print("Encuesta de plataformas móviles")
cantidadestudiantes = int(input("¿Cuántos estudiantes participarán en la encuesta? "))
votosandroid = 0
votosios = 0
contador = 0
while contador < cantidadestudiantes:
    codigo = input("Ingrese código del estudiante: ")
    voto = input("¿Qué plataforma prefiere? (Android/iOS): ").lower()
    if voto == "android":
        votosandroid = votosandroid + 1
        print("Voto registrado para Android")
    elif voto == "ios":
        votosios = votosios + 1
        print("Voto registrado para iOS")
    else:
        print("Opción no válida. Voto no contabilizado.")
    contador = contador + 1
print("RESULTADOS DE LA ENCUESTA ")
print(f"Android: {votosandroid} votos")
print(f"iOS: {votosios} votos")
if votosandroid > votosios:
    print("Android es la plataforma ganadora")
elif votosios > votosandroid:
    print("iOS es la plataforma ganadora")
else:
    print("Empate se usará otro mecanismo de elección.")