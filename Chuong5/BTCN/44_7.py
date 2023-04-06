L=[]
M=[]
n=int(input('n='))
for i in range(1,n+1):
    L+=[int(input())]
for i in L:
    if i in M: continue
    else: M+=[i]
for i in M:
    print(i,end=' ')