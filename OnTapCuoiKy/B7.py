#3 chuoi, dao nguoc 3 chuoi va in ra man hinh
#in: python list exercises
a=input()
b=input()
c=input()
def daonguoc(a):
    kq=''
    for i in range(len(a)-1,-1,-1):
        kq=kq+a[i]
    return kq
print(daonguoc(a))
print(daonguoc(b))
print(daonguoc(c))