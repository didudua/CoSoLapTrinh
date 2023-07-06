x=input()
X=x.split(',')
kq=[]
for i in X:
    if int(i)% 3==0:
        kq+=[i]
print(','.join(kq))