# viết chương trình xét xem 1 tháng trong năm đó có bao nhiêu ngày:
# hàm nhận 2 tham số, tháng và năm
def XetNam(thang, nam):
    ngay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ngayn = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if int(nam[-1]) == 0 and int(nam[-2]) == 0:
        if int(nam) % 400 == 0:
            nhuan = True
        else:
            nhuan = False
    else:
        if int(nam) % 4 == 0:
            nhuan = True
        else:
            nhuan = False
    if nhuan:
        print(f'thang {thang}, nam {nam} co {ngayn[int(thang)-1]} ngay')
    else:
        print(f'thang {thang}, nam {nam} co {ngay[int(thang)-1]} ngay')


thang = input('nhap thang: ')
nam = input('nhap nam: ')
XetNam(thang, nam)
