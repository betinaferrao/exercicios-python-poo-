from math import trunc
def aumento(salario, percentual):
    reajuste = salario * percentual
    novo_salario = salario + reajuste
    print("Novo salario:{} \nReajuste ganho:{:.2f} \nEm percentual {}%".format(novo_salario,reajuste,trunc(percentual*100)))


salario = float(input("Qual o salario? "))
if 0 <= salario <= 400.00 :
    percentual = '15%'
    aumento(salario,0.15)
elif 400.01 <= salario <= 800.00:
    percentual = '12%'
    aumento(salario,0.12)  
elif 800.01 <= salario <= 1200.00:
    percentual = '10%'
    aumento(salario,0.10)
elif 1200.01<= salario <= 2000.00:
    percentual = '7%'
    aumento(salario,0.07)
else:
    percentual = '4%'
    aumento(salario,0.04)

print("Fim")