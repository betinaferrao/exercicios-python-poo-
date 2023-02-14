from datetime import datetime
menu = "1)Cadastrar usuário \n2)Imprimir dados (pesquisar pelo nome) \n3)Imprimir dados (todos os usuários) \n4)Encerrar o programa"
print(menu)
lista = []
dados = {}
while True:
    op = int(input("\nOpção: "))
    #cadastrar
    if op == 1:
        while True:
            dados['nome'] = str(input("Nome: "))
            nasc = int(input("Ano de nascimento: "))
            dados['idade'] = ((datetime.now().year) - nasc)
            dados['ctps'] = int(input("Carteira de trabalho (0 - não tem): "))
            if dados['ctps'] != 0:
                dados['contratação'] = int(input("Ano de Contratação: "))
                dados['salario'] = float(input("Salário: "))
                dados['aposentadoria']= dados['idade'] + ( (dados['contratação']+35) - datetime.now().year)
            lista.append(dados.copy())
            print(lista)                              
            novamente = str(input('Cadastrar outra pessoa? [S/N] ')).upper()
            if novamente == 'N':
                break
            
    #Imprimir dados (pesquisar pelo nome)
    if op == 2:
        flag = False
        nome = input("Digite o nome: ")
        for j in range(len(lista)):   
            if lista[j]['nome'] == nome:
                e = lista[j]
                for v in e.values():
                    print(v, end = " ")
                flag = True
        if flag == False:
            print("Nome não encontrado no cadastro.")

    #Imprimir dados (todos os usuários)
    if op == 3:
        for i in lista:
            for e in i.values():
                print(e, end= ' ')
            print()

    if op == 4:
        print("Programa encerrado! ")
        break
    
