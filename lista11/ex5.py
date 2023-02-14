n = int(input("Deseja ver o boletim de quantos alunos? "))
notas = []
lista = []
for i in range(n):
    nome = input("Nome: ")
    notas.append(nome)
    for j in range(3):
        nota = int(input("{}° Nota: ".format(j+1)))
        notas.append(nota)
    lista.append(notas[:])
    notas.clear()
print(lista)

medias = []
soma = 0
for i in range(0, n):
    for j in range(1, 4):
        soma += lista[i][j]
    media = soma / 3
    medias.append(media)
    soma = 0

print(medias)

for i in range(0, n):
    print("Média de {}: {:.2f}".format(lista[i][0], medias[i]))
print()
for i in range(0, n):
    print("Notas parciais de {}: {:.2f}, {:.2f}, {:.2f}".format(lista[i][0], lista[i][1], lista[i][2], lista[i][3] ))


