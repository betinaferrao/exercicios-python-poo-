numeros = (int(input("Digite um número: ")),
           int(input("Digite um número: ")),
           int(input("Digite um número: ")),
           int(input("Digite um número: ")),
           int(input("Digite um número: ")))

cont = 0
pos = 0
pares = ""
for i in numeros:
    if i == 9:
        cont += 1
    if i == 3 and pos < numeros.index(i):
        pos = numeros.index(i)
    if i % 2 == 0:
        pares += str(i) + " "
        
print("O número 9 apareceu {} vez(es).".format(cont))
print("A posição que o primeiro três foi digitado é a {}°.".format(pos+1))
print("Números pares digitados: {}".format(pares))