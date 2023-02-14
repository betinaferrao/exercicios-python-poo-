
def calcularMedia (soma):
    media = soma/5
    return media


maior = 0
soma = 0
for i in range(5):
    nota = int(input("Nota do %i° aluno: " % (i+1)))
    soma += nota
    if i == 0:
        maior = nota
    elif (nota>maior):
        maior = nota

media = calcularMedia(soma)
print("Média da turma: {}".format(media))
print("Aluno com a nota mais alta possui nota de %.2f" % maior)
if (maior > 5.75):
    print("Aprovado!")
elif (2.75 < maior < 5.75):
    print("Em recuperação!")
elif (maior < 2.75):
    print("Reprovado!")