num = int(input("Quantidade de números da lista de Bino: "))
lista = []
for i in range(num):
    n = int(input("Números da lista de Bino: "))
    lista.append(n)

cont2 = cont3 = cont4 = cont5 = 0
for i in range(num):
    if lista[i] % 2 == 0:
        cont2 += 1
    if lista[i] % 3 == 0:
        cont3 += 1
    if lista[i] % 4 == 0:
        cont4 += 1
    if lista[i] % 5 == 0:
        cont5 += 1

print("{} Multiplo(s) de 2".format(cont2))
print("{} Multiplo(s) de 3".format(cont3))
print("{} Multiplo(s) de 4".format(cont4))
print("{} Multiplo(s) de 5".format(cont5))