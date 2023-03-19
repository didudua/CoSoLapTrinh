n=int(input('n='))
s=0
for i in range(1,n+1,2):
    s+=1/i
print('Tong nghich dao cac so le la:',round(s,2))  