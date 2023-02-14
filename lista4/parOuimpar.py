def parOuImpar(n):
    par = impar = 0
    if (n % 2 == 0):
        par += 1
        print("É par")
    else:
        impar += 1
        print("É ímpar")
    return par, impar

cont = 0
pares = 0
impares = 0
while (cont < 10):
    n = int(input("Digite um número: "))
    x, y = parOuImpar(n)
    pares += x
    impares += y
    cont += 1
print("Total de números pares: %d" % (pares))
print("Total de números ímpares: %d" % (impares))    