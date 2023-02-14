#1154

def mediaIdade(i):
    cont = 0
    soma = 0
    while(i>0):
        i = int(input("Idade: " ))
        cont += 1
        soma += i
    media = soma / cont
    return media

i = int(input("Idade: " ))
total = mediaIdade(i)
print(total)