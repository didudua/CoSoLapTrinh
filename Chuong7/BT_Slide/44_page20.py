str=input('str=')
ch=input('ch=')
u=0
for i in str.lower():
    if i==ch:
        u+=1
print('Number of character n is:',u)