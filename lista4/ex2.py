#2057
'''def fuso (s, t, f):
    fim = ((s + t + f) % 24)
    print(fim)

s = int(input("Hora de saída: "))
t = int(input("Tempo de viagem: "))
f = int(input("Fuso horário: "))
fuso(s, t, f)


     
'''
def fuso(s, c, dif):
    x = s + c + dif
    if (dif >= 24):
        x -= 24
    elif (dif < 0):
        x += 24
    print(f"A hora de chegada do vôo é às {x} horas")
    
    
fuso(int(input("Informe o horário de saída do vôo: ")), int(input("Informe o horário de chegada do vôo: ")), int(input("Informe a diferença de fuso horário entre a partida e o destino: ")))