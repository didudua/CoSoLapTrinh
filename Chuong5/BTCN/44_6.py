A=[]
for j in range(10):
    A+=[int(input())]
B=A
for i in range(0,len(A),2):
    B[i],B[i+1] = A[i+1], A[i]
print(B)

