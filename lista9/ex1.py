from random import randint

n = int(input("Tamanho da matriz: "))
matriz = list()

for l in range(n):
    linha = []
    for c in range(n):
        numero = randint(1, 10)
        linha.append(numero)
    matriz.append(linha)

print(matriz)

for l in range(0,n):
    for c in range(0,n):
        print(f'[{matriz[l][c]}]',end=" ")
    print()

x = ""
cont = 0
while x != 'N':
    l = int(input("Qual linha será considerada para a operação? "))
    t = input("Qual operação será realizada(S- Soma, M- Média)? ").upper().strip()

    soma = 0
    if t == 'S':
        for i in range(n):
            soma += matriz[l][i]
        print(soma)
        x = input("Deseja realizar outra operação? (S/N) ").upper().strip()

    if t == 'M':
        #for i in range(n):
            #soma += matriz[l][i]
            #cont += 1
        media = soma / cont
        print(media)
        x = input("Deseja realizar outra operação? (S/N) ").upper().strip()

    
    

