empresa1 = set()
empresa2 = set()
total = set()

while True:
        print("MENU")
        print("1-Relação de clientes cadastrados por empresa")
        print("2-Cadastrar novos clientes")
        print("3-Verificar se já existem clientes cadastrados nas 2 empresas e ver quais são esses clientes")
        print("4-Verificar o número de clientes")
        n = int(input('\nDigite a opção escolhida: '))
        
        while n < 0 or n > 4:
            n = int(input('Opção Inválida. Digite novamente a opção escolhida: '))
        
        if n == 1:
            print("Clientes da empresa 1: {}".format(empresa1))
            print("Clientes da empresa 2: {}".format(empresa2))
            
        if n == 2:
            emp1 = int(input("Digite o número de clientes novos da Empresa 1: "))
            for i in range(emp1):
                empresa1.add(input("Nome do novo cliente: "))

            emp2 = int(input("Digite o número de clientes novos da Empresa 2: "))
            for i in range(emp2):
                empresa2.add(input("Nome do novo cliente: "))
            
        if n == 3:
            for a in empresa1.intersection(empresa2):
                total.add(a)
                
            print(f'Existem {len(total)} de clietes nas duas empresas.')
            print(f'Os clientes que possuem direito ao desconto são {total}')
            
        if n == 4:
            print("1- Número de clientes da empresa 1")
            print("2- Número de clientes da empresa 2")
            print("3- Número de clientes já pertencetes a ambas as empresas")
            print("4- Número de clientes pertencentes a apenas 1 das empresas")
            print("5- Número total de clientes")
            op = int(input('\nDigite a opção escolhida: '))
            if op == 1:
                print("Número de clientes da empresa 1: {}".format(len(empresa1)))
            if op == 2:
                print("Número de clientes da empresa 2: {}".format(len(empresa2)))
            if op == 3:
                print("Número de clientes já pertencentes a ambas as empresas: {}".format(len(total)))
            if op == 4:
                print("Número de clientes pertencentes a apenas 1 das empresas: {}".format(empresa1.symmetric_difference(empresa2)))
            if op == 5:
                print("5- Número total de clientes: {}".format(len(empresa1.union(empresa2))))
        continuar = input('Você deseja continuar? [S/N] ').upper().strip()
        if continuar == 'N':
            break
        
        