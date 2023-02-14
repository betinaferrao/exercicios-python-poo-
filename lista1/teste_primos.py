def primo(num, count, primo, naoPrimo):
    for c in range(1, num + 1):
        if (num % c == 0):
            count += 1
    if count > 2:
        print("Não é primo")
        naoPrimo += 1
    else:
        print("É primo")
        primo += 1
    return primo, naoPrimo
    
p = np = 0
soma = 0      
count = 0
quant = int(input('Quantos números você deseja ler? '))
while (quant != soma):
    num = int(input('Digite um número: '))
    p, np = primo(num, count, p, np)
    soma += 1
print("Quantidade de primos: ", p)
print("Quantidade de não primos: ", np)

