def int2hex(n,doi):
    kq = ''
    while True:
        du = n % 16
        kq = doi[du] + kq
        n //= 16
        if n == 0:
            break
    return kq

def hex2in(n,doi):
    mu = len(n)-1
    kq = 0
    for i in n:
        kq += doi.index(i)*16**mu
        mu -= 1
    return kq

he10=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
he16='0123456789ABCDEFabcdef'
doi = '0123456789ABCDEF'
n = input('Nhap so thap phan: ')
xethe=input('so ban nhap thuoc he: ')
if int(xethe)==0 or int(xethe)== 16:
    if int(xethe)==10 and n in he10:
        print(f'doi sang thap luc phan la: {int2hex(int(n),doi)}')
    else:
        print('he 10 chi nhan cac gia tri tu 0-15. hay nhap lai')
    if int(xethe)==16 and n in he16:
        n=n.upper()
        print(f'doi sang thap phan la: {hex2in(n,doi)}')
    else: print(f'he 16 chi nhan cac gia tri (0123456789abcdef) gom chu hoa va thuong. hay nhap lai')
else: print('hay nhap lai chuong trinh chi nhan he 10 va 16')