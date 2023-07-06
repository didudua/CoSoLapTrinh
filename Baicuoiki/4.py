def nhap():
    A=[]
    while True:
        a=input()
        if a=='': break
        else:
            A.append(a)
    return A
A=nhap()
for i in range(len(A)):
    A[i]=A[i].replace('Python','J',len(A[i]))
    A[i]=A[i].replace('Java','P',len(A[i]))
    for j in A[i]:
        if j=='P':A[i]=A[i].replace('P','Python',len(A[i]))
        if j=='J':A[i]=A[i].replace('J','Java',len(A[i]))
            
for k in A:
    print(k)