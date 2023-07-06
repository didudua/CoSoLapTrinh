#Nhập số nguyên n, và dãy n số, in  True nếu số đó xuất hiện 1 lần duy nhất. Còn lại false
n=int(input())
L=[]
kq=[]
for i in range(n):
    L.append(int(input()))
for i in L:
    if i==n:
        kq+=[i]
if len(kq)==1: print(True)
else: print(False)