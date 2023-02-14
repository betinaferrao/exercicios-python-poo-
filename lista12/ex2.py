def nomeLingua(n):
    lista = []
    dic = {}
    for i in range(n):
        lingua = input("Nome de uma língua: ")
        trad = input("Tradução de 'Feliz Natal' para essa língua: ")
        dic['lingua'] = lingua
        dic['tradução'] = trad
        lista.append(dic.copy())
    return lista

def pessoas(m):
    lista2 = []
    dic1 = {}
    for i in range(m):
        nome = input("Nome da criança: ")
        lingua_nativa = input("Língua nativa da criança: ")
        dic1['nome'] = nome
        dic1['lingua_nativa'] = lingua_nativa
        lista2.append(dic1.copy())
    return lista2

def felizNatal(lista, lista2):
    for i in lista:
        for j in lista2:
            if i['lingua'] == j['lingua_nativa']:
                print(j['nome'], " = ", i['tradução'])       

#Código Principal
n = int(input("Quantidade de traduções da palavra 'Feliz Natal': "))
lista = nomeLingua(n)
m = int(input("Quantidade de crianças que receberão as cartas: "))
lista2 = pessoas(m)

felizNatal(lista, lista2)

print(lista)
print(lista2)


