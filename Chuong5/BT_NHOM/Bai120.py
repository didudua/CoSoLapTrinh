def Input():
    L=[]
    n=int(input('do dai day so:'))
    for i in range(1,n+1):
        L+=[int(input())]
    return L
def KiemTraSapXep(L):
    if len(L)==0: 
        return 'Day so rong'
    elif len(L)==1:
        return 'Do dai day so >=2'
    else:
        for i in range(1,len(L)):
            if L[i]<L[i-1]:
                tang= False
                break
        else: tang= True
        for i in range(1,len(L)):
            if L[i]>L[i-1]:
                giam= False
                break
        else: giam= True
    return tang or giam
print(KiemTraSapXep(Input()))