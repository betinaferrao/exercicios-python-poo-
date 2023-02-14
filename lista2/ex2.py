from random import randrange
num = randrange(10)
teclado = int(input("Digite um número entre 0 e 10: "))
cont = 1
while(num != teclado):
    teclado = int(input("Tente novamente: "))
    cont += 1

print('Parabéns! O número secreto era: {}. Tentativas: {}'.format(num, cont))