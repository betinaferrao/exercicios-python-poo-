def elevador(leituras):
    cont = 0
    total = 0
    for i in range(leituras):
        s, e = input("Quantas pessoas saíram e entraram no andar? ").split()
        s, e = int(s), int(e)
        #if (i == 0):
        #    total = e
        #else:
        total = total - s + e
        if (total > cap_max):
            cont += 1
    if (cont >= 1):
        print('S')
    else:
        print('N')


while True:
    leituras = int(input("Número de leituras realizadas pelo sensor: "))
    cap_max = int(input("Capacidade máxima do elevador: "))
    if (1 <= leituras <= 1000) and (1 <= cap_max <= 1000):
        break
elevador(leituras)