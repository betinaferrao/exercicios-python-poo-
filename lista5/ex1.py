n = 1
posicao = 0
while ( 1 <= n <= 100):
    n = int(input("Número de comandos emitidos pelo sargento: "))
    if n == 0:
        break
    c = input("Comandos emitidos pelo sargento: ").upper()
    for i in c:
        if i == 'D':
            posicao += 90
        if i == 'E':
            posicao -= 90
    
        if posicao == 360:
            posicao = 0
        
    if posicao == 0:
        print('N')
    elif posicao == 180 or posicao == -180:
        print('S')
    elif posicao > 0:
        print('L')
    else:
        print('O')
        

else:
    n = int(input("Digite o número de comandos emitidos pelo sargento novamente: "))