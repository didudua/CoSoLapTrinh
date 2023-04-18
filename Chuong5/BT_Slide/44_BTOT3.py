def Input():
    x=int(input())
    L=[]
    n=int(input())
    for i in range(1,n+1):
        L+=[int(input())]
    return L,x
def delete(L,x):
    i=0
    while i<len(L):
        if L[i] == x:
            L=L[:i]+L[i+1:]
        else: i+=1
    return L
    # while i<len(L):
    #     if L[i]==x: 
    #         L.pop(i)
    #     else:
    #         i+=1
    # return L
L,x=Input()
print(delete(L,x))
            