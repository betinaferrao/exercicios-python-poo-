num = int(input("Digite um número para ver sua tabuada: "))
cont = 1

while(cont <= 10):
    tab = cont * num
    print(cont, ' x ', num, ' = ', tab)
    cont += 1