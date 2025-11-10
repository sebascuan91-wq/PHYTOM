print("Ingrese un carácter: ")
opcion = input()
print("Su opción es", end=" ")
if opcion == 'a' or opcion == 'A':
    print("Android")
elif opcion == 'i' or opcion == 'I':
    print("iOS")
else:
    print("inválida")