# cslt6.41 130104 tuan nguoi gia
# cslt6.44 151204
# cslt6.15 060604 khoa
# cslt6.19 200304 long
n=int(input('n='))
u=[]
j=0
for x in range(2,9999999):
    for i in range(2,x):
        if x%i==0: break
    else: u+=[str(x)]
    if len(u)==n: break
print(', '.join(u))