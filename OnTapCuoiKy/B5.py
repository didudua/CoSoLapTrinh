#VCT loai bo cac phan tu trong mot danh sach tai cac vi tri index 1, 3, 4 cho truoc
#Red Green Black Pink Yellow ->  Red White Yellow
a=input()
A=a.split()
A[1],A[3],A[4]='','',''
for i in A:
    if i=='':
        A.remove(i)
print(' '.join(A))