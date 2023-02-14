notas = {'W':1, 'H':1/2, 'Q':1/4, 'E':1/8, 'S':1/16, 'T':1/32, 'X':1/64}

composicao = input("Composição: ")

while (composicao != '*'):
    corretas = 0
    compasso = 0
    
    for letra in composicao:
        if (letra == '/'):
            if (compasso == 1):
                corretas += 1
            compasso = 0
        else:
            compasso += notas[letra]
    
    print (corretas)
    corretas = 0
    composicao = input("Composição: ")