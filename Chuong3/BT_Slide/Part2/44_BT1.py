n = int(input('n='))
u=1
if n >= 0 and n <= 100:
    for i in range(1,n+1):
        u = i*u
    print(n,'!=',u, sep="")