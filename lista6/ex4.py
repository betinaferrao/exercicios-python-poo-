n = int(input("Quantos elementos? "))
numeros = list()
lista = list()
for i in range(n):
    numero = int(input("Número: "))
    numeros.append(numero)

k = int(input("Número multiplicativo: "))
for j in numeros:
    lista.append(j * k)

print(lista)

