while True:
    s=0
    n=int(input('n='))
    if n<=0: break
    for i in range(1,n+1):
        if n%i==0: s+=i
    print(s)