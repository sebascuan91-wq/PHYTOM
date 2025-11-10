print("Ingrese su nombre: ")
nom = input()
print("Ingrese su edad: ")
edad = int(input())
if edad >= 18:
    mensajeedad = "Mayor de edad"
else:
    mensajeedad = "Menor de edad"
print("Hola", nom)
print("Usted es", mensajeedad)