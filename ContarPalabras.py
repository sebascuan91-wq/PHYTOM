frase = input("Digite frase: ")
palabras = frase.split()

dic = {}

for p in palabras:
    if p in dic:
        dic[p] = dic[p] + 1
    else:
        dic[p] = 1

print(dic)
