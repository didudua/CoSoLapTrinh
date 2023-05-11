# A=[]
# for j in range(10):
#     A+=[int(input())]
# B=A
# for i in range(0,len(A),2):
#     B[i],B[i+1] = A[i+1], A[i]
# print(B)

L=[]
import copy
for i in range(0,10):
    n=int(input())
    L=L+[n]
B=copy.copy(L)
for i in range(0,10,2):
    B[i]=L[i+1]
    B[i+1]=L[i]
for i in B:
    print(i,end=" ")