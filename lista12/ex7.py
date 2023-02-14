while True:
    n = int(input("Número de alunos na sala: "))
    lista = []
    dic = {}
    for i in range(n):
        mat = int(input("Número da matrícula: "))
        sigla_curso = input("Sigla do curso: ")
        dic['matricula'] = mat
        dic['curso'] = sigla_curso
        lista.append(dic.copy())

    epr = ehd = intrusos = 0
    for i in lista:
        if i['curso'] == 'EPR':
            epr += 1
        if i['curso'] == 'EHD':
            ehd += 1
        if i['curso'] != 'EPR' and i['curso'] != 'EHD':
            intrusos += 1

    print("EPR: ", epr)
    print("EHD: ", ehd)
    print("INTRUSOS: ", intrusos)
    
    x = input("Deseja cotinuar? (S/N) ").upper()
    if x == 'N':
        break
