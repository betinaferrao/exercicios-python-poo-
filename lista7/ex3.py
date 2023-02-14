n = int(input("Deseja inserir quantos números? "))
lista = []
for i in range(n):
    num = int(input("Número: "))
    lista.append(num)
    
repetidos = []
repeticoes = []
for i in lista:
    qnt = lista.count(i)
    if qnt > 1 and i not in repetidos:
        repetidos.append(i)
        repeticoes.append(qnt)

if len(repetidos) == 0:
    print("Não há repetições")
else:
    print("Há valores repetidos!")

for i in range(0, len(repetidos)):
    print("{} se repete {} vezes.".format(repetidos[i], repeticoes[i]))