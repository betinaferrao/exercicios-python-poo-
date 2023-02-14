lista = list()
for i in range(19):
    n = int(input("Número: "))
    lista.append(n)
    
tam = len(lista)

for i in range(tam//2):
    a = lista[i]
    b = lista[tam-i-1]
    
    lista[i] = b
    lista[tam-i-1] = a

print(lista)
    