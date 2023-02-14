n, m = input("Número de participantes e número de problemas: ").split()
n, m = int(n), int(m)

lista = list()
linha = list()

if n != 0 or m != 0:
    for j in range(m):
        for i in range(n):
            num = int(input("O {}° competidor resolveu o {}° problema? (1- sim, 0- não) ".format(i+1, j+1)))
            linha.append(num)
        lista.append(linha[:])
        linha.clear()

    print(lista)
    
    cont = 0
    for l in range(0,n):
        for c in range(0,m):
            print(f'[{lista[l][c]}]',end=" ")
            if lista[l][c] == 1:
                cont += 1
        print()
    
    print("Características alcançadas na competição:", cont)
    
    
else:
    print(" ")

