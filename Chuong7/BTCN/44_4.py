l=input()
kq=[]
L=l.split(',')
for i in L:
    if i not in kq:
        kq.append(i)
kq.sort()
print(','.join(kq))