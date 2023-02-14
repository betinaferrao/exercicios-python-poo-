
s = input("Qual o sexo da pessoa (M/F): ").upper()
while (s != 'M' and s != 'F'):
    s = input("Digite novamente (M/F): ").upper()

if (s == 'F'):
    print("Pessoa do sexo feminino!" )
elif (s == 'M'):
    print("Pessoa do sexo masculino!" )

    
        