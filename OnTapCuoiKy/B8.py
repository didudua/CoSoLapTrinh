#Cho mot chuoi ki tu viet chuong trinh de tinh tong cac chu so co 1 chu so trong chuoi. Neu dau tru dung truoc so thi van tinh la so am
#in: nhap vao mot chuoi ki tu
#out: in tong cac chu so xuat hien
#123abc45 -> 15, 1-2-3abc45 -> 5
a=input()
kq=0
for i in range(len(a)):
    if a[i].isnumeric():
        if a[i-1]=='-':
            kq=kq-int(a[i])
        else:
            kq=kq+int(a[i])
print(kq)