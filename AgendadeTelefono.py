agenda = {}
while True:
    nom = input("Nombre (fin para terminar): ")

    if nom == "fin":
        break

    tel = input("Telefono: ")
    agenda[nom] = tel
print(agenda)
