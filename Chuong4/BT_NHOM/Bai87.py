def nhap():
    n=input()
    chieurong=int(input('nhap chieu rong: '))
    return n,chieurong
def inkq(n, chieurong):
    if chieurong <= len(n):
        kq=n
        return kq
    else:
        khoantrong = (chieurong - len(n)) // 2
        kq= ' '*khoantrong + n +' '*khoantrong
        return kq
n,chieurong=nhap()
print(inkq(n, chieurong))