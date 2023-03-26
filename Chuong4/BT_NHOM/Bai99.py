def BatkySangThap(n, hevao, he16):
    mu = len(n)-1
    kq = 0
    if hevao == 16:
        for i in n:
            kq += he16.index(i)*16**mu
            mu -= 1
        return kq
    else:
        for i in n:
            kq += int(i)*hevao**mu
            mu -= 1
        return kq

def ThapSangBatKy(u, hera, he16):
    kq = ''
    if hera == 2:
        for i in range(7, -1, -1):
            if u >= 2**i:
                kq += str(1)
            else:
                kq += str(0)
                continue
            u -= 2**i
        return int(kq)
    if hera == 10:
        return u
    if hera == 16 or hera == 8:
        while True:
            du = u % hera
            if hera == 16:
                kq = he16[du] + kq
            else:
                kq = str(du) + kq
            u //= hera
            if u == 0:
                return kq

n = input('nhap so bat ky: ')
he = [2, 8, 10, 16]
he2 = '01'
he16 = '0123456789ABCDEF'
hevao = int(input('so do thuoc he: '))
hera = int(input('chuyen so do thanh he: '))
if hevao in he and hera in he:
    if hevao == 2:
        for i in n:
            if i in he2 and len(n) <= 8:
                u = True
            else:
                u = False
                break
        if u:
            print(
                f'so duoc chuyen doi thanh: {ThapSangBatKy(BatkySangThap(n, hevao,he16), hera,he16)}')
        else:
            print('so ban nhap khong thuoc he 2')
    else:
        print(
            f'so duoc chuyen doi thanh: {ThapSangBatKy(BatkySangThap(n, hevao,he16), hera,he16)}')
else:
    print('khong tim duoc he ma ban da nhap')