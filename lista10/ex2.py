p, n = input("Altura do pulo do sapo e número de canos: ").split()
p = int(p)
n = int(n)

lista = []
for i in range(n):
    h = int(input("Altura do {}° cano: ".format(i+1)))
    lista.append(h)

cont = 0
for i in range(n-1):
    if (lista[i+1] - lista[i]) < p:
        cont += 1    

if (cont) == (n-1):
    print("YOU WIN")
else:
    print("GAME OVER")
    