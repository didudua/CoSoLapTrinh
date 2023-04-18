def Input():
    x=int(input())
    L=[]
    n=int(input())
    for i in range(1,n+1):
        L+=[int(input())]
    return L,x
def search(L,x):
    if x in L:
        # return L.index(x)
        for i in range(len(L)):
            if L[i]==x:
                return i
        else: return None
L,x=Input()
print(search(L,x))