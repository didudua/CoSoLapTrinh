from math import sqrt
n=int(input('n='))
s=1
for i in range(1,n+1,2):
    s*=sqrt(i)
print(round(s,2))