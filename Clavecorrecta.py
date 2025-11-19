clavecorrecta = "1234"
intentos = 0
while intentos < 3:
    clave = input("Digite clave: ")
    if clave == clavecorrecta:
        print("Acceso permitido")
        break
    intentos = intentos + 1
if intentos == 3:
    print("Acceso denegado")
