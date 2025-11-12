print("PRÁCTICA DE TABLAS DE MULTIPLICAR ")
while True:
    tabla = int(input("\n¿Qué tabla quieres practicar? (1-20): "))
    if tabla < 1 or tabla > 20:
        print("Por favor, elige una tabla entre 1 y 20")
        continue
    aciertos = 0
    print(f"\n--- Practicando la tabla del {tabla} ---")
    for numero in range(1, 11):
        resultado_correcto = tabla * numero
        respuesta = int(input(f"{tabla} × {numero} = "))
        if respuesta == resultado_correcto:
            print("¡Correcto! ¡Muy bien! ")
            aciertos = aciertos + 1
        else:
            print(f"Incorrecto. La respuesta es: {resultado_correcto} ")
    print(f"\n--- RESULTADO FINAL ---")
    print(f"Tuviste {aciertos} de 10 correctos")
    if 0 <= aciertos <= 5:
        print("Calificación: Insuficiente")
    elif aciertos == 6 or aciertos == 7:
        print("Calificación: Aceptable")
    elif aciertos == 8 or aciertos == 9:
        print("Calificación: Sobresaliente")
    else:
        print("Calificación: Excelente 🎉")
    continuar = input("\n¿Quieres practicar otra tabla? (s/n): ").lower()
    if continuar != 's':
        print("¡Gracias por practicar! 👋")
        break