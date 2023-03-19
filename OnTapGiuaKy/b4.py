s=0
u=0
while True:
    n=int(input())
    if n==0: break
    for i in range(2,n):
        if n%i!=0: u=1
        else: break
    if u==1: s+=1
    if n==2: s+=1
    
print('co',s,'so nguyen to')
