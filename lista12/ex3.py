def assOriginal(n):
    lista = []
    dic = {}
    for i in range(n):
        nome = input("Nome do aluno: ")
        ass = input("Assinatura Original do aluno: ")
        dic['nome'] = nome
        dic['assinatura_original'] = ass
        lista.append(dic.copy())
    return lista

def assAula(m):
    lista1 = []
    dic1 = {}
    for i in range(m):
        nome = input("Nome do aluno: ")
        ass = input("Assinatura na aula: ")
        dic1['nome'] = nome
        dic1['assinatura_aula'] = ass
        lista1.append(dic1.copy())
    return lista1

def checagem(lista, lista1):
    cont = 0
    for i in lista:
        for j in lista1:
            if i['nome'] == j['nome']:
                if i['assinatura_original'] != j['assinatura_aula']:
                    cont += 1
    return cont


while True:
    n = int(input("Quantidade de alunos da turma: "))
    lista = assOriginal(n)
    if n == 0:
        break
    
    m = int(input("Quantidade de alunos que compareceram a aula: "))
    lista1 = assAula(m)
    
    print(checagem(lista, lista1))
    
    
            
    