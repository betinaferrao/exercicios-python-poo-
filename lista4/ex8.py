def parOuImpar(n):
    par = impar = 0
    if (n % 2 == 0):
        valor = 0
        print("%d - É par" % n)
    else:
        valor = 1
        print("%d - É ímpar" % n)
    return valor

cont = 0
pares = 0
impares = 0
while (cont < 10):
    n = int(input("Digite um número: "))
    x = parOuImpar(n)
    if x == 0:
        pares += 1
    else:
        impares +=1
    cont += 1
print("Total de números pares: %d" % (pares))
print("Total de números ímpares: %d" % (impares))    