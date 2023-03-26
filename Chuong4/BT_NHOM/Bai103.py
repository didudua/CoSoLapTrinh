def XetNgayKyDieu():
    for nam in range(1901, 2001):
        for thang in range(1, 13):
            ngay = 31
            if thang == 4 or thang == 6 or thang == 9 or thang == 11:
                ngay = 30
            elif thang == 2:
                if nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0):
                    ngay = 29
                else:
                    ngay = 28
            for day in range(1, ngay + 1):
                if day * thang == nam % 100:
                    print(f'{day}/{thang}/{nam}')

print('nhung ngay ky dieu trong the ky 20 la:')
XetNgayKyDieu()