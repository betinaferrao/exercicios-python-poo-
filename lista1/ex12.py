maiorDist = 0
somaDist = 0
soma = 0
praias = int(input("Deseja cadastrar quantas praias? "))
for i in range(0, praias):
    nome = input("Nome da praia: ")
    dist = int(input("Distância do centro da cidade: "))
    if(dist > maiorDist):
        maiorDist = dist
        nomeMaior = nome
    if(20 > dist > 15):
        soma += 1
    somaDist += dist
media = somaDist / praias
   
print("Praia mais distante do centro: %s \nQuantidade de praias entre 15 e 20km do centro: %d \nDistância média das praias: %.1f" % (nomeMaior, soma, media))