alunos = int(input("Digite a quantidade de alunos da turma: "))
for i in range(alunos):
    soma = 0
    notas = list()
    for i in range(3):
        nota = int(input("Digite a nota: "))
        while (0 > nota) or (nota > 10):
            print("\nValor inválido! Tente novamente")
            nota = int(input("Digite a nota: "))
        notas.append(nota)
        
        if i == 0:
            maior = notas[0]
            menor = notas[0]
            
        if (notas[i] > maior):
            maior = notas[i]
            
        if (notas[i] < menor):
            menor = notas[i]
            
        soma += notas[i]

    media = soma / 3
    dif = maior - menor
    print("Média do aluno: {:.1f}\nNota maior: {}\nNota menor: {}\nDiferença entre notas maior e menor: {}".format(media, maior, menor, dif))
    soma = 0
