casa = 0
escritorio = 0
cont = 0
sn1 = 0
sd1 = 0
dias = int(input("Quantidade de dias previstos pelo sistema metereológico: "))
while (cont < dias):
    sd, sn = input("Previsão do tempo para ida e volta do trabalho: ").lower().split()
    
    if sn1 != sd:
        if sd == 'chuva':
            casa += 1
        if sn == 'chuva':
            escritorio += 1
    sd1 = sd
    sn1 = sn
    
    cont += 1

print(casa, escritorio)    
    
    