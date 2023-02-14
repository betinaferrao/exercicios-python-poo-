while True:
    x, y = input().split()
    x, y = int(x), int(y)
    if x == y:
        break
    if x > y:
        print("Decrescente")
    elif y > x:
        print("Crescente")
