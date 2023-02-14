def media (n, soma):
    soma += n
    return soma

n = 1
cont = 0
soma = 0
while True:
    n = int(input("Idade: "))
    if n < 0:
        break
    soma = media(n, soma)
    cont += 1
    
media = soma / cont
print("{:.2f}".format(media))