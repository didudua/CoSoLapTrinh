A=[]
for j in range(4):
    A+=[int(input())]
B=A
for i in range(0,len(A)-1,2):
    B[i],B[i+1] = A[i+1], A[i]
print(B)

