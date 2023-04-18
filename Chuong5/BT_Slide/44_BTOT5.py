def Input():
    x=int(input())
    y=int(input())
    L=[]
    n=int(input())
    for i in range(1,n+1):
        L+=[int(input())]
    return L,x,y
def update(L,x,y):
    for i in range(len(L)):
        if L[i]==x:
            L[i]=y
    return L
L,x,y=Input()
print(update(L,x,y))