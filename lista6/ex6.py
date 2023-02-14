
while True:
    n = input("Quantidade de algarismos do número [1-10]: ")
    nValue = int(n)
    while nValue < 1 or nValue > 10:
        print("\nValor inválido! Tente novamente")
        n = input("Quantidade de algarismos do número: ")
        nValue = int(n)
    
    
    m = input("\nNúmero a ser verificado: ")
    mValue = int(m)
    while len(m) != nValue or mValue < 1 or mValue > 10**9:
        print("\nNúmero inválido! Tente novamente")
        m = input("Número a ser verificado: ")
        mvalue = int(m)
    
    
    soma = 0
    for i in m:
        soma += int(i)
    if soma % 3 == 0:
        print("{} - sim".format(soma))
    else:
        print("{} - não".format(soma))
    
    
    escolha = input("Deseja continuar? [S/N]: ").strip().upper()
    while len(escolha) == 0 or escolha not in 'SN':
        print("\nEscolha um 'S' ou 'N'!")
        escolha = input("Deseja continuar? [S/N]: ").strip().upper()
        
    if escolha == 'N':
        break
    