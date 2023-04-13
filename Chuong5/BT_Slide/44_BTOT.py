L = [1, 2, 3, 4, 5, 6, 7]

def nhap():
    x = input('nhap x: ')
    k = int(input('vi tri k: '))
    y = input('y thay the x: ')
    return x, k, y

def add(L, x, k):
    if k > len(L):
        L=L+[x] # them x vao vi tri cuoi cua day
    else:
        L=L[:k]+[x]+L[k:] # them x vao vi tri k cua day
    return L

#cau 2
def search(L, x):
    for i in range(len(L)):
        if str(L[i]) == x:
            return i
    else:
        return None

#cau 3
def delete(L, x):
    # if x in L:
    #     L.remove(x)
    # return L
    for i in range(len(L)):
        if str(L[i]) == x:
            L=L[:i]+L[i+1:]
            return L

#cau4
def count(L) :
    # return len(L)
    u=0
    for i in L:
        u+=1
    return u

#cau5
def update(L, x, y):
    for i in L:
        if str(x) == str(i) :
            # L.insert(L.index(x), y)
            # L.remove(x)
            L=delete(add(L,y,search(L,x)),x)
    return L

x, k, y = nhap()
print('cau 1')
L = add(L, x, k)
print(L)
print('cau 2')
u = search(L, x)
print(u)
print('cau 3')
L = delete(L, x)
print(L)
print('cau 4')
c = count(L)
print(c)
print('cau 5')
L = update(L, x, y)
print(L)