n=int(input('n='))
x=0
if n==2: x=1
if n>2 and n<=100:
 for i in range(2,n):
    if n%i==0:
        x=0
        break
    else: x=1
 if x==1 : print(n, 'la SNT')
 else: print(n, 'Khong la SNT')
