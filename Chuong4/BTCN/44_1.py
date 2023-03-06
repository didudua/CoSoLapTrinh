def nhap():
    n=int(input('n='))
    return n
def giaithua(n):
    X=1
    if n ==0:
        X=1
    while n>0: 
        X=n*X
        n=n-1
    return X
def inkq(n,X):
    print(n,'!=',X,sep='')
n=nhap()
X=giaithua(n)
inkq(n,X)
        