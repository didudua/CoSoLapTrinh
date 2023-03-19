a=int(input('A='))
b=int(input('B='))
s=0
for i in range(1,a):
    if a%i==0 and b%i!=0: s+=i
print(s)
