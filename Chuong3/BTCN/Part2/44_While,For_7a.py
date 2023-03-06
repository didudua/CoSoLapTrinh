while True:
    n = int(input(''))
    u = 1
    if n < 0:
        break
    while n >= 1:
        u = u*n
        n = n-1
    print(u)
