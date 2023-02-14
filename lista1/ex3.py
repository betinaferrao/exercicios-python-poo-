
x = 0.0
for i in range(1, 6):
    nome = input("Nome: ")
    nota = float(input("Nota: "))
    valor_mensalidade = float(input("Valor mensalidade: "))
    if x < nota:
        x = nota
        nomeMaior = nome
        mensalidade = valor_mensalidade
        valorMensalidadeMaior = valor_mensalidade - (valor_mensalidade * 0.3)
        
print("Nome: ", nomeMaior, "\nMensalidade normal: ", mensalidade, "\nMensalidade com desconto: ", valorMensalidadeMaior)
        


        

