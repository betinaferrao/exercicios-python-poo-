import random
lista = []
jogo = []
n = int(input("Quantos jogos serão sorteados? "))
for i in range(n):
    for j in range(6):
        num = random.randint(1, 60)
        lista.append(num)
    jogo.append(lista[:])
    lista.clear()
    
print("-"*6, end="")
print(f' SORTEANDO {n} JOGOS ', end="")
print("-"*6)

for i in range(n):
    print("JOGO {}: {} ".format(i+1, jogo[i]))
    
print("-"*10, end="")
print(f' BOA SORTE ', end="")
print("-"*10)