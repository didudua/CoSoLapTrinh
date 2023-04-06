def Input():
    L=[]
    n=int(input('n='))
    for i in range(1,n+1):
        L+=[int(input())]
    x=int(input('x='))
    return L,x
def FirstAndLast(L):
    print(f'[{L[0]},{L[-1]}]')
def Search(L,x):
    if x in L: return True
    else: return False

L,x=Input()
FirstAndLast(L)
print(Search(L,x))