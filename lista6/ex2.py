n = int(input("Deseja ler quantos números? "))
numeros = list()
for i in range(n):
    num = int(input("Número: "))
    numeros.append(num)


repetidos = []
repeticoes = []
for i in numeros:
    qtd = numeros.count(i)
    if qtd > 1 and i not in repetidos :
        repetidos.append(i)
        repeticoes.append(qtd)
        
if len(repetidos) == 0:
    print("Não há repetições")
else:
    print("Há valores repetidos!")


for i in range(0,len(repetidos)):
    print("{} se repete {} vezes.".format(repetidos[i], repeticoes[i]))

