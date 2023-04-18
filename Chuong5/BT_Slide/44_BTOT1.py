def Input():
    x=int(input())
    k=int(input())
    L=[]
    n=int(input())
    for i in range(1,n+1):
        L+=[int(input())]
    return L,x,k
def add(L,x,k):
    if k>len(L):
        L=L+[x]
    else:
        L=L[:k]+[x]+L[k:]
    return L
L,x,k=Input()
print(add(L,x,k))
