par = 0
impar = 0
for i in range(0,10):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1

print("Quantidade de números ímpares: ", impar, "\nQuantidade de números pares: ", par)
    