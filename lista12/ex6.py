n = int(input("Digite o número de inteiros: "))
dic = {}
num = input("Números: ").split()

for i in num:
    if i not in dic.keys():
        dic[i] = 1
    else:
        dic[i] += 1

print(dic)
    
for k, i in dic.items():
    if i % 2 == 1:
        print(k)

    
    