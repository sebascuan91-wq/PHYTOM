print("Reloj digital")
print("Simulando un día completo")
for hora in range(0, 24):
    for minuto in range(0, 60):
        for segundo in range(0, 60):
            hora_str = str(hora).zfill(2)
            minuto_str = str(minuto).zfill(2)
            segundo_str = str(segundo).zfill(2)
            
            print(f"{hora_str}:{minuto_str}:{segundo_str}", end="\r")
print("¡Un día completo ha pasado")