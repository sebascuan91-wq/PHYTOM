def invertir(cad):
    if cad == "":
        return ""
    return invertir(cad[1:]) + cad[0]
texto = input("Texto: ")
print("Invertido:", invertir(texto))
