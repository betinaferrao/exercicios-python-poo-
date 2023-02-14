lista = []
resultado = []
n = int(input("Número de células no tabuleiro: "))
for i in range(n):
    sn = int(input("Existe mina na {}° célula? (0- não, 1- sim) ".format(i+1)))
    lista.append(sn)
    
cont = 0
for i in range(1, len(lista)-1):
    if lista[i-1] == 1:
        cont += 1
    if lista[i] == 1:
        cont += 1
    if lista[i+1] == 1:
        cont += 1
    resultado.append(cont)
    cont = 0

for i in range(0, 1):
    if lista[i] == 1:
        cont += 1
    if lista[i+1] == 1:
        cont += 1
    resultado.insert(0, cont)
    cont = 0

for i in range(0, 1):
    if lista[len(lista)-2] == 1:
        cont += 1
    if lista[len(lista)-1] == 1:
        cont += 1
    resultado.append(cont)
    cont = 0

print(resultado)