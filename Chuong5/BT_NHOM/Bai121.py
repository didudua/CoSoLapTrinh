def Input():
    L=[]
    min=int(input('min: '))
    max=int(input('max: '))
    n=int(input('do dai day so:'))
    for i in range(1,n+1):
        L+=[int(input())]
    return L,min,max
def countRange(L,min,max):
    u=0
    for i in L:
        if min<= i < max:
            u+=1
    return u
L,min,max=Input()
print(f'So phan tu >={min},<{max} trong danh sach la: {countRange(L,min,max)}')
