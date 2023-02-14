tab = []
tab2 = []

for c in range(n):
    campo = it(input("Digite os valores: "))
    tab.append(campo)

for campo in range(len(tab)):
    total = 0
    if campo == 0:
        if tab[campo] == 1: total += 1
        if tab[campo + 1] == 1: total += 1
    elif campo == (len(tab)-1):
        if tab[campo-1] == total += 1
        if tav[campo] == 1: total += 1
    else:
        if tab[campo-1] == 1: total += 1
        if tab[campo] == 1: total += 1
        if tab[campo+1] == 1: total += 1
    tab2.append(total)
print(tab)
print(tab2)