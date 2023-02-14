soma = 0
n = int(input("Deseja verificar quantas pessoas? "))

for i in range(0, n):
    idade = int(input("Qual sua idade? "))
    soma += idade

media = soma / n
if media >= 0 and media <= 25:
    print("Turma jovem")
elif media > 25 and media < 61:
    print("Turma adulta")
elif media > 60:
    print("Turma idosa")
