x = int(input("x: "))
y = int(input("y: "))
coord = (x, y)
inf = 0
sup = 10
if coord[0] >= inf and coord[0] <= sup and coord[1] >= inf and coord[1] <= sup:
    print("Dentro del rango")
else:
    print("Fuera del rango")
