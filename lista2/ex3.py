c = 'S'
porc = 0
while(c == 'S' or c == 's'):
    sal = float(input("Salário: "))

    desconto = (sal * 0.11)

    if desconto > 320.00:
        salDesconto = sal - 320
        porc = (320 * 100) / sal
    elif desconto < 320.00:
        salDesconto = sal - (sal * 0.11)
        porc = 11
    print("O desconto aplicado foi de %.2f\nNovo salário: %.2f\nPorcentagem do desconto: %.2f" % (desconto, salDesconto, porc))

    c = input("Deseja continuar? (S/N) ")
    if c == 'N' or c == 'n':
        break
    
