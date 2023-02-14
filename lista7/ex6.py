lista = []
for i in range(10):
    n = int(input("Digite um número: "))
    lista.append(n)

for i in lista:
    if i <= 0:
        pos = lista.index(i)
        lista[pos] = 1

for i in range(10):
    print("N[{}] = {}".format(i, lista[i]))
        