L=[1,2,3,4,5,5,7]
def nhap():
    x=input('nhap x: ')
    k=int(input('vi tri k: '))
    y=input('y thay the x: ')
    return x,k,y
def add(L,x,k):
    if k > len(L):
        L=L.append(x) # them x vao vi tri cuoi cua day
    else: L=L.insert(k,x) # them x vao vi tri k cua day
    return L
#cau 2
def search(L,x):
    if x in L:
        u=L.index(x)
        return u
    else:  return None
#cau 3
def delete(L,x):
    if x in L:
        L=L.clear(x)
    return L
#cau4
def count(L) :
    c=len(L)
    return c
#cau5
def update(L,x,y):
    if x in L:
        L=L.insret(L.index(x),y)
    return L

x,k,y=nhap()
print('cau1')
add(L,x,y)
print(L)
print('cau2')
u=search(L,x)
print(u)
print('cau3')
delete(L,x)
print(L)
print('cau4')
c=count(L)
print(c)
print('cau5')
update(L,x,y)
print(L)
