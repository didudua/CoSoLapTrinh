import random
n,k=[int(i) for i in input().split()]
A=[]
for i in range(1,n+1):
    A+=[i]
B=A.copy()
if k==0: print(*B)
else:
    while True:
        u=1
        random.shuffle(B)
        for i in range(len(A)):
            if A[i]-B[i]==k or B[i]-A[i]==k:
                u+=1
        if u== len(B): break
            
print(*B)