#Nhập số n, rồi nhập 1 dãy số. Kiểm tra vị trí xuất hiện của số n trong dãy đó. Ví dụ : 
#2
#1 2 3 4 5 2
#in ra: [1,5]
# day_so = [int(x) for x in day_so]
n=int(input())
L=input().split()
L=[int(x) for x in L]
c=[]
for i in range(len(L)):
    if L[i]==n:
        c+=[i]
print(c)