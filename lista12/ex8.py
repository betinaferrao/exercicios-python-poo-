n, n1 = input("Digite o número de palavras e de textos: ").split()
n, n1 = int(n), int(n1)
dic = {}
for i in range(n):
    palavra, valor = input("Digite uma palavra e o valor para ela: ").split()
    valor = int(valor)
    dic[palavra] = valor

for i in range(n1):
    texto = input("Digite o texto: ")
    print(dic)

    soma = 0
    for p in texto.split():
        if p in dic.keys():
            soma += dic[p]
    print(soma)
