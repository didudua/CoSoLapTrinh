# 1 coc = 16 muong canh
# 1 muong canh = 3 muong ca phe
# 1 coc = 48 muong ca  phe
def nhap():
    soluong = int(input('so luong: '))
    donvi = input('don vi: ')
    return soluong, donvi


def KetQua(soluong, donvi):
    if donvi == "coc":
        coc = soluong
        muong_canh = 0
        ca_phe = 0
    elif donvi == "muong canh":
        coc = soluong // 16
        muong_canh = soluong % 16
        ca_phe = 0
    elif donvi == "muong ca phe":
        coc = soluong // (16 * 3)
        muong_canh = (soluong % (16 * 3)) // 3
        ca_phe = soluong % 3
    return coc, muong_canh, ca_phe


soluong, donvi = nhap()
coc, muong_canh, ca_phe = KetQua(soluong, donvi)
print(f'{soluong} {donvi} tuong duong {coc} coc, {muong_canh} muong canh, {ca_phe} muong ca phe')
