
a = 0
g = 0
d = 0
num = 0

while(num != 4):
    num = int(input("1 - Álcool\n 2 - Gasolina\n 3 - Diesel\n 4 - Fim\n"))
    if (num == 1):
        a += 1
    elif (num == 2):
        g += 1
    elif (num == 3):
        d += 1

print("MUITO OBRIGADO!\n Alcool: %i\n Gasolina: %i\n Diesel: %i" % (a, g, d))