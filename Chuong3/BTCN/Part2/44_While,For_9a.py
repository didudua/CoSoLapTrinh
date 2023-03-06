n=int(input())
u=2
while n>=2 and n<=50: 
    if n%2==0:
        while u<=n:
            print(u,end=" ")
            u=u+2
    while u<n:
        print(u,end=" ")
        u=u+2
    n=n+50
        