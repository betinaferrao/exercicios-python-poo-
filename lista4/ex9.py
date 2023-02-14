def primos(numero):
    primo = 0
    if (numero % 2 == 0):
        primo = 1
    return primo

éPrimo = cont = 0
num = int(input("Deseja ler quantos números: "))
while (cont < num):
    numero = int(input("Número: "))
    p = primos(numero)
    if p == 1:
        éPrimo += 1
    cont += 1
print("Quantidade de números primos: %i" % éPrimo)
    
    