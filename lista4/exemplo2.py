def maiorQueZero(numeros):
    cont = 0
    soma = 0
    for i in range(numeros):
        n = float(input("Digite o número: "))
        if (n > 0):
            cont += 1
            soma += n
    media = soma / cont
    print("{} valores positivos.\nMédia: {} ".format(cont, media))   

numeros = int(input("Quantos números quer ler: "))
maiorQueZero(numeros)
