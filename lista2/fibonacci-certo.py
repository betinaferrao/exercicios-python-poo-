h = int(input("h: "))
t1 = 0
t2 = 1
c = 0
while h > c:
    if(c%2 == 0):
        print(t1)
        t1 = t1 + t2
    else:
        print(t2)
        t2 = t2 + t1
    c += 1
