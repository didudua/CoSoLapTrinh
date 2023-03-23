# ta 2 ham , hex2in(): chuyen thap luc phan sang thap phan
# int2hex(): chuyen thap phan sang thap luc phan
def int2hex(n,doi):
    kq = ''
    while True:
        du = n % 16
        kq = doi[du] + kq
        n //= 16
        if n == 0:
            break
    return kq


def hex2in(m,doi):
    mu = len(m)-1
    kq = 0
    for i in m:
        kq += doi.index(i)*16**mu
        mu -= 1
    return kq

doi = '0123456789ABCDEF'
n = int(input('Nhap so thap phan: '))
print(f'doi sang thap luc phan la: {int2hex(n,doi)}')
m = input('Nhap so thap luc phan: ')
print(f'doi sang thap phan la: {hex2in(m,doi)}')
