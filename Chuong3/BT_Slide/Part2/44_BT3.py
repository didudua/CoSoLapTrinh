n = int(input('n='))
while n >= 0 and n <= 9999:
    if n >= 10 and n < 100:
        print(n, 'co 2 chu so')
    elif n >= 100 and n < 1000:
        print(n, 'co 3 chu so')
    elif n >= 1000 and n < 10000:
        print(n, 'co 4 chu so')
    else:
        print(n, 'co 1 chu so')
    break
