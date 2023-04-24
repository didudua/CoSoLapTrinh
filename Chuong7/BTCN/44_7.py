l=input()
L=l.split()
email=''
for i in L:
    if '@' in i:
        email=i
        break
print(email)