def calcularMediaPositivos(pos, cont):
    media = pos / cont
    return media
    
cont = 0
pos = 0
for i in range(6):
    n = float(input("Valor: "))
    if n > 0:
        pos += n
        cont += 1
media = calcularMediaPositivos(pos, cont)
print("%i valores positivos.\nMédia: %.1f" % (cont, media))