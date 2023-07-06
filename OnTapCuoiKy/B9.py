a=input()
kq=[]
for i in a:
    if i.isnumeric():
        kq.append(i)
print(max(kq))