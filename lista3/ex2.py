n = int(input("Casos testes: "))
cont = 1
soma_i = 0
while(n >= cont):
    x, y = input().split()
    x, y = int(x), int(y)
    if y > x:
        for i in range(x+1, y):
            if i % 2 != 0:
                soma_i += i
    elif x > y:
        for i in range(y+1, x):
            if i % 2 != 0:
                soma_i += i
    cont += 1

    print(soma_i)
    soma_i = 0
    