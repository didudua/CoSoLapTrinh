L=input().split()
kq=[]
for i in L:
    if i not in kq:
        kq+=i
print(len(kq))