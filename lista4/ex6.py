def passaOunao(a, b, c, h, l):
    if (a <= h and b <= l):
        simOunao = 'S'
    elif (a <= h and c <= l):
         simOunao = 'S'
    elif (b <= h and a <= l):
         simOunao = 'S'
    elif (b <= h and b <= l):
         simOunao = 'S'
    elif (c <= h and a <= l):
         simOunao = 'S'
    elif (c <= h and b <= l):
         simOunao = 'S'
    else:
         simOunao = 'N'
    return simOunao

a, b, c = input("Dimensões do colchão: ").split()
a, b, c = int(a), int(b), int(c)

h, l = input("Altura e largura da porta: ").split()
h, l = int(h), int(l)

x = passaOunao(a, b, c, h, l)
if x == 'S':
    print("Você escolheu um colhão de tamanho adequado! Parabéns pela compra!")
elif x == 'N':
    print("Você deve procurar outro colchão!")

