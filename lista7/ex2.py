from random import randint

numero = (randint(1, 10),
          randint(1, 10),
          randint(1, 10),
          randint(1, 10),
          randint(1, 10))

maior = 0
menor = 0

for i in numero:
    if numero.index(i) == 0:
        maior = i
        menor = i
    if i > maior:
        maior = i
    if i < menor:
        menor = i

print("Tupla: {}.\nMaior: {}\nMenor: {}".format(numero, maior, menor))