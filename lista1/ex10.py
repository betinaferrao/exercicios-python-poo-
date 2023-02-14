x = 0
for i in range (0, 5):
    nome = input("Nome do aluno: ")
    n1 = int(input("Nota 1: "))
    n2 = int(input("Nota 2: "))
    media = (n1 + n2)/ 2
    if (x == 0 or media > mediaMaior):
        nomeMaior = nome
        mediaMaior = media
        x += 1
        
if(mediaMaior >= 5.75):
    print("Aluno ", nomeMaior, " aprovado! Média: ", mediaMaior)
elif(mediaMaior >= 2.75):
    print("Aluno tem direito a fazer recuperação!")
elif(mediaMaior < 2.75):
     print("Aluno ", nomeMaior, " reprovado! Média: ", mediaMaior)
            

    
    