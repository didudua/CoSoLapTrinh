# import itertools

# for i in itertools.count():

for i in range(1, 100):
    n = int(input(''))
    u = 1
    if n <= 0:
        break
    for i in range(1, n+1):
        u *= i
    print(u)
