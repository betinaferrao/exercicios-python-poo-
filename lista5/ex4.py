
soma = 0
cont = 0
n = int(input("Número de casos teste: "))
while (cont < n):
    if (1 >= n >= 1000):
        break
    else:
        num = input("Digite um número: ")
        if (1 >= int(num) >= 10*100):
            break
        else:
            for i in num:
                if i == '1':
                    soma += 2
                elif i == '2':
                    soma += 5
                elif i == '3':
                    soma += 5
                elif i == '4':
                    soma += 4
                elif i == '5':
                    soma += 5
                elif i == '6':
                    soma += 6
                elif i == '7':
                    soma += 3
                elif i == '8':
                    soma += 7
                elif i == '9':
                    soma += 6
                elif i == '0':
                    soma += 6
            print(soma, "leds")
            soma = 0
    cont += 1
        
    
    

