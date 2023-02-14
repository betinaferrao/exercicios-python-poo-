n = int(input("Deseja mostrar quantos números da sequência de Fibonnaci? "))
t1 = 0
t2 = 1
cont = 1
print(t1)
while(n >= cont+1):
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1
    print(t3)
