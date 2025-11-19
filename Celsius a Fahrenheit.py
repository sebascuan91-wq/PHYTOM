def celsiusfahrenheit(c):
    f = (c * 9/5) + 32
    return f
c = float(input("Grados Celsius: "))
print("Fahrenheit =", celsiusfahrenheit(c))
