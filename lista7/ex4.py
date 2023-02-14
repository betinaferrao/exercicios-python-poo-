n = int(input("Quantidade de casos teste: "))
cont = 0
numeros = []
vencedor = 0
while (cont < n):
    qt, s = input("Quantidade de alunos do grupo e número secreto: ").split()
    qt, s = int(qt), int(s)
    
    for i in range(qt):
        num_chutado = int(input("Digite o número que cada aluno do grupo chutou: "))
        numeros.append(num_chutado)
    
    for i in range(len(numeros)):
        if numeros[i] == s and vencedor < numeros.index(numeros[i]):
            vencedor = numeros.index(numeros[i]) + 1
            
          
    #Achar o número mais próximo
    menor_diferenca = abs(numeros[0] - s)
    for numero in numeros:
        diferenca_atual = abs(numero - s)
        if diferenca_atual < menor_diferenca:
            vencedor = numeros.index(numero) + 1
            menor_diferenca = diferenca_atual
            
    
    
    print("O número da posição do ganhador é: {}".format(vencedor))
    vencedor = 0
    numeros = []
    cont += 1
