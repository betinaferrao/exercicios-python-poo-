primo = 0

num = int(input())
for i in range (1, num+1):
    if num % i == 0:
        primo += 1

if primo == 2 :
    print("É primo!")
else:
    print("Não é primo!")
    for c in range(1, num+1):
        if num % c == 0:
            print(c)