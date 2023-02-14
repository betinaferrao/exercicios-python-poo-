cont = 0
soma = 0
totCoelho = totRato = totSapo = 0
n = int(input("Casos teste: "))
while (cont < n):
    q, tipo = input("Digite a quantidade de cobaias e o tipo: ").split()
    q, tipo = int(q), tipo.upper()
    if (1 >= q >= 15):
        break
    
    soma += q
    if tipo == 'C':
        totCoelho += q
    if tipo == 'R':
        totRato += q
    if tipo == 'S':
        totSapo += q
    cont += 1

percC = (totCoelho * 100)/ soma
percR = (totRato * 100)/ soma
percS = (totSapo * 100)/soma
    
print("Total: %.0f\nTotal de coelhos: %.0f\nTotal de ratos: %.0f\nTotal de sapos: %.0f\nPercentual de coelhos: %.2f\nPercentual de ratos: %.2f\nPercentual de sapos: %.2f" % (soma, totCoelho, totRato, totSapo, percC, percR, percS))