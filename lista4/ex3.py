##1150

def valor (x, z):
    soma = 0
    cont = 0
    while(soma <= z):
        soma = soma + (x + cont)
        cont += 1
    print("Quantidade de inteiros: {}".format(cont))
    
x = int(input("Digite um valor para x: "))
z = int(input("Digite um valor para z: "))
while (z <= x):
    z = int(input("Digite outro valor para z: "))
valor(x, z)
    
