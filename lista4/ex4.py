def quadrante(x, y):
    if (x > 0 and y > 0):
        print("Primeiro quadrante")
    elif (x < 0 and y > 0):
        print("Segundo quadrante")
    elif (x < 0 and y < 0):
        print("Terceiro quadrante")
    elif (x > 0 and y < 0):
        print("Quarto quadrante")

x = y = 1
while (x != 0 and y != 0):            
    x, y= input("Número 1 e 2: ").split()
    x, y = int(x), int(y)
    quadrante(x, y)
        
        
        