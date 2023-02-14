n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma = 0
if n2 > n1:
    for i in range(n1+1, n2, 1):
        print(i)
        soma += i
elif n1 > n2:
    for c in range(n1-1, n2, -1):
        print(c)
        soma += c
print("Soma: ", soma)
        


