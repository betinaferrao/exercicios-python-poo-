def contador(inicio, fim, passo):
    if fim > inicio:
        for i in range(inicio, fim+1, passo):
            print(i)
    elif inicio > fim:
        for i in range(inicio, fim-1, -passo):
            print(i)

contador(1, 10, 1)
contador(10, 0, 2)
x, y, z = input("Contagem personalizada (Passe valores para o início, fim e passo): ").split()
x, y, z = int(x), int(y), int(z)
contador(x, y, z)