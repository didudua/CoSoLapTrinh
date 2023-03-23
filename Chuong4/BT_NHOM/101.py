# nhập vào 2 số nguyên. in ra kết quả phân số tối giản của 2 số đó
def UCLN(a,b):
    if b==0: return a
    else: return UCLN(b,a%b)
a=int(input('Nhap tu so:'))
b=int(input('Nhap mau so:'))
print(f'phan so toi gian {a}/{b} = {int(a/UCLN(a,b))}/{int(b/UCLN(a,b))}')