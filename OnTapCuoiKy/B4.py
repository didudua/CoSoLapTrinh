#Mot danh sach va mot tu, chen phan tu vao truoc moi phan tu trong danh sach
#In: dong 1 day tu cach nhau 1 khoang trang, dong 2 1 tu
#Out: In danh sach moi
#Red Green Black / Blue -> Blue Red Blue Green Blue Black
a=input()
b=input()
B=[]
A=a.split()
for i in A:
    B=B+[b]+[i]
print(' '.join(B))