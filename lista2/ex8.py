soma = 0
m = 0
n = 0
s = ""
while(m <= 0 or n <= 0):
    m, n = input().split()
    m = int(m)
    n = int(n)
    if m > n:
        for i in range(n, m+1, 1):
            soma += i
            if (i == m):
                s += str(i)
            else:
                s += str(i) + " "
    if n > m:
        for i in range(m, n+1, 1):
            soma += i
            if (i == n):
                s += str(i)
            else:
                s += str(i) + " "
    print("%s Sum=%d" % (s, soma))


