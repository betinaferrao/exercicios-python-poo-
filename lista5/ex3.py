n = int(input("Número de casos de teste: "))
cont = 0
while (cont < n):
    n1, l, n2 = input("Digite um número, uma letra e outro número: ")
    n1, l, n2 = int(n1), l, int(n2)
    
    if n1 != n2:
        if (l.upper() == l):
            fim = n2 - n1
        else:
            fim = n1 + n2
    else:
        fim = n1 * n2
    
    print(fim)
    cont += 1
    