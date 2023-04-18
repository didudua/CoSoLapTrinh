def Input():
    L=[]
    n=int(input())
    for i in range(1,n+1):
        L+=[int(input())]
    return L
def count(L):
    # return len(L)
    u=0
    for i in L:
         u+=1
    return u
print(count(Input()))