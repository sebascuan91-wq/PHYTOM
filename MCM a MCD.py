def mcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def mcm(a, b):
    return abs(a * b) // mcd(a, b)

x = int(input("A: "))
y = int(input("B: "))

print("MCM =", mcm(x, y))
