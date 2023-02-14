lista1 = []
lista2 = []
for i in range(5):
    x = int(input("Digite os pontos de conexão do primeiro conector (0 - tomada, 1 - plugue): "))
    lista1.append(x)

for i in range(5):
    y = int(input("Digite os pontos de conexão do segundo conector (0 - tomada, 1 - plugue): "))
    lista2.append(y)

lista3 = []

for i in range(5):
    lista3.append(lista1[i]+lista2[i])
    
if lista3.count(1) == 5:
    print('Y')
else:
    print('N')
