n = int(input("Digite a quatidade de suspeitos: "))
lista = []
for i in range(n):
    num = int(input("Classificação de quão suspeita a {}° pessoa é? ".format(i+1)))
    lista.append(num)


lista1 = lista[:]
lista.sort()
ass = lista[1]
indice = lista1.index(ass)


print("O índice do assassino é: {} ".format(indice))
    