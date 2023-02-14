def produtos_disp(M):
    produtos = []
    for i in range(M):
        produto = input(f'Produto {i} - Nome e preço: ').split()
        info = {'nome': produto[0], 'preco': float(produto[1])}
        produtos.append(info.copy())
    return produtos
        
def mostrar_produtos_disp(produtos):
    for e in produtos:
        for v in e.values():
            print(v, end=' ')
        print()

def produtos_comprou(P):
    comprou = []
    for i in range(P):  
        produto = input(f'Produto {i} - Nome e quantidade: ').split()
        info = {'nome': produto[0], 'quantidade': int(produto[1])}
        comprou.append(info.copy())
    return comprou

def valorCompra(comprou, produtos):
    valorCompra = 0  
    for c in comprou:  
        for p in produtos: 
            if c['nome'] == p['nome']:  
                valorCompra += c['quantidade'] * p['preco']
    return valorCompra                 

#Programa Principal
N = int(input('Quantas vezes Parcinova foi à feira: '))  
for ida in range(N):
    M = int(input('Quantos produtos estão disponíveis? '))
    produtos = produtos_disp(M)
    
    mostrar_produtos_disp(produtos)
    
    P = int(input('Quantos produtos Parcinova quer comprar? '))
    comprou = produtos_comprou(P)

    valorCompra = valorCompra(comprou, produtos)                                                   
    print('R$:', valorCompra)