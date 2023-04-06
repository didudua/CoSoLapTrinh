A=[]
u=0
n=int(input('n='))
for i in range(1,n+1):
    A+=[int(input())]
for i in A:
    if A.index(i)%2!=0:
        u+=i
print(f'Tong={u}')