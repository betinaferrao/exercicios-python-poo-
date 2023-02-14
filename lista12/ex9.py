n = int(input("Quantidade de participantes no amigo secreto: "))
lista = []
dic = {}
for i in range(n):
    x = input("Digite o nome e 3 opções de presete desejados: ").split()
    dic = {'nome': x[0], 'p1': x[1], 'p2': x[2], 'p3': x[3]}
    lista.append(dic.copy())

lista2 = []
dic2 = {}

s = int(input("Deseja verificar para quantas pessoas: "))
for i in range(s):
    y = input("Digite um nome e um presente que deseja consultar: ").split()
    dic2 = {'nome': y[0], 'p': y[1]}
    lista2.append(dic2.copy())
    

print(lista)
print(lista2)
for j in lista2:
    for i in lista:
        if i['nome'] == j['nome']:
            if i['p1'] == j['p'] or i['p2'] == j['p'] or i['p3'] == j['p']:
                print("Uhul! Seu amigo secreto vai adorar o/")
            else:
                print("Tente Novamente!")
            
    
   