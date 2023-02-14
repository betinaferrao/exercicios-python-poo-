num = int(input("Deseja ver quantos números? "))
n = int(input("Valor: "))
lista = []
lista.append(n)
for i in range(num):
    n = n * 2
    lista.append(n)
    
for i in range(num):
    print("N[{}] = {}".format(i, lista[i]))