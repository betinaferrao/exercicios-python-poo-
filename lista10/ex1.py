mergulhou = list()
voltou = list()
n, r = input("Digite o número de voluntários que mergulhou e número de voluntários que retornou do mergulho? ").split()
n = int(n)
r = int(r)

for i in range(n):
    mergulhou.append(i+1)
    
for i in range(r):
    voluntario = int(input("Digite o {}° voluntário que retornou? ".format(i+1)))
    voltou.append(voluntario)

naoVoltou = ""
voltou1 = 0
for i in mergulhou:
    if i not in voltou:
        naoVoltou += str(i) + " "
    else:
        voltou1 += i
    if voltou1 == n:
        naoVoltou = "*"
    
print("Voluntários que não retornaram: {}".format(naoVoltou))