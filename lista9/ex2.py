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
while x != 'N':
    t = input("Qual operação será realizada(S- Soma, M- Média)? ").upper().strip()

    soma = 0
    a = n
    if t == 'S':
        for l in range(n-1, 0, -1):
            for c in range(0, a-1, 1):
                soma += matriz[l][c]
            a = a - 1
        print(soma)
    
    x = input("Deseja realizar outra operação? (S/N) ").upper().strip()
    
    cont = 0
    if t == 'M':
        for l in range(n-1, 0, -1):
                for c in range(0, a-1, 1):
                    soma += matriz[l][c]
                    cont += 1
                a = a - 1
            media = soma / cont
            print(media)
    
    x = input("Deseja realizar outra operação? (S/N) ").upper().strip()
