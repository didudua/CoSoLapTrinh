def XetNam(nam):
    if nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0):
        return True

ngay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ngayn = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
thang = input('nhap thang: ')
nam = input('nhap nam: ')
if XetNam(int(nam)):
    print(f'thang {thang}, nam {nam} co {ngayn[int(thang)-1]} ngay')
else:
    print(f'thang {thang}, nam {nam} co {ngay[int(thang)-1]} ngay')