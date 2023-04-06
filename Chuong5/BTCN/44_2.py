def Input():
    L=[]
    n=int(input('n='))
    for i in range(1,n+1):
        L+=[int(input())]
    return L
def Search(L):
    m=max(L)
    n=min(L)
    return m,n
def Output(max,min):
    print(f'{max} {min}')
L=Input()
m,n=Search(L)
Output(m,n)