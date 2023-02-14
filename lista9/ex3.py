
n = int(input("Número de pessoas que participaram da pesquisa: "))
cont = 1
lista = list()
while (cont <= n):
    q = int(input("Pessoa {} - Considera o cenário atual satisfatório? (0 - sim, 1 - não) ".format(cont)).upper().strip())
    lista.append(q)
    cont += 1

um = zero = 0
for i in range(len(lista)):
    if lista[i] == 1:
        um += 1
    elif lista[i] == 0:
        zero += 1

if um > zero or um == zero:
    print("N")
if um < zero:
    print("S")
