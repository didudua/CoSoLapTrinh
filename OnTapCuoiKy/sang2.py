def kiemtra(a,b,c):
    return (a+b+c)/3
def nhap():
    while True:
        a=float(input())
        if 0<=a <=10:
            while True:
                b=float(input())
                if 0<=b <=10:
                    while True:
                        c=float(input())
                        if 0<=c <=10:
                            return a,b,c
                        else: print('khong hop le')
                else:
                    print('khong hop le!')
        else:
            print('khong hop le !')
a,b,c=nhap()
print(kiemtra(a,b,c))

# def nhap():
#     while True:
#         diem=float(input())
#         if diem>=0 and diem<=10:
#             break
#         else:
#             print('Khong hop le!')
#     return diem
# diem1=nhap()
# diem2=nhap()
# diem3=nhap()
# avg=(diem1+diem2+diem3)/3
# print(avg)