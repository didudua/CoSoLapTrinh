def nhap():
    n=int(input('n='))
    print('Nhap', n, 'so nguyen:')
    return n

def NhapVaDem(n):
    kq = 0
    while n > 0:
        a = int(input())
        if a % 2 == 0 and a != 0:
            kq = kq+1
        n = n-1
    return kq
def InKQ(kq):
    print('So chu so chan la:', kq)


n=nhap()
kq=NhapVaDem(n)
InKQ(kq)
