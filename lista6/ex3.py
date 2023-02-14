tupla = (1,2,3,4,5,6,7,8,9,10)

for i in range(0, len(tupla)):
    if i == 0:
        maior = tupla[i]
        menor = tupla[i]
    if (tupla[i] > maior):
        maior = tupla[i]
    if (tupla[i] < menor):
        menor = tupla[i]
        
index_maior = tupla.index(maior)
index_menor = tupla.index(menor)
print(f'Maior número: {maior} | Posição: {index_maior}')
print(f'Menor número: {menor} | Posição: {index_menor}')