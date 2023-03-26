def nhap():
    a=int(input('So mat hang ma khach hang mua:'))
    return(a)
def tinhtien(a):
    if a==1:
        t=10.95
    if a>1:
        t=10.95+(a-1)*2.95
        return(t)
def inkq(t):
    print('So tien phai tra',t)
a=nhap()
t=tinhtien(a)
inkq(t)