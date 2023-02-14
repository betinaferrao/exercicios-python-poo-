n = int(input("Deseja criar uma matriz de que ordem: "))
matriz = []
for i in range(n):
    linha = []
    for j in range(n):
        num = int(input("Número da {}° linha e {}° coluna: ".format(i+1, j+1)))
        linha.append(num)
    matriz.append(linha[:])
    linha.clear()

print(matriz)
for i in range(0, n):
    for j in range(0, n):
        print(f'[{matriz[i][j]}]',end = " ")
    print()

par = cont = somaDiagP = somaAcima = cont1 = somaUltimos = 0
prodDiagS = 1

for i in range(0, n):
    for j in range(0, n):
        if (matriz[i][j] % 2 == 0):
            par += matriz[i][j]
        if i == j:
            somaDiagP += matriz[i][j]
            cont += 1
        if (i + j == n - 1):
            prodDiagS *= matriz[i][j]
        if j > i:
            somaAcima += matriz[i][j]
            cont1 += 1
        if j == (n - 1):
            somaUltimos += matriz[i][j]
        if i == 0:
            if j == 0:
                menor = matriz[i][j]
            if matriz[i][j] < menor:
                menor = matriz[i][j]
            
mediaDiagP = somaDiagP / cont
mediaAcima = somaAcima / cont1

print("Soma de todos os elementos pares da matriz: {}".format(par))
print("Média dos elementos da diagonal principal: {:.2f}".format(mediaDiagP))
print("Produto dos elementos da diagonal secundária: {}".format(prodDiagS))
print("Média dos elementos acima da diagonal principal: {}".format(mediaAcima))
print("Soma dos elementos da última coluna da matriz: {}".format(somaUltimos))
print("O menor valor da primeira linha da matriz é: {}".format(menor))