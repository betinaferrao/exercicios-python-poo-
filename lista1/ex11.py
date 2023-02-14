soma = 0


num = int(input("Deseja ler quantos números? "))
for i in range(0, num):
    n = int(input("Digite um número: "))
    soma += n
    if(i == 0):
        maior = n
        menor = n
    else:
        if(n > maior):
            maior = n
        if (n < menor):
            menor = n  
media = soma / num
print("Média entre números lidos: ", media, "\nMaior: ", maior, "\nMenor: ", menor)