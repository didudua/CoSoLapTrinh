#Tao danh sach moi gom cac phan tu chung
#In: 2 dong, cach nhau 1 ly tu trang
#Out: danh sach moi gom cac phan tu chung
#Red Green White Orange / Green Black White Pink -> Green White
a=input()
b=input()
A=a.split()
B=b.split()
C=[]
for i in A:
    if i in B:
        C+=i
print(' '.join(C))